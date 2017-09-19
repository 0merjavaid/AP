import unittest
from is_prime import is_prime
from is_prime import is_prime_correct

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
	
        self.assertTrue(is_prime(5),msg="5 is prime")


    
    
    def test_non_primes(self):
	"Checking a list of non primes"
	non_primes=[4,6,8,9]
	for i in non_primes:
		self.assertTrue(is_prime_correct(5),msg="5 is prime")
		self.assertFalse(is_prime_correct(i))



    def test_negative_prime(self):
        """Is negative successfully determined to be prime?"""
	
	self.assertFalse(is_prime_correct(-1),msg="-1 is not prime")

if __name__ == '__main__':
    unittest.main()
