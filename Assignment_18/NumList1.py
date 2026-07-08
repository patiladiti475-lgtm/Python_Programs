# ---------------------------------------------------------
# File Name : NumList1.py
# Description:
# Contains utility function for prime number checking.
# ---------------------------------------------------------

def ChkPrime(number):
    
    if number <= 1:
        return False
    
    for value in range(2,number):
        if number % value == 0:
            return False
    
    return True
