from random import randint


class Agent:
    def __init__(self, game_length, num_colors, guess_length):
        self.game_length = game_length
        self.num_colors = num_colors
        self.guess_length = guess_length
        self.reward = 0

    def __str__(self):
        return f'agent reward is {self.reward}'

    def guess(self, game_state, reward):
        raise NotImplementedError

class RandomAgent(Agent):

    def guess(self, game_state, reward):
        """ returns a self.guess_length list of integers between [0, self.num_colors] """
        self.reward += reward

        return [ randint(0, self.num_colors) for x in range(self.guess_length) ]

class AgentV1(Agent):
    def __init__(self, game_length, num_colors, guess_length):
        super().__init__(game_length, num_colors, guess_length)
        """ num_colors x guess_length array where memory[i][j] is the probability that
            color i in position j is correct
        """
        self.memory =  [ [0] * guess_length for x in range(num_colors) ]

    def guess(self, game_state, reward):
        """ returns a self.guess_length list of integers between [0, self.num_colors] """

        # This is our first guess so just guess randomly
        if len(game_state) == 0:
            return [ randint(0, self.num_colors) for x in range(self.guess_length) ]
        else:
            last_guess = game_state[-1][0]
            for i, color in enumerate(last_guess):
                self.memory[color][i] += reward

            return self.get_next_guess(game_state)
            # return [ randint(0, self.num_colors) for x in range(self.guess_length) ]


    def get_next_guess(self, game_state):
        """ use self.memory to find the most probable guess.
            Don't repeat guesses from game_state
            be more random at the beginning but less at end
        """
        pass