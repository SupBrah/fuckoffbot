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

MAN = ['Evan', 'Matt']
BEAST = ['Shardik', 'Linus']


@listen_to('^fuck off$', re.IGNORECASE)
def fuck_off(message):
    """You don't get to tell me to fuck off!"""
    message.reply('No, you fuck off!!!')


@respond_to('random', re.IGNORECASE)
def random_fuckoff(message):
    """Respond to 'random' with a fuck.random element."""
    message.reply(fuck.random(name=random.choice(MAN),
                              from_=random.choice(BEAST)).text)


@respond_to('yoda', re.IGNORECASE)
def yoda(message):
    """Respond to 'yoda' with a fuck.yoda element."""
    message.reply(fuck.yoda(name=random.choice(MAN),
                            from_=random.choice(BEAST)))
