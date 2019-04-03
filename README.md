# CS303 Updater :iphone:
This script simply checks for commit updates during class.

It is helpful if you cannot make it to class for some reason, but would still like to participate in the in-class activities.

## Requirements

### Python 3

Ensure you have Python 3 installed, and a bash environment to run the code in. 

Note that if your Python interpreter is utilized with a command other than ``` python3 ```, then you will have to change the line ``` python3 303script.py ``` in the file ``` 303script.bash ``` accordingly.

### Git

Clone the repository with ``` git clone https://github.com/gaurav-karna/303_Texter ```

### Twilio Account

To enable texting, you need a [trial Twilio account](https://www.twilio.com/try-twilio). Create
a project, and get your project's ``` account_sid ``` and ``` auth_token ```. 

## Run Script

Ensure the corresponding variables for ``` account_sid ``` and ``` auth_token ``` are saved 
in ``` 303script.py```. 

In the file, ``` 303script.py ``` - ensure you change ``` twilio_phone ``` to the phone number granted by Twilio for your project, and add your personal phone number to the ``` my_phone ``` space.

Navigate to the repository in the terminal, and run ``` bash 303script.bash ```, and if there is an update to the repository during class - you will get a text at the phone number you provided.

## Improvements
I'll automate the updating of the commit even further when I have more time. It involves a commit updater when you first start the bash script.

I have also thought of using web hooks, and RSS feeds. But putting that on the back-burner for the time being.

For now - this works as a novel solution. If there any problems, open an issue and let me know :blush:
