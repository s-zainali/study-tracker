import time
import chime

BREAK = 0
STUDY = 0

FLAG_STUDY = False
FLAG_BREAK = False

BREAK_IN_DEBT = False

STUDY_SESSION = 45

mins_to_secs = lambda minutes : minutes * 60
secs_to_mins = lambda seconds : seconds / 60


def play_alarm():
    chime.theme("zelda")
    chime.success()


def start_study(session_time:int):
    global STUDY, BREAK, FLAG_STUDY, FLAG_BREAK, STUDY_SESSION

    FLAG_STUDY = False

    break_counter = 0

    while not FLAG_STUDY:
        time.sleep(0.125)
        STUDY += secs_to_mins(0.125) 
        break_counter += 0.125

        if break_counter >= 3.5:
            break_counter = 0
            BREAK += secs_to_mins(1)
            # BREAK += 1
        
        if STUDY % STUDY_SESSION == 0:
            if STUDY_SESSION > 30:
                STUDY_SESSION -= 5
            BREAK += 30

    FLAG_STUDY = False



def start_break():
    global BREAK, FLAG_BREAK, BREAK_IN_DEBT

    FLAG_BREAK = False

    while not FLAG_BREAK:
        time.sleep(0.125)
        BREAK -= 0.125 / 60

        if not BREAK_IN_DEBT and BREAK <= 0:
            play_alarm()
            BREAK_IN_DEBT = True

        if BREAK >= 0:
            BREAK_IN_DEBT = False
    
    FLAG_BREAK = False
