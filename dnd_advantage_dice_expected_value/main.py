import numpy as np
import matplotlib.pyplot as plt

from dicer import real_advantage_dice

if __name__ == "__main__":

    # Graph of number of dice vs expected value
    num_sides = 20
    num_dices = np.arange(1, 25)
    expected_values = [real_advantage_dice(num_sides, num_dice) for num_dice in num_dices]

    print(expected_values)

    plt.plot(num_dices, expected_values)
    plt.xlabel("Number of dice")
    plt.ylabel("Expected value")
    plt.show()