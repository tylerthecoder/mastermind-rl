import random
from collections import Counter

colors = ['r', 'g', 'b', 'o', 'k', 'w']

class Game:
  def __init__(self, n=10, c=6, s=4):
    super().__init__()
    self.n = n
    self.c = c
    self.s = s

    self.game_state = []

    # generate a random code
    self.code = []
    for i in range(s):
      self.code.append(random.randint(0, c -1))

    self.codeCount = Counter(self.code)


  def print(self):
    print("This is the Game")
    print("It has been", len(self.game_state), "turns")
    print("Code: ", self.code)
    for guess, result in self.game_state:
      print("Guess", guess, "Result:", result)

  def is_over(self):
    return len(self.game_state) > self.n

  def getState(self):
    return self.game_state

  # Input: array of colors (int) that was guessed
  # Output: Amount of things that were correct ( colors: number, position: number )
  def guess(self, guess):
    # see how close they were
    # first calculate what they had in the right place
    rightPosition = 0
    rightColor = 0

    for g, c in zip(guess, self.code):
      if g == c:
        rightPosition += 1

    guessCount = Counter(guess)

    for key, value in guessCount.items():
      rightColor += value if self.codeCount[key] >= value else self.codeCount[key]

    # don't want to double count colors
    rightColor -= rightPosition

    result = ( rightPosition, rightColor )

    self.game_state.append((guess, result))

    return result
