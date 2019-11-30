from slackbot.bot import listen_to

'''
スレッド追跡
    ref@ https://api.slack.com/docs/message-threading#finding_message_threads_in_the_wild
'''
@listen_to("Howdy")
def greet(message):
    message.reply("Howdy to as well", in_thread=True)
