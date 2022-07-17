# simple_telebot
Simple to use wrapper for telepot

By default this package uses [TimeToCheckBot](http://t.me/TimeToCheckBot). Add this telegram bot and press 'START'. After this you should check your Telegram ID using [userinfobot](https://t.me/userinfobot). Save your ID to a file.

## Install

Install the latest version from Github:

`pip install git+https://github.com/msipola/simple_telebot.git`

## Usage

    from simple_telebot import initBot, sendMessage
    bot, chat_id = initBot(id_file)
    sentMessage(message,bot,chat_id)

### Versions

The simple_telebot project uses the [semantic versioning](https://semver.org) scheme. The latest release is [v0.1.0](https://github.com/msipola/simple_telebot/releases).
