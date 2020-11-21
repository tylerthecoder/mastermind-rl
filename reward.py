
color_correct_reward = 1
pos_correct_reward = 3
guess_penalty = 0.5

class Reward:

    def compute(self, game_state):
        if len(game_state) == 0:
            return 0

        last_result = game_state[-1][1]
        return self.compute_one(last_result[0], last_result[1])

        # reward = 0
        # for guess, result in game_state:
        #     reward +=


    def compute_one(self, pos_correct, color_correct):
        return color_correct * color_correct_reward + pos_correct * pos_correct_reward - guess_penalty