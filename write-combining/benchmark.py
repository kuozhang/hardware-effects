import os
import sys

import matplotlib.pyplot as plt
import seaborn


ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(ROOT)
from utils import benchmark


data = [
    ("Count", [16]),
    ("Increment", list(range(1, 16)))
]

frame = benchmark(data, pin_to_cpu=True, repeat=2)

seaborn.barplot(data=frame, x="Increment", y="Time", hue="Count")
plt.show()
