import timeit
from typing import List

def generate_fibonacci(n: int):
    if not isinstance(n, int):
        raise TypeError("Sequence upper bound must be an integer.")
    if n < 0:
        raise ValueError("Sequence upper bound cannot be negative.")
    
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    # for _ in range(2, n):
    #     sequence.append(sequence[-1] + sequence[-2])
        
    return sequence

def benchmark_fibonacci(n: int, iterations: int = 10000) -> float:
    setup_code = "from __main__ import generate_fibonacci"
    statement = f"generate_fibonacci({n})"
    
    total_time = timeit.timeit(statement, setup=setup_code, number=iterations)
    return total_time

if __name__ == "__main__":
    target_terms = int(input("Enter length: "))
    
    try:
        result = generate_fibonacci(target_terms)
        print(f"Generated Sequence ({target_terms} terms): {result}")
        
        elapsed_time = benchmark_fibonacci(target_terms, iterations=5000)
        print(f"Benchmark Runtime: {elapsed_time:.6f} seconds (5,000 iterations for n={target_terms})")
        
    except (ValueError, TypeError) as e:
        print(f"Parameter Validation Error: {e}")
