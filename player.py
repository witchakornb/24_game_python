class Player:
    def __init__(self, name: str):
        self.name = name
        self.scores = []
        self.times = []

    def add_score(self, score: int):
        self.scores.append(score)

    def record_time(self, time_taken: float):
        self.times.append(time_taken)

    def get_total_score(self):
        return sum(self.scores)

    def get_scores(self):
        return self.scores

    def get_times(self):
        return self.times
