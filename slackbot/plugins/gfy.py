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
                            from_=random.choice(BEAST)).text)


@respond_to('possibles', re.IGNORECASE)
def possibles(message):
    poss = ['awesome(from_)', 'ballmer(name, company, from_)', 'because(from_)', 'bus(name, from_)', 'bye(from_)', 'caniuse(namer, from_)', 'chainsaw(name, from_)', 'cool(from_)', 'diabetes(from_)', 'donut(name, from_)', 'everyone(from_)', 'everything(from_)', 'fascinating(from_)', 'field(name, from_, reference)', 'flying(from_)', 'king(name, from_)', 'life(from_)', 'linus(name, from_)', 'madison(name, from_)', 'nugget(name, from_)', 'off(name, from_)', 'outside(name, from_)', 'pink(from_)', 'thanks(from_)', 'that(from_)', 'thing(thing, from_)', 'this(from_)', 'random(name, from_)', 'shakespeare(name, from_)', 'what(from_)', 'xmas(name, from_)', 'yoda(name, from_)', 'you(name, from_)', ]
    #  possibles = [

    for elem in poss:
        fuck_name = elem.split('(')[0]
        fuck_param = elem.split('(')[1].strip(')')
        print('''def {}:
    """{} docstring"""
    message.reply(fuck.{}({}))
    '''.format(elem, fuck_name, fuck_name, fuck_param))

    #  message.reply(possibles)


possibles(message='suck it')
