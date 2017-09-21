def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(number):
        if number % element == 0: 
            return False

    return True


































def is_prime_correct(number):
    """Return True if *number* is prime."""
    if(number<=1):
	return False
    for element in range(2,number):  #Error corrected by changing range from 0-n to 2-n
        if number % element == 0: 
            return False

    return True
