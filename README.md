# Whatsapp_Bot_For_PC_App (Window OS Only)
A simple Whatsapp Chat Bot(For Whatsapp PC) used for replying to Messages based on the responses in The Repository Created by the User...Sometimes It needs Calibration based on Whatsapp Window...
and It also needs some packages to be installed before The Execution of Programs since.
In the Terminal
pip install pyautogui
pip install opencv-python (for Image recognition)

Basically What this Programme does is ..Every 10 secs It Searches for A New message.
i.e It compares a provided image of a greendot in its repository with the greendot on the Screen and if there is a match it auto clicks on the senders chat and then looks for the paper clip that is  beside the chat menu..From there it is specified how much Upward movement it needs to do to reach the new message..there it copies the new messge compares it with its responses provided by the user ..Then it  Serach for paperclip again on the screen and from there it knows the referal distance of the messaging area..It types it message and sends it.Then it retrys after 10secs again......
