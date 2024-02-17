# FIBONACCI GENERATOR
#
# The Fibonacci series is a sequence where each number is
# the sum of the two preceding numbers, defined by a
# mathematical recurrence relationship.
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


# Example: Generate the first 10 Fibonacci numbers
if __name__ == '__main__':
    result = generate_fibonacci(10)
    print(result)


