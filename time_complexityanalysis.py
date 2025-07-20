import random
import time
import matplotlib.pyplot as plt

# Linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate random list with n elements
def generate_random_list(n):
    return [random.randint(1, 10000) for _ in range(n)]

# Measure the time taken for Linear Search
def measure_linear_search_time(n, target):
    arr = generate_random_list(n)  # Create a random list
    start_time = time.perf_counter()  # Start time measurement
    linear_search(arr, target)  # Perform linear search
    end_time = time.perf_counter()  # End time measurement
    return end_time - start_time  # Return the time taken

# Measure the time taken for Bubble Sort
def measure_bubble_sort_time(n):
    arr = generate_random_list(n)  # Create a random list
    start_time = time.perf_counter()  # Start time measurement
    bubble_sort(arr)  # Perform bubble sort
    end_time = time.perf_counter()  # End time measurement
    return end_time - start_time  # Return the time taken

# Collect data for plotting (for different sizes of the list)
sizes = []
linear_times = []
bubble_times = []

# Testing for sizes from 100 to 1000 with step 100
for n in range(100, 1001, 100):
    target = random.randint(1, 10000)  # Random target value for Linear Search
    linear_time = measure_linear_search_time(n, target)  # Measure Linear Search time
    bubble_time = measure_bubble_sort_time(n)  # Measure Bubble Sort time
    sizes.append(n)
    linear_times.append(linear_time)
    bubble_times.append(bubble_time)

# Now create a more appropriate comparison graph

plt.figure(figsize=(10, 6))

# Plot both Linear Search and Bubble Sort on the same graph
plt.plot(sizes, linear_times, label="Linear Search Time", color='blue', marker='o')
plt.plot(sizes, bubble_times, label="Bubble Sort Time", color='red', marker='x')

# Labeling the axes and the title
plt.xlabel('Size of List')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Linear Search and Bubble Sort Time Complexity')

# Adding grid, legend, and display the graph
plt.grid(True)
plt.legend()
plt.yscale('log')  # Use a logarithmic scale to make small differences more visible
plt.show()