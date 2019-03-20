#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import gtts
import os
import playsound
import datetime
import random

if len(sys.argv) < 2:
    print 'Usage: {} <wordlist file>'.format(sys.argv[0])
    exit(1)

reload(sys)
sys.setdefaultencoding('utf8')

with open(sys.argv[1], 'r') as f:
    words = f.read().splitlines()

language = sys.argv[2] if len(sys.argv) >= 3 else 'en'

random.shuffle(words)

if not os.path.isdir('./sounds'):
    os.mkdir('./sounds')
if not os.path.isdir('./results'):
    os.mkdir('./results')

answers = []

for word in words:
    sys.stdout.write('> ')
    sys.stdout.flush()

    if not os.path.isfile('sounds/{}_{}.mp3'.format(word, language)):
        tts = gtts.gTTS(word, language)
        tts.save('sounds/{}_{}.mp3'.format(word, language))

    playsound.playsound('sounds/{}_{}.mp3'.format(word, language))

    answer = raw_input()
    answers.append(answer)

score = []
output = []

output.append('Correct, Expected, Obtained')

for word, answer in zip(words, answers):
    correct = word.lower() == answer.lower()
    score.append(int(correct))
    output.append('{}, {}, {}'.format(str(correct).rjust(5), word, answer))

score = int(100*float(sum(score))/len(score))

output.append('Score: {}%'.format(score))

output = '\n'.join(output)

with open('results/{}%_{}_{}.csv'.format(score, str(datetime.datetime.now()), language), 'w') as f:
    f.write(output)

print output