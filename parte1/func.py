import math

def es_primo(num) -> bool:
    """Check if a number is prime."""
    # Check if the input is None or not a number
    if num is None or not isinstance(num, (int, float)):
        return False

    # Attempt to convert the input to a float
    try:
        num = float(num)
    except ValueError:
        return False

    # Define a tolerance for floating-point comparison
    tolerance = 1e-9

    # Check if the number is close to an integer
    if not (abs(num - round(num)) < tolerance):
        return False
    
    # Convert float to integer
    num = int(round(num))
    
    # Handle edge cases
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check for factors from 3 to sqrt(num)
    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(es_primo(5))
