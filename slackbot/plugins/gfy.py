#!/usr/bin/env python3

import sys
import re
import logging
import logging.config
import random
from random import choice as randchoice
from slackbot import settings
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from foaas import Fuck

fuck = Fuck(secure=True)

MAN = ['Evan', 'Matt']
BEAST = ['Shardik', 'Linus']
BOTH = MAN + BEAST

name = random.choice(BOTH)
from_ = random.choice(BOTH)


def choose_random():
    return randchoice(BOTH)


@listen_to('^fuck off$', re.IGNORECASE)
def fuck_off(message):
    """You don't get to tell me to fuck off!"""
    message.reply('No, you fuck off!!!')


@respond_to('random', re.IGNORECASE)
def random_fuckoff(message):
    """Respond to 'random' with a fuck.random element."""
    message.reply(fuck.random(name=random.choice(BOTH),
                              from_=random.choice(BOTH)).text)


@respond_to('yoda', re.IGNORECASE)
def yoda(message):
    """Respond to 'yoda' with a fuck.yoda element."""
    message.reply(fuck.yoda(name=random.choice(BOTH),
                            from_=random.choice(BOTH)).text)


@respond_to('you', re.IGNORECASE)
def you(message):
    """you docstring"""
    name = choose_random()
    from_ = choose_random()
    #  message.reply(fuck.you(name=name))
    print(fuck.you(name=name, from_=from_).text)


@respond_to('possibles', re.IGNORECASE)
def possibles(message):
    #  poss = ['awesome(from_)', 'ballmer(name=random.choice(BOTH)=, company, from_)',]# 'because(from_)', 'bus(name, from_)', 'bye(from_)', 'caniuse(namer, from_)', 'chainsaw(name, from_)', 'cool(from_)', 'diabetes(from_)', 'donut(name, from_)', 'everyone(from_)', 'everything(from_)', 'fascinating(from_)', 'field(name, from_, reference)', 'flying(from_)', 'king(name, from_)', 'life(from_)', 'linus(name, from_)', 'madison(name, from_)', 'nugget(name, from_)', 'off(name, from_)', 'outside(name, from_)', 'pink(from_)', 'thanks(from_)', 'that(from_)', 'thing(thing, from_)', 'this(from_)', 'random(name, from_)', 'shakespeare(name, from_)', 'what(from_)', 'xmas(name, from_)', 'yoda(name, from_)', 'you(name, from_)', ]
    BOTH = 'BOTH'
    poss = ["awesome(from_=random.choice(BOTH))", "ballmer(name=random.choice(BOTH), company='Fuck.com', from_=random.choice(BOTH))", "because(from_=random.choice(BOTH))", "bus(name=random.choice(BOTH), from_=random.choice(BOTH))", "bye(from_=random.choice(BOTH))", "caniuse(name=random.choice(BOTH), from_=random.choice(BOTH))", "chainsaw(name=random.choice(BOTH), from_=random.choice(BOTH))", "cool(from_=random.choice(BOTH))", "diabetes(from_=random.choice(BOTH))", "donut(name=random.choice(BOTH), from_=random.choice(BOTH))", "everyone(from_=random.choice(BOTH))", "everything(from_=random.choice(BOTH))", "fascinating(from_=random.choice(BOTH))", "field(name=random.choice(BOTH), from_=random.choice(BOTH), reference='Reference')", "flying(from_=random.choice(BOTH))", "king(name=random.choice(BOTH), from_=random.choice(BOTH))", "life(from_=random.choice(BOTH))", "linus(name=random.choice(BOTH), from_=random.choice(BOTH))", "madison(name=random.choice(BOTH), from_=random.choice(BOTH))", "nugget(name=random.choice(BOTH), from_=random.choice(BOTH))", "off(name=random.choice(BOTH), from_=random.choice(BOTH))", "outside(name=random.choice(BOTH), from_=random.choice(BOTH))", "pink(from_=random.choice(BOTH))", "thanks(from_=random.choice(BOTH))", "that(from_=random.choice(BOTH))", "thing(thing, from_=random.choice(BOTH))", "this(from_=random.choice(BOTH))", "random(name=random.choice(BOTH), from_=random.choice(BOTH))", "shakespeare(name=random.choice(BOTH), from_=random.choice(BOTH))", "what(from_=random.choice(BOTH))", "xmas(name=random.choice(BOTH), from_=random.choice(BOTH))", "yoda(name=random.choice(BOTH), from_=random.choice(BOTH))", "you(name=random.choice(BOTH), from_=random.choice(BOTH))", ]

    for elem in poss:
        #  print(elem.split()[0])
        fuck_name = elem.split('(')[0]
        fuck_param = elem.split('(')[1].strip(fuck_name)
        fuck_param_list = elem.split(',')
        for param in fuck_param_list:
            print('param: {}'.format(param))

        print('''@respond_to('{}', re.IGNORECASE)
def {}(message):
    """{} docstring"""
    name = chose_random()
    from_=chose_random()
    message.reply(fuck.{}({}(BOTH)))

'''.format(fuck_name, fuck_name, fuck_name, fuck_name, fuck_param))

    #  message.reply(possibles)


possibles(message='hi')


