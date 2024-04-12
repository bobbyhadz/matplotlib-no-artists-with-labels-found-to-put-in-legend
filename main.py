# Matplotlib: No artists with labels found to put in legend

import pandas as pd
import matplotlib.pyplot as plt

test_data = pd.DataFrame.from_dict({
    'x': {0: 9.49084, 1: 14.47866, 2: 5.06412, 3: 11.27358, 4: 5.33439},
    'y': {0: 1.35503, 1: 9.01758, 2: 7.36345, 3: 7.36519, 4: 6.73471}
})

fig = plt.figure()
ax = fig.add_subplot(221)

data = plt.scatter(test_data.x, test_data.y)


ax.legend([data], ['dots'])

plt.show()