from streaming_data_generator import streaming_data_generator
from reservoir_sampling import reservoir_sampling

stream_generator = streaming_data_generator(100)
reserovir = reservoir_sampling(stream=stream_generator, k=10)
print(reserovir)