from streaming_data_generator import streaming_data_generator
from reservoir_sampling import reservoir_sampling
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def run_verification_test(N: int, k: int, T: int):
    all_samples = []
    for _ in range(T):
        stream_generator = streaming_data_generator(N)
        reservoir = reservoir_sampling(stream_generator, k)
        all_samples.append(reservoir)

    all_samples = np.array(all_samples)
    all_samples = all_samples.T
    results_df = pd.DataFrame(all_samples, columns=[f'stream_{i}' for i in range(T)])
    return results_df

# Define parameters
N_STREAM = 100
K_RESERVOIR = 10
T_RUNS = 100000

# Run the test
print(f'Start Test: {T_RUNS} runs...')
results = run_verification_test(N_STREAM, K_RESERVOIR, T_RUNS)
print('End Test.')

# Flatten and count the number of unique values
all_samples_flat = results.values.flatten()
unique, counts = np.unique(all_samples_flat, return_counts=True)

# Turn unique and count values into DataFrame
analysis_df = pd.DataFrame(counts, index=unique, columns=['number_of_appears'])
analysis_df.index.name = 'unique_value'

# Theoretical and Experimental Analysis
theoretical_probability = K_RESERVOIR / N_STREAM
theoretical_number_of_appears = T_RUNS * K_RESERVOIR / N_STREAM

print('--- Theoretical and Experimental Analysis ---')
print(f'Theoretical Probability: {theoretical_probability} ({theoretical_probability*100:.2f}%)')
print(f'Theoretical Number of Appears: {theoretical_number_of_appears}')
print(f'Experimental Average Number of Appears: {analysis_df['number_of_appears'].mean():.2f}')
print(f'Experimental Standard Deviation of Appears: {analysis_df['number_of_appears'].std():.2f}')

# Empirical probability that a particular number will occur in a set
emp_probability = analysis_df['number_of_appears'] / T_RUNS

plt.figure(figsize=(15, 10))
plt.bar(analysis_df.index, emp_probability)
plt.axhline(theoretical_probability, color='r', linestyle='--', label='Theoretical Probability')
plt.ylabel('Probability of Appears')
plt.xlabel('Stream Element')
plt.legend(loc='upper right')
plt.grid()
plt.show()