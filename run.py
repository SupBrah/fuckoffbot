#!/usr/bin/env python

import sys
import re
import logging
import logging.config
import random
from slackbot import settings
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from foaas import Fuck

fuck = Fuck(secure=True)


def main():
    kwargs = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kwargs)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
    bot = Bot()
    bot.run()


@respond_to('random', re.IGNORECASE)
def random_fuckoff(message):
    man = ['Evan', 'Matt']
    beast = ['Shardik', 'Linus']
    both = man + beast

    message.reply(fuck.random(name=random.choice(man), from_=random.choice(beast)).text)


@respond_to('hiya', re.IGNORECASE)
def hiya(message):
    message.reply('I can understand hiya or HIYA!')
    # react with thumb up emoji
    message.react('+1')


@listen_to('Fuck off')
def fuck_off(message):
    message.reply('No, you fuck off!!!')


@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)


if __name__ == '__main__':
    main()
