def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(number):
        if number % element == 0: # divide by zero error
            return False

    return True

def is_prime_correct(number):
    """Return True if *number* is prime."""
    if(number<=1):
	return False
    for element in range(2,number):
        if number % element == 0: # divide by zero error
            return False

    return True
