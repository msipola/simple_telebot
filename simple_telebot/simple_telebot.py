def initBot(id_file):
    """/
    Initiate the bot with the id_file. The if_file is a file containing your Telegram id. Returns the bot and chat_id.
    """
    import telepot
    import re
    bot = telepot.Bot('5544476478:AAEUgpwQAZtX2B4zYxWFHb7xHM85kAG_kS0')
    
    with open(id_file) as f:
        lines = f.readlines()
    f.close()
    
    chat_id = re.findall(r'\d+', lines[0])[0]
    print('Initiated successfully!')
    return bot, chat_id

def sendMessage(message,bot,chat_id):
    """/
    Send a message to the bot. Takes as an argument a string you want to send. Before running this function, you should initiate the bot with initBot().
    """
    bot.sendMessage(text=message,chat_id=chat_id)
    return 'Message sent successfully!'