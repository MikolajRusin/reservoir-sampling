def streaming_data_generator(n_stream: int) -> int:
    """
    Generates a sequence of integers from 0 up to (n_stream - 1), 
    simulating a data stream.
    """
    for i in range(n_stream):
        yield i