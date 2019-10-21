# the game True or False assumes that the participant chooses one of the options.
# He will have to answer the 10 questions with only two attempts at error

import local as lc

print(lc.TXT_TASK)

trying = 1
# determine the number of valid attempts
while trying <= 3:
    answer = str.lower(input(lc.TXT_ANS_1))
    if answer == lc.TXT_TRUE:
        trying += 1
    elif answer == lc.TXT_FALSE:
        answer_2 = str.lower(input(lc.TXT_ANS_2))
        if answer_2 == lc.TXT_FALSE:
            answer_3 = str.lower(input(lc.TXT_ANS_3))
            if answer_3 == lc.TXT_TRUE:
                answer_4 = str.lower(input(lc.TXT_ANS_4))
                if answer_4 == lc.TXT_TRUE:
                    answer_5 = str.lower(input(lc.TXT_ANS_5))
                    if answer_5 == lc.TXT_TRUE:
                        answer_6 = str.lower(input(lc.TXT_ANS_6))
                        if answer_6 == lc.TXT_FALSE:
                            answer_7 = str.lower(input(lc.TXT_ANS_7))
                            if answer_7 == lc.TXT_FALSE:
                                answer_8 = str.lower(input(lc.TXT_ANS_8))
                                if answer_8 == lc.TXT_FALSE:
                                    answer_9 = str.lower(input(lc.TXT_ANS_9))
                                    if answer_9 == lc.TXT_TRUE:
                                        answer_10 = str.lower(input(lc.TXT_ANS_10))
                                        if answer_10 == lc.TXT_TRUE:
                                            print(lc.TXT_WIN)
                                        elif answer_10 == lc.TXT_FALSE:
                                            trying += 1
                                    elif answer_9 == lc.TXT_FALSE:
                                        trying += 1
                                elif answer_8 == lc.TXT_TRUE:
                                    trying += 1
                        elif answer_6 == lc.TXT_TRUE:
                            trying += 1
                    elif answer_5 == lc.TXT_FALSE:
                        trying += 1
                elif answer_4 == lc.TXT_FALSE:
                    trying += 1
            elif answer_3 == lc.TXT_FALSE:
                trying += 1
        elif answer_2 == lc.TXT_TRUE:
            trying += 1
else:
    print(lc.TXT_END)