# 1.	Low speed performance when calling higher integers which is mainly due to heavy push-pop of the stacked memory once the recursive function is being called. 
# Recursive function runs faster for smaller integers but once the nth number increases its performance tends to lag.


# 2

def isPowerOfTwo(n): 
	return (n and (not(n & (n - 1)))) 
def isProthNumber(n): 
	k = 1
	while(k < (n//k)): 	
		# check if k divides n or not 
		if(n % k == 0): 
	# Check if n / k is power of 2 or not 
			if(isPowerOfTwo(n//k)): 
					return True
		# update k to next odd number 
		k = k + 2	
	return False
n = 17
    # Check n for Proth Number 
if(isProthNumber(n-1)):
    print("A Prime number"); 
else: 
    print("Not a prime number"); 
