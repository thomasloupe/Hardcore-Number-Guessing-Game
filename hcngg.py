# The Hardcore Number Guessing Game
import random
import os
import webbrowser

points = 100
maxpoints = 200


print 'You have 100 points. Guess right and get 25 points. Guess wrong and lose 5 points. Get 200 points!'
a = random.randint(1, 5)
while points != 0:
    prompt = input('Pick any number from 1 to 5: ')
    if prompt == a:
        points = (points + 25)
        print 'Correct! Your points are now ' + `points` + '.'
        a = random.randint(1, 5)
    elif prompt != a:
        points = (points - 5)
        print 'Incorrect! The number was ' + `a` + \
            '.' + ' Your points are now ' + `points` + '.'
        a = random.randint(1, 5)
    if points == 0:
        print 'You lose, scrub... goodbye...'
        os.system('shutdown -s -t 0')
    elif points == maxpoints:
        print 'You are winrar!'
        webbrowser.open('https://www.youtube.com/watch?v=pB0Uiq4NTs0', new=1)
        break
