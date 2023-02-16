import matplotlib.pyplot as plt
from datetime import datetime
from Game_24 import game
from User import user


def welcome():
    print("""
    Welcome to 24 Game
    \n\n
    Example
    15 2 8 7
    (15 + (2 * 8)) - 7
    or
    8 / ((7 - 2) / 15)
    \n\n
    Example in case of error
    8 + (7-2) - 7 // error
    6*4+1-1 // error
    """)


def remove(x: str) -> str:
    x = x.replace("(", "")
    x = x.replace(")", "")
    return x


def Main() -> None:
    player = user("james")
    play = game()
    count = 0
    welcome()
    while True:
        print("Are you ready? (Y or N)")
        uin = input("Enter your choice: ")
        uin = uin.upper()
        if uin == "Y" or uin == "YES":
            break

    while count <= 10:
        print(f"Value = {play.generateNumber()}")
        print()
        time_start = datetime.now()
        user_number = input("Enter :").split()
        time_end = datetime.now()
        time = time_end - time_start
        try:
            num1, op1, num2, op2, num3, op3, num4 = user_number
            list_of_number = list(map(remove, [num1, num2, num3, num4]))
            play.convertNumber(list_of_number)
            if play.check():
                print("invalid please check input")
                continue
            else:
                player.add_score(play.solve(user_number))
                player.set_time(time.seconds)
                print(f"Your score is {player.get_sum_score()}")
                print(f"Time to ues {player.get_time()} ")
                count += 1
        except:
            print("something went wrong")

    plt.plot(player.get_score(), label="Score")
    plt.plot(player.get_time(), label="Time")
    plt.legend()
    plt.show()
    # for i in range(2):
    #     print(g.generateNumber())
    #     time_start = datetime.now()
    #     user_number = input("Enter :").split()
    #     time_end = datetime.now()
    #     time = time_end - time_start
    #     num1, op1, num2, op2, num3, op3, num4 = user_number
    #     list_of_number = list(map(remove, [num1, num2, num3, num4]))
    #     g.convertNumber(list_of_number)
    #     if g.check():
    #         print("invalid please check input")
    #     else:
    #         player.add_score(g.solve(user_number))
    #         player.set_time(time.seconds)
    #         print(f"Time to use {time.seconds} seconds")
    #         print(f"your score is {player.get_sum_score()}")
    # plt.plot(player.get_score(), label="Score")
    # plt.plot(player.get_time(), label="Time")
    # plt.legend()
    # plt.show()


Main()
