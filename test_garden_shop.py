import garden_shop

# TESTCASES
# ========================================== #

# a. test with even number of patches:
def test_a():
    assert garden_shop.get_days(1) == 10
    assert garden_shop.get_days(2) == 9
    assert garden_shop.get_days(4) == 8
    assert garden_shop.get_days(6) == 8
    assert garden_shop.get_days(8) == 7
    assert garden_shop.get_days(100) == 4
    assert garden_shop.get_days(512) == 1
    assert garden_shop.get_days(1000) == 1

# b. test with uneven number of patches:

'''
#3 Garden is covered by Patch #1, #2, and #3:

Patch #1: 
          1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8: 128, 9:256, 10:512
Patch #2: 
          1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8: 128, 9:256, 10:512
Patch #3: 
          1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8: 128, 9:256, 10:512

Garden is covered by day 9 (grass size is then > 512).

'''
def test_b():
    assert garden_shop.get_days(3) == 9
    assert garden_shop.get_days(5) == 8
    assert garden_shop.get_days(7) == 8
    assert garden_shop.get_days(9) == 7
    assert garden_shop.get_days(101) == 4
    assert garden_shop.get_days(511) == 2
    assert garden_shop.get_days(513) == 1
    assert garden_shop.get_days(1001) == 1