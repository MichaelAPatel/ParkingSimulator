import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(0)


def sim():
    old_garage = []
    new_garage = []
    for i in range(0, 200):
        # If the new garage is not full then there is an equal chance that the person will choose the new or old garage.
        if len(new_garage) < 100:
            choice = np.random.choice(2)
            if choice == 0:
                new_garage.append(i)
            else:
                old_garage.append(i)
        # If the new garage is full then the person is forced to choose the old garage.
        else:
            old_garage.append(i)
    # Return the amount of money collected for this simulation based on the number of cars in each garage.
    return len(old_garage) + len(new_garage) * 10


# Run the simulation 100,000 times to get meaningful statistics.
results = []
for j in range(0, 100000):
    results.append(sim())

# Print the mean, median, and mode values.
print 'The mean value collected is $' + str(np.mean(results)) + '.'
print 'The median value collected is $' + str(np.median(results)) + '.'
print 'The mode value collected is $' + str(stats.mode(results)[0]).strip('[').strip(']') + '.'

# Plot a histogram of the amount collected vs the number of times you collect that money.
(counts, bins) = np.histogram(results, bins=range(900, 1101))
factor = 1. / 100000.
plt.hist(bins[:-1], bins, weights=factor*counts)
plt.xlabel('Dollars Collected ($)')
plt.ylabel('Probability of Collecting X Dollars')
plt.show()
