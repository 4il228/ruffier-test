from instructions import *
def get_ruffier_index(p1, p2, p3):
    ruffier_index = (4*(p1 + p2 + p3) - 200 / 10)
    return ruffier_index
def get_heart_performance(ruffier_index, user_age):
    if user_age >= 15:
        if ruffier_index >= 15:
            return HP_LOW
        elif ruffier_index >= 11:
            return HP_OKAY
        elif ruffier_index >= 6:
            return HP_MEDIUM
        elif ruffier_index >= 0.5:
            return HP_UPPERMEDIUM
        else:
            return HP_HIGH
    if user_age >= 13:
        if ruffier_index >= 16.5:
            return HP_LOW
        elif ruffier_index >= 12.5:
            return HP_OKAY
        elif ruffier_index >= 7:
            return HP_MEDIUM
        elif ruffier_index >= 2:
            return HP_UPPERMEDIUM
        else:
            return HP_HIGH
    if user_age >= 11:
        if ruffier_index >= 18:
            return HP_LOW
        elif ruffier_index >= 14:
            return HP_OKAY
        elif ruffier_index >= 9:
            return HP_MEDIUM
        elif ruffier_index >= 3.5:
            return HP_UPPERMEDIUM
        else:
            return HP_HIGH
    if user_age >= 9:
        if ruffier_index >= 19.5:
            return HP_LOW
        elif ruffier_index >= 15.5:
            return HP_OKAY
        elif ruffier_index >= 10.5:
            return HP_MEDIUM
        elif ruffier_index >= 5:
            return HP_UPPERMEDIUM
        else:
            return HP_HIGH
    if user_age >= 7:
        if ruffier_index >= 21:
            return HP_LOW
        elif ruffier_index >= 17:
            return HP_OKAY
        elif ruffier_index >= 12:
            return HP_MEDIUM
        elif ruffier_index >= 6.5:
            return HP_UPPERMEDIUM
        else:
            return HP_HIGH