# insta-following-count
A script that keeps track of your Instagram following count.

This bot:
* Logs in to your IG account
* Get your number of following accounts
* Compares it to your desired number of following accounts
* Sends an email if the last two don't match

## Environment variables
Some env vars can be provided in an `.env` file:

```shell
APP_NAME=insta-following-count
LOGS_FOLDER_PATH=logs
DESIRED_FOLLOWING=666
IFC_EMAIL_SENT=0
LAN=EN
SMTP_PORT=587
SMTP_SERVER=smtp.gmail.com
SENDER_EMAIL=sender@gmail.com
EMAIL_PASSWORD=senderemailpassword
RECEIVER_EMAIL=receiver@gmail.com
IG_USERNAME=igusername
IG_PASSWORD=igpassword
```