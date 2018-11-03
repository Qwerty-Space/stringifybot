# stringifybot

## Installation and Setup

1. `git clone https://github.com/Qwerty-Space/qbot.git stringifybot`
1. `cd stringifybot`
1. `rm -rf plugins`
1. `git clone https://github.com/Qwerty-Space/stringifybot.git plugins`
1. `pip install -r requirements.txt`
1.  `cp example_config.ini config.ini`
1.  Follow this [link][my telegram] and login with your phone number
1.  A Create new application window will appear.  Fill in your application details.  There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
1.  Click on Create application at the end.  
1.  Add your api id, api hash, and other information to `config.ini`
    -  Create a bot with botfather if you need/want to
    -  If you want a userbot; add your phone number to `PHONE`, if you want an api bot; add your bot token to `TOKEN`
1.  Start bot  

#### Remember that your API hash is secret and Telegram won’t let you revoke it.  Don’t post it anywhere!

[my telegram]: https://my.telegram.org/
