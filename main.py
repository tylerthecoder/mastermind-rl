from game import Game
from agent import Agent
from reward import Reward

game_length = 10
num_colors = 6
guess_length = 4

game = Game(game_length, num_colors, guess_length)
agent = Agent(game_length, num_colors, guess_length)
reward = Reward()

while not game.is_over():

    game.print()

    game_state = game.getState()

    agent_guess = agent.guess(game_state, reward.compute(game_state))
    print(agent)

    game.guess(agent_guess)

