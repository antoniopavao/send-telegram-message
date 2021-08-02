# send-telegram-message
Code to send messages with telegram in the easiest way! With Python!
# Creating your bot
On Telegram, search @ BotFather, send him a “/start” message
Send another “/newbot” message, then follow the instructions to setup a name and a username
Your bot is now ready, be sure to save a backup of your API token, and correct, this API token is your bot_token

# Getting your Chat id

On Telegram, search your bot (by the username you just created), press the “Start” button or send a “/start” message
Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> with your API token, press enter and you should see something like this:

{"ok":true,"result":[{"update_id":77xxxxxxx,
"message":{"message_id":550,"from":{"id":34xxxxxxx,"is_bot":false,"first_name":"Man Hay","last_name":"Hong","username":"manhay212","language_code":"en-HK"}
Look for “id”, for instance, 34xxxxxxx above is my chat id. Look for yours and put it as your bot_chatID in the code above
Now you are all set, run the code, and enjoy receiving messages from yourself :)
