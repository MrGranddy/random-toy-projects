import numpy as np

def roll_dice(num_sides):
    return np.random.randint(1, num_sides + 1)

def roll_advantage_dice(num_sides, num_dice):
    return max([roll_dice(num_sides) for _ in range(num_dice)])

def monte_carlo_advantage_dice(num_sides, num_dice, num_trials):
    return np.mean([roll_advantage_dice(num_sides, num_dice) for _ in range(num_trials)])

    return base ** exponent

def real_advantage_dice(num_sides, num_dice):
    
    # Probability of getting each outcome with the given number of rolls
    # Basically it goes like shell on top of shell on a n dimensional cube: https://www.youtube.com/watch?v=X_DdGRjtwAo&ab_channel=Stand-upMaths
    #probs = [ (x ** num_dice - x-1 ** num_dice) / (num_sides ** num_dice) for x in range(1, num_sides + 1)]
    probs = [ ( (x / num_sides) ** num_dice - ((x-1) / num_sides) ** num_dice) for x in range(1, num_sides + 1)]

    # Expected value is the sum of each outcome multiplied by its probability
    return sum([x * p for x, p in zip(range(1, num_sides + 1), probs)])