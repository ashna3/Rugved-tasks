# Function to generate Fibonacci Sequence

def fibonacci_sequence(n):
    # Initialize the first two values of the sequence
    fib_sequence = [0, 1]

    # Generate the sequence until it reaches n values
    while len(fib_sequence) < n:
        # Append the sum of the last two values in the sequence
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    return fib_sequence

# Main program
if __name__ == "__main__":
    # Get the number of values from the user
    n = int(input("Enter the number of Fibonacci sequence values to generate: "))

    # Check if the input is a positive integer
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # Generate and print the Fibonacci Sequence
        sequence = fibonacci_sequence(n)
        print(f"Fibonacci Sequence up to {n} values: {sequence}")

