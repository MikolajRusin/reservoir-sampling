import random
from typing import Generator

def reservoir_sampling(stream: Generator, k: int):
    # Define reservoir for our stored data
    reservoir = []
    # Fetchingdata from the simulated streaming data
    for i, x in enumerate(stream, start=1):
        # First, fill the reservoir
        if i <= k:
            reservoir.append(x)
        # Random replacement ith element with probability k/i
        else:
            j = random.randint(1, i)
            if j <= k:
                reservoir[j - 1] = x
    
    return reservoir