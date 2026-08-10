class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: if n is 0, x^0 is 1.
        if n == 0:
            return 1

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        final = 1
        current_product = x

        # Loop until n becomes 0
        while n > 0:
            # If n is odd, multiply final by the current_product
            if n % 2 == 1:
                final *= current_product
            
            # Square the current_product and halve n
            current_product *= current_product
            n //= 2
            
        return final

