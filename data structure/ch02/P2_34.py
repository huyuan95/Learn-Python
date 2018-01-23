import matplotlib.pyplot as plt
import numpy as np

ch_dict = {}
with open('RomeoandJuliet.txt', 'r') as f:
    text = f.read()
    for ch in text:
        if ch.isalpha() == True:
            if ch.lower() in ch_dict:
                ch_dict[ch.lower()] += 1
            else:
                ch_dict[ch.lower()] = 1


ind = np.arange(26)
p1 = plt.bar(ind, ch_dict.values(), 1)
plt.xticks(ind, ch_dict.keys())
plt.show()
        
