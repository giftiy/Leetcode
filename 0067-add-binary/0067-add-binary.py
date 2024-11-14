class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  # To store the result
        carry = 0  # Initialize carry to 0
        
        # Pointers for a and b
        i, j = len(a) - 1, len(b) - 1
        
        # Loop until both strings are fully processed or there is a carry left
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (0 if out of bounds)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of the digits and the carry
            total = digit_a + digit_b + carry
            result.append(str(total % 2))  # Append the binary result (0 or 1)
            carry = total // 2  # Update carry (0 or 1)
            
            # Move to the next left digit
            i -= 1
            j -= 1
        
        # The result list is in reverse order, so we need to reverse it
        return ''.join(result[::-1])
