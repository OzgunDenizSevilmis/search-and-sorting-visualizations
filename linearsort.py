import matplotlib.pyplot as plt
import random

def linear_search_visualized(data, target):
    plt.ion()  # Enable interactive mode

    for i in range(len(data)):
        # Visualize the current search step
        plt.bar(range(len(data)), data, color="blue")
        plt.bar(i, data[i], color="yellow")
        plt.title(f"Searching for {target} | Checking index {i}")
        plt.pause(0.5)

        if data[i] == target:
            plt.bar(i, data[i], color="green")
            plt.title(f"Found {target} at index {i}")
            plt.pause(2)
            plt.ioff()  # Turn off interactive mode
            plt.show()

            print("Original List:", data)
            print(f"Target {target} found at index {i}")
            return i

        plt.clf()  # Clear the figure for the next step

    # If target is not found
    plt.bar(range(len(data)), data, color="red")
    plt.title(f"{target} not found in the list")
    plt.pause(2)
    plt.ioff()  # Turn off interactive mode
    plt.show()

    print("Original List:", data)
    print(f"Target {target} not found in the list")
    return -1

# Generate random data
data = random.sample(range(1, 100), 10)  # Random list of 10 numbers from 1 to 100
target = random.choice(data + [random.randint(101, 200)])  # Randomly select a target (might not exist in the list)

# Run the visualization
linear_search_visualized(data, target)
