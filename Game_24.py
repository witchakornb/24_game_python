import numpy as np


class game:
    sum = str
    number = np.ndarray
    number_all = np.ndarray

    def __init__(self) -> None:
        self.sum = None
        self.number_all = None
        self.number = None

    def generateNumber(self) -> np.ndarray:
        self.number = np.random.randint(low=0, high=20, size=4)
        return self.number

    def convertNumber(self, list_of_number: list) -> None:
        self.number_all = list(map(int, list_of_number))

    def check(self) -> None:
        for obj in self.number:
            j = 0
            if obj in self.number_all:
                self.number = np.delete(self.number, j)
            else:
                return True

    def solve(self, user: list) -> int:
        self.sum = str(user)
        self.sum = self.sum.replace("'", "")
        self.sum = self.sum.replace(",", "")
        self.sum = self.sum.replace("[", "")
        self.sum = self.sum.replace("]", "")
        if eval(self.sum) == 24:
            return 10
        else:
            return 0
