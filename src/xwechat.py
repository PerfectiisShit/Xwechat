#!/usr/bin/env python

import asyncio
from asyncio import FIRST_EXCEPTION, CancelledError
from concurrent.futures.thread import ThreadPoolExecutor
import curses
import signal

from wxpy import Bot
from utils import ensure_one
from ncurses import MainWindow
from _messages import _Message
from _db import MessageDb


class XWechat(object):
    def __init__(self, interval=0.5):
        self.db = MessageDb()
        self.bot = Bot(console_qr=True)
        self.bot.enable_puid("/tmp/wxpy_puid.pkl")
        self.interval = interval
        self.mwin = MainWindow(curses.initscr(), self.db)
        self.loop = asyncio.get_event_loop()
        self.executor = ThreadPoolExecutor()
        self.friends = self.bot.friends()
        self.groups = self.bot.groups()
        self.friends.extend(self.groups)
        self.mwin.rwin.friends = self.friends

    async def update_db(self):
        try:
            while True:
                if self.bot.messages.updated:
                    new_messages = [_Message(m) for m in self.bot.messages if not m.read]
                    self.bot.messages.updated = False
                    self.db.process(new_messages)
                # wxpy retrieves messages every 0.5s, keep the db updating messages every 0.5s as well
                await asyncio.sleep(0.5)

        except CancelledError:
            return

    async def print_msg(self):
        try:
            while True:
                # query chaters which has sent messages to you after you login
                results = self.db.search_chats()
                chats = [ensure_one(self.bot.search(puid=chat)) for chat in results]
                non_none = lambda x: x is not None and x != ""
                self.mwin.rwin.chats = list(filter(non_none, chats))
                # query all received messages which will be displayed in the left screen
                self.mwin.lwin.messages = self.db.search_all()
                # if chose chater, then query all messages received from or sent to this chater
                if self.mwin.rwin.chater:
                    self.mwin.rwin.messages = self.db.search_user_msg(self.mwin.rwin.chater.puid)
                self.mwin.update()
                # Make sure the cursor will back to the right bottom screen after updating the messages
                if self.mwin.rwin.is_typed:
                    self.mwin.rwin.right_bottom_screen.refresh()

                await asyncio.sleep(self.interval)

        except CancelledError:
            return

    async def listener_executor(self):
        # https://docs.python.org/3/library/asyncio-eventloop.html
        # The listener is a blocking function, calling the listener in a Executor
        # which is pool of threads will avoid blocking other tasks
        self.loop.set_default_executor(self.executor)
        await self.loop.run_in_executor(None, self.mwin.listener)

    async def asynchronous(self):
        tasks = [asyncio.ensure_future(task) for task in [self.listener_executor(), self.update_db(), self.print_msg()]]
        done, pending = await asyncio.wait(tasks, return_when=FIRST_EXCEPTION)
        for pending_task in pending:
            pending_task.cancel()

        # listener is running in executor, can not cancel a running task inside executor,
        #   just manually exit the blocking process window.getch() by push 'q' to getch()
        if not self.mwin.isendwin:
            self.mwin.exit(raise_exception=False)

    def terminal(self):
        # Send 'q' to the listener of curses to raise a Exception
        #   so that asyncio.wait return and cancel all pending tasks
        self.mwin.exit(raise_exception=True)

    def cleanup(self):
        self.mwin.destroy()
        self.bot.logout()
        self.db.close()

    def run(self):
        try:
            self.loop.add_signal_handler(signal.SIGTERM, self.terminal)
            self.loop.add_signal_handler(signal.SIGINT, self.terminal)
            self.loop.run_until_complete(self.asynchronous())
            self.executor.shutdown(wait=True)
            self.loop.close()
        finally:
            self.cleanup()


if __name__ == '__main__':
    xwechat = XWechat()
    xwechat.run()
