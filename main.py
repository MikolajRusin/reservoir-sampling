from streaming_data_generator import streaming_data_generator
from reservoir_sampling import reservoir_sampling

# Define parameters
N_STREAM = 100    # Total size of the simulated stream
K_RESERVOIR = 10  # Desired size of the final sample

# Initialize the stream generator
streaming_generator = streaming_data_generator(N_STREAM)
# Run the Reservoir Sampling algorithm
reservoir = reservoir_sampling(stream=streaming_generator, k=K_RESERVOIR)
print(reservoir)