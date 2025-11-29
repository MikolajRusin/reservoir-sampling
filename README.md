# 🌊 Reservoir Sampling Algorithm (Sampling from a Stream)

This project implements the **Reservoir Sampling**. This fundamental technique is especially usefule when we have to deal with streaming data whose total length may be unknown or too large to fit into memory. These disadavantages are mainly known from production, 
where data is collected continuously.

---

## 💡 Concept and Goal

In the context of Big Data and stream-based Machine Learning, standard sampling methods sucha as **Simple Random Sampling**, **Stratified Sampling** or **Weighted Sampling** where the data is collected only from past data can lead to **temporal bias** 
because the collected data may quickly becomes outdated. Another reason to consider **Reservoir Sampling** is that some methods, such as SRS (Simple Random Sampling) can lead to unbalanced or unrepresentative data.

Reservoir Sampling solves this by guaranteeing that after processing the elements, **every historical item** in the stream has an **identical probability** of being included in the final reservoir. 

Imagine you’re receiving a continuous stream of temperature readings from one weather station placed in a remote area.
You want to sample a certain number, k, of weather temperatures to do analysis or train a model on.
Since the station sends data at irregular intervals and you don’t know how many readings will arrive, you can’t pre-assign a probability to each reading in advance.

Yet you’d like to guarantee that:
- Every weather temperature has an equal probability of being selected.
- You can stop the algorithm at any time and the weather temperatures are sampled with the correct probability.

## 🛠️ Steps of the Alogirthm
As the name suggests the algorithm is based on **reservoir**, which can be an array, and consists of these steps:
1. Put the first ***k*** elements int to the reservoir.
2. For each incoming $i^{th}$ element, generate a random number ***j*** such that $\ 1 \le j \le i \$.
3. If $\ 1 \le j \le k \$ then replace the $j^{th}$ in the reservoir with the $i^{th}$ element. Else, do nothing.

---

## 💻 Implementation
To test the **Reservoir Sampling** algorithm, we simulated a continuous data stream that **does not load all data into memory at once**. This is achieved using a **Python Generator**.

### 1. `streaming_data_generator.py`
This file contains the generator function that produces elements one by one, simulating an external data source (like a sensor or log file).

```
def streaming_data_generator(n_stream: int):
    """
    Generates a sequence of integers from 0 up to (n_stream - 1), 
    simulating a data stream.
    """
    for i in range(n_stream):
        yield i
```

### 2. `reservoir_sampling.py`

This file contains the core logic of the Reservoir Sampling algorithm.

```
def reservoir_sampling(stream: Generator, k: int):
    # Define reservoir for our stored data
    reservoir = []

    # Fetching data from the simulated streaming data
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
```
