# StringifyBot

A bot for showing MTProto events:  @[StringifyBot]

[StringifyBot]: https://t.me/StringifyBot

## Requirements
- The [Nix package manager](Nix)
- A brain definitely

[Nix]: https://nixos.org/

---

## Installation and Setup

1.  `cp config.example.py config.py`
1.  Follow this [link][my telegram] and login with your phone number
1.  A "Create New Application" window will appear.  Fill in your application details.  There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
1.  Click on Create application at the end.  
1.  Add your api id, api hash, and other information to `config.py`
    -  To get the `token`, you must create a bot with botfather
1. Run the bot with `nix-shell --run 'python bot.py'`

#### Remember that your API hash is secret and Telegram won’t let you revoke it.  Don’t post it anywhere!
