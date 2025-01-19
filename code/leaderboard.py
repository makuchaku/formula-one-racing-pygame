import json

class ScoreLeaderboard:
    def __init__(self):
        self.scores = {}
        self.filename = './code/leaderscores.txt'

    
    def save_score(self, name, score_player):
        # Read file
        file = open(self.filename, "rb")
        data = file.read()

        # If no data, initalize scores as empty dict, else load dict from file
        if len(data) == 0:
            self.scores = {}
        else:
            self.scores = json.loads(data)
            print(type(self.scores))
        file.close()

        # Save score to file
        self.scores[name] = score_player
        dict(sorted(self.scores.items(), key=lambda x: x[1], reverse=True))
        file = open(self.filename, "w")
        file.write(json.dumps(self.scores))
        file.close()

        return self.scores



# s = ScoreLeaderboard()
# s.save_score("mj", 100)