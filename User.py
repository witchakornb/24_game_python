import numpy as np


class user:
    _name: str
    _score: np.ndarray
    _time: np.ndarray

    def __init__(self, name: str) -> None:
        self._name = name
        self._score = np.array([], dtype="int64")
        self._time = np.array([], dtype="float64")

    def add_score(self, score: int) -> None:
        self._score = np.append(self._score, score)

    def get_sum_score(self) -> np.ndarray:
        return sum(self._score)

    def get_score(self) -> np.ndarray:
        return self._score

    def set_time(self, time: float) -> None:
        self._time = np.append(self._time, time)

    def get_time(self) -> np.ndarray:
        return self._time
