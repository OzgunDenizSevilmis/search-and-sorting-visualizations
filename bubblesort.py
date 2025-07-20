import matplotlib.pyplot as plt
import random

def bubble_sort_visualized(data):
    n = len(data)
    plt.ion()  # Enable interactive mode for real-time plotting

    # Visualize initial unsorted array
    plt.bar(range(len(data)), data, color="blue")
    plt.title("Unsorted Array")
    plt.pause(1)

    # Perform Bubble Sort and visualize each step
    for i in range(n):
        for j in range(0, n-i-1):
            # Visualize the array before swapping
            plt.bar(range(len(data)), data, color="blue")
            plt.bar(j, data[j], color="yellow")  # Highlight the current pair being compared
            plt.bar(j+1, data[j+1], color="yellow")
            plt.title(f"Comparing index {j} and {j+1}")
            plt.pause(0.5)

            # Swap if the current element is greater than the next
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

        # Visualize the array after each pass
        plt.bar(range(len(data)), data, color="blue")
        plt.title(f"After pass {i+1}")
        plt.pause(0.5)

    # Visualize sorted array
    plt.bar(range(len(data)), data, color="green")
    plt.title("Sorted Array")
    plt.pause(1)
    plt.ioff()  # Turn off interactive mode
    plt.show()

    print("Sorted Array:", data)

# Generate random data
data = random.sample(range(1, 100), 10)  # Random list of 10 numbers from 1 to 100

# Run the Bubble Sort visualization
bubble_sort_visualized(data)



