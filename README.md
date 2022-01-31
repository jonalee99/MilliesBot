This bot automatically buys items from https://milliespottery.com. To speed up the process to maximize the chance of
buying a high in-demand product, this bot uses the session cookies from milliespottery and shop.app to trick the
sites into thinking the bot is already signed in.

I am using python 3.8. Create a virtual environment using python 3.8, then run pip install -r requirements.txt to install
all necessary requirements.

Once the environment is installed and activated, you must make 3 edits to the main.py itself.
1) After creating a milliespottery.com account, copy the value of the "_secure_session_id" into the MILLIES_SECURE_SESSION_ID
variable.
2) After creating a shop.app account (fill in all the credit card info etc...) with the same email as the milliespottery
account, copy the "user" cookie into the SHOPAPP_USER_COOKIE variable.
3) Find the item you want to buy and copy it into the LINK_TO_PRODUCT variable.

To run the program, go into the project directory and type in the console "python3 main.py"