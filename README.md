# Xwechat
Running wechat in shell terminal

## Send message(Press Enter key in your keyboard)
![image](https://github.com/MrDreamerSang/Xwechat/blob/master/xwx11.PNG)

## Display messages and list recent chats only(Press 'b' or 'B' key in your keyboard)
![image](https://github.com/MrDreamerSang/Xwechat/blob/master/xwx12.PNG)

## Display messages and list all friends(Press 'a' or 'A' key in your keyboard)
![image](https://github.com/MrDreamerSang/Xwechat/blob/master/xwx13.PNG)


## Start application(actually just a script, requires python3 and wxpy module)
<pre> python xwechat.py </pre>


## Usage
Press 'A'/'a'  ->  display all of your friends and groups in the right screen

Press 'B'/'b'  ->  only display recent chats(sent messages to you or received messages after you run the xwechat)

Press the direction key 'Up'/'Down'/'Right'/'Left'  ->  choose a friend/group to start the chats

Press 'Enter'  ->  switch to the chat screen like the picture 1 above. It will generate two screens, the top one will display the messages you sent to or received from the friend/group you have chosen; the bottom one will wait for your inputs and send the message to the chosen friend/group

## Tips for the chats
1. How to delete/rewrite messages you have typed?
  While you are typing messages, if you want to delete/rewrite the messages, just press the DELETE key and then press Enter, it will then ask you to re-type messages

2. How to exit the chat page and list your friends/groups/contacts?
  While you are typing messages, if you don't want to send the messages out and you want to return back to the page to display friends/groups/contacts, just press ESC key and then press Enter, it will go back to the friends list page
  And if you didn't type anything yet, then just press Enter, it wil then go back to the friends list page as well.

## Improvements
0. Daemonize the application
1. Add a robot to reply message automaticially
2. Optimize typing while send message. For now, you can not revoke or delete what you have typied while send messages as the "delete" key in the keyboard doesn't work. 
3. Add the return fuction so that we can cancel sending messages. Then you can choose another friend/group to send messages or just view the messages only
4. Optimize system exit hanlder and asyncio loop close
