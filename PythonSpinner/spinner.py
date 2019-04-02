# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import sys
import re
import os
from datetime import timedelta
import datetime


CALLED = 0
def test_callback_true():
    '''
    test_callback which returns true and then false
    '''
    global CALLED
    CALLED = CALLED + 1
    if CALLED < 25: # equals ~ 5s = 0,2 * 50
        return True
    else:
        CALLED = 0
        return False

def test_callback_false():
    '''
    test_callback which returns true and then false
    '''
    global CALLED
    CALLED = CALLED + 1
    if CALLED < 25: # equals ~ 5s = 0,2 * 50
        return False
    else:
        CALLED = 0
        return True
'''
LOADING ANIMATION AND COUNTDOWN
'''
def loading_bar(progress=0, loading_style='■', state=None):
    '''
    shows progress/loading bar
    100 = 100%
    50 = 50%
    etc.
    '''
    if len(loading_style) != 1:
        loading_style='■'

    if progress > 100:
        progress = 100
    if progress <= 0:
        progress = 1
    terminal_size = os.popen('stty size', 'r').read().split()
    terminal_width = int(terminal_size[1])
    terminal_width_prog = int((float(terminal_width - 2)/ 100.0) * float(progress))
    if terminal_width_prog <1:
        terminal_width_prog = 1
    terminal_loadingbar = str(terminal_width_prog * loading_style) + str((terminal_width - 2 - terminal_width_prog)* ' ')
    if state:
        print(str(state) + str((terminal_width - len(state) +2) *' '))
    print('[' + str(terminal_loadingbar) + ']' + '\r' ,end='')
    sys.stdout.flush()


def sleep(interval_time=0, countdown=False, callback=None, negative=False, loading_anim=None):
    '''
    makes cool print effect with countdown, to show it is working and not crashed
    '''
    if loading_anim and (len(loading_anim) > 2):
        loading_anim = loading_anim
    else:
        loading_anim = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘'] # rotating moon
        # loading_anim = ['🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛'] # rotation clock
        # loading_anim = ['|','/','–','\\'] # rotating slash

    length_index = len(loading_anim)
    anim_index = 0

    '''
    if got callback and check while false
    '''
    if callback and negative:
        while not callback():
            print(str(loading_anim[anim_index]) + '\r' ,end='')
            time.sleep(0.2)
            anim_index = anim_index + 1
            if anim_index == length_index:
                anim_index = 0
            sys.stdout.flush()
        return
    '''
    if got callback and check while true
    '''
    if callback:
        while callback():
            print(str(loading_anim[anim_index]) + '\r' ,end='')
            time.sleep(0.2)
            anim_index = anim_index + 1
            if anim_index == length_index:
                anim_index = 0
            sys.stdout.flush()
        return
    '''
    doing for given interval
    '''
    if interval_time <= 0:
        return
    end_time = datetime.datetime.now() + timedelta(seconds=interval_time)
    while datetime.datetime.now() <= end_time:
        if countdown:
            remaining_raw = end_time - datetime.datetime.now()
            expr = '[0-9]+:[0-9]+:[0-9]+'
            match = re.search(expr, str(remaining_raw))
            if match:
                remaining = match.group(0)
            else:
                remaining = str(remaining_raw) # full formatted time
            print(str(loading_anim[anim_index]) + ' Remaining: ' + str(remaining) + '\r' ,end='')
        else:
            print(str(loading_anim[anim_index]) + '\r' ,end='')
        time.sleep(0.2)
        anim_index = anim_index + 1
        if anim_index == length_index:
            anim_index = 0
        sys.stdout.flush()
    return
facepalm = '''
............................................________
....................................,.-'"...................``~.,
.............................,.-"..................................."-.,
.........................,/...............................................":,
.....................,?......................................................,
.................../...........................................................,}
................./......................................................,:`^`..}
.............../...................................................,:"........./
..............?.....__.........................................:`.........../
............./__.(....."~-,_..............................,:`........../
.........../(_...."~,_........"~,_....................,:`........_/
..........{.._$;_......"=,_......."-,_.......,.-~-,},.~";/....}
...........((.....*~_......."=-._......";,,./`..../"............../
...,,,___.`~,......"~.,....................`.....}............../
............(....`=-,,.......`........................(......;_,,-"
............/.`~,......`-...................................../
.............`~.*-,.....................................|,./.....,__
,,_..........}.>-._...................................|..............`=~-,
.....`=~-,__......`,.................................
...................`=~-,,.,...............................
................................`:,,...........................`..............__
.....................................`=-,...................,%`>--==``
........................................_..........._,-%.......`
...................................,
'''

if __name__ == '__main__':
    # print(facepalm)
    # look cool while waiting and idling
    print('Starting showtime:')
    print('Loading anim for time interval with countdown \nExample: sleep(5.0, countdown=True|False|None)')
    sleep(5.0, countdown=True)
    print('Loading anim while callback returns TRUE \nExample: sleep(callback=callable_function)')
    sleep(callback=test_callback_true)
    print('Loading anim while callback returns FALSE \nExample: sleep(callback=callable_function, negative=True)')
    sleep(callback=test_callback_false, negative=True)
    print('Loading anim with another animation via arguments \nExample: sleep(5.0, loading_anim=[" .  "," .. "," ..."])')
    sleep(5.0, loading_anim=[" .  "," .. "," ..."])
    x = 0
    state = 'Removing old files…'
    print('Loadingbar Example: loading_bar(0 - 100, loading_style="■", state="…")')
    while x <= 100:
        if x == 20:
            state = 'Configuring files…'
        if x == 40:
            state = 'Copy new files…'
        if x == 80:
            state = 'Install new files…'
        loading_bar(x, loading_style="■",state=state)
        state = None
        time.sleep(0.5)
        x = x + 10
    print('\nDONE')
