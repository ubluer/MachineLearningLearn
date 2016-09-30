import random


def lottery():
    reds = list(range(1, 34))
    blue = list(range(1, 17))
    selected_reds = random.sample(reds, 6)
    selected_reds.sort()
    selected_blue = random.sample(blue, 1)
    print(selected_reds, selected_blue)
    return selected_reds, selected_blue


def select_lotteries(n):
    for i in range(n):
        lottery()


select_lotteries(10)
