
"""
    Top 100: Math_22, Math_30
    Top 1000: Closure_13
"""

CHART_SIZE=26
CLOSURE_SIZE=133
LANG_SIZE=65
MATH_SIZE=106
MOCKITO_SIZE=38
TIME_SIZE=27

CHART_CORRECT=(1,4,11,19,19002) # 24: sub
CLOSURE_CORRECT=(10,38,62,63,73)
LANG_CORRECT=(57,59)
MATH_CORRECT=(22,22002,30,34,35,35002,57,70,75,79,82) # 85: infinite test for buggy, 33: too large iter
MOCKITO_CORRECT=(29,38)
# TIME_CORRECT=(19,) # 19: too large iter

MOCKITO_SKIP=(9,10,11,21)

CHART_PLAUSIBLE=(12,13,14,15,17,25,3,7)
CLOSURE_PLAUSIBLE=(129,19)
LANG_PLAUSIBLE=(63,)
MATH_PLAUSIBLE=(20,33,50,63,84) # 50, 63: need check, 80, 81: infinite test
TIME_PLAUSIBLE=(11,19) # 11: need check