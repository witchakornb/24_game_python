import time
import re
import matplotlib
matplotlib.use("Agg")  # ใช้ Agg backend
import matplotlib.pyplot as plt
from game24 import Game24
from player import Player


def main():
    game = Game24()
    player = Player(input("Enter your name: ").strip())

    print("\nWelcome to Game 24!")
    print("Solve mathematical expressions to make 24 using the provided numbers.")
    print("You can use +, -, *, /, and parentheses.")

    rounds = 5
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num} of {rounds}")
        numbers = game.generate_numbers()
        print(f"Numbers: {numbers}")

        start_time = time.time()
        user_input = input("Enter your solution (e.g., '(8 + 2) * (3 + 1)'): ").strip()
        user_numbers = list(map(int, re.findall(r'\d+', user_input)))
        end_time = time.time()

        time_taken = end_time - start_time
        score = game.solve(user_numbers, user_input)
        player.add_score(score)
        player.record_time(time_taken)

    print("\nGame Over!")
    print(f"Total Score: {player.get_total_score()}")
    print("Round-by-round scores:", player.get_scores())
    print("Time taken per round (seconds):", player.get_times())

    # Save results as a graph
    plt.plot(range(1, rounds + 1), player.get_scores(), marker='o', label="Scores")
    plt.plot(range(1, rounds + 1), player.get_times(), marker='x', label="Time (s)")
    plt.xlabel("Round")
    plt.ylabel("Value")
    plt.title(f"Performance of {player.name}")
    plt.legend()
    plt.grid()
    plt.savefig("performance.png")  # บันทึกกราฟเป็นไฟล์
    print("\nGraph saved as 'performance.png'")


if __name__ == "__main__":
    main()
