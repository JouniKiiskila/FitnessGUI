# TESTS FOR THE MODULE TIMETOOLS.PY

# Lets import module to by tested
import timetools

# UNIT TESTS DEFINATIONS

def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

def test_test_timediff():
    assert timetools.timediff('14:00:00', '11:00:00') == 1    


# # Let's test date difference
# date1 = '2023-03-21'
# date2 = '2023-03-17'

# ero = datediff2(date1, date2, 'day')
# print('ero oli', ero, 'päivää')

# # Let's test time difference
# time1 = '10:00:00'
# time2 = '15:25:00'
# ero = timediff2(time1, time2, 'minute')
# print('ero oli', ero, 'minuuttia')