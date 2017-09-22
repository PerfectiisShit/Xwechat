# Xwechat
Running wechat in shell terminal

## Send message
![image](https://github.com/MrDreamerSang/Xwechat/blob/master/Xwx3.PNG)

## Display message and list recent chats only
![image](https://github.com/MrDreamerSang/Xwechat/blob/master/Xwx1.PNG)

## Display message and list all friends
![image](https://github.com/MrDreamerSang/Xwechat/blob/master/Xwx2.PNG)


## Start application(actually just a script, only can run in python3)
<pre> python mybot.py </pre>


## Usage
After you start the application, you just need to wait for messages coming. After you received messages, you can move the cursor in the right screen and choose a friend/group to send message and then press enter, the application will wait for you to type messaeges(like picture1). After your typed messages, press enter to send the message.

## Improvements
0. Daemonize the application
1. Add a robot to reply message automaticially
2. Optimize typing while send message. For now, you can not revoke or delete what you have typied while send messages as the "delete" key in the keyboard doesn't work. 
3. Add the return fuction so that we can cancel sending messages. Then you can choose another friend/group to send messages or just view the messages only
4. Optimize system exit hanlder and asyncio loop close