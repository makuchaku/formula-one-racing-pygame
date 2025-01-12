# pickling.py
import pickle

class ScoreLeaderboard:
    def __init__(self):
        self.scores = {}
        self.filename = './code/leaderscores.txt'

    
    def save_score(self, name, score_player):
        with open(self.filename, 'rb') as pickle_file:
            self.scores = pickle.load(pickle_file)
        # with open(self.filename, 'r') as reader:
            # Read and print the entire file line by line
            # data = reader.read()
            # print(data)
            # self.scores = pickle.load(data)
            if self.scores == None:
                self.scores = {}
            self.scores[name] = score_player
            print(self.scores)
        
        # dumped_score = pickle.dump(self.scores)
        # with open(self.filename, 'w') as writer:
        #     writer.write(dumped_score)