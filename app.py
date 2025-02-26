import time
import threading

BREAK = 0
STUDY = 0

mins_to_secs = lambda minutes : minutes * 60
secs_to_mins = lambda seconds : seconds / 60


def start_study(session_time):
    global STUDY, BREAK

    break_counter = 0

    while STUDY < session_time:
        time.sleep(0.125)
        # STUDY += secs_to_mins(0.1) TODO
        STUDY += 0.125
        break_counter += 0.125

        if break_counter >= 3.5:
            break_counter = 0
            # BREAK += secs_to_mins(1) TODO
            BREAK += 1

    STUDY = 0



def start_break():
    global BREAK

    elapsed = 0

    while elapsed < 3:
        time.sleep(0.5)
        BREAK -= 0.5
        elapsed += 0.5

    