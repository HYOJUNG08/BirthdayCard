# Automated BirthdayCard
![HBD](https://user-images.githubusercontent.com/104620291/176481407-61b09fa7-244a-40d0-8116-0072af89a041.gif)
<p align="center"><img width="22%" src="https://user-images.githubusercontent.com/104620291/176481609-7a3ee581-776e-4ae2-a2a2-e1cf2c171771.gif"/></p>

# Project Description
This project automatically sends messages at a specific time. Sometimes, we want to celebrate a friend's birthday at midnight but go to bed earlier than midnight. Then, you need this tool to send you messages automatically at midnight. You can save your birthday card before the birthday; this tool will send the saved messages at midnight.   

# Technologies Use
HTML   
CSS   
Python   
MongoDB   
FLASK   
Twilio API   
Bootstrap   
MDBootstrap   

# How to use the project
1. Click 'Start' button
2. Submit your friend's birthday, phone number, and birthday card
3. Done!

# How it works
### submit.html
: get data from the user (birthday, phone number, message)    

### server.py
: get data from submit.html and pass the data to the database.py   

### database.py
: put the data into database    

### message.py
: check the database every midnight and find the person whose birthday is today   
: get the phone number and message from the database and send the birthday message at midnight automatically   
