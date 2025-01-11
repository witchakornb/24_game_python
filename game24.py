from itertools import permutations, product
import numpy as np


class Game24:
    def __init__(self):
        self.generated_numbers = np.array([], dtype="int64")

    def generate_numbers(self) -> np.ndarray:
        """
        สุ่มตัวเลขใหม่ที่สามารถแก้ Game 24 ได้
        """
        while True:
            numbers = np.random.randint(1, 21, size=4)
            if self.can_solve_game24(numbers):
                self.generated_numbers = numbers
                return numbers

    def can_solve_game24(self, numbers) -> bool:
        """
        ตรวจสอบว่าชุดตัวเลขสามารถแก้ปัญหา Game 24 ได้หรือไม่
        """
        operators = ['+', '-', '*', '/']

        for num_perm in permutations(numbers):
            for ops in product(operators, repeat=3):
                expressions = [
                    f"(({num_perm[0]} {ops[0]} {num_perm[1]}) {ops[1]} {num_perm[2]}) {ops[2]} {num_perm[3]}",
                    f"({num_perm[0]} {ops[0]} ({num_perm[1]} {ops[1]} {num_perm[2]})) {ops[2]} {num_perm[3]}",
                    f"({num_perm[0]} {ops[0]} {num_perm[1]}) {ops[1]} ({num_perm[2]} {ops[2]} {num_perm[3]})",
                    f"{num_perm[0]} {ops[0]} (({num_perm[1]} {ops[1]} {num_perm[2]}) {ops[2]} {num_perm[3]})",
                    f"{num_perm[0]} {ops[0]} ({num_perm[1]} {ops[1]} ({num_perm[2]} {ops[2]} {num_perm[3]}))"
                ]

                for expr in expressions:
                    try:
                        if abs(eval(expr) - 24) < 1e-6:
                            return True
                    except ZeroDivisionError:
                        continue
        return False

    def solve(self, input_numbers: list, expression: str) -> int:
        """
        ตรวจสอบว่าสมการของผู้ใช้แก้ Game 24 ได้หรือไม่
        """
        if not set(input_numbers).issubset(self.generated_numbers):
            print("Error: Your numbers don't match the generated numbers.")
            return 0

        try:
            result = eval(expression)
            if abs(result - 24) < 1e-6:
                print("Correct! You scored 10 points.")
                return 10
            else:
                print(f"Incorrect! Your result is {result}, not 24.")
        except Exception as e:
            print(f"Invalid expression: {e}")
        return 0
