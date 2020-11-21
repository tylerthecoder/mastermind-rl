This is a RL version of master mind

n = 10  # number of attempts
c = 6   # colors
s = 4   # locations
r = 1   # amount of times you can repeat a color in the code

Rewards:
- Correct color: 1 pt
- Correct color and position Position: 2pt
- Correct code: 10pt
- Each attempt: -0.5 points
- Incorrect code in n attempts: -7 points

