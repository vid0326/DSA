# 1st non negative character in the stream of the chracter 
# ababcd o/p=> aab#cc


from collections import deque

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # Frequency array for characters 'a' to 'z'
        arr = [0] * 26
        # Queue to maintain the order of characters
        q = deque()
        # Resultant string
        result = []

        for char in A:
            # Update frequency
            arr[ord(char) - ord('a')] += 1
            # Add character to the queue
            q.append(char)

            # Remove characters from the queue if they are not non-repeating
            while q and arr[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            # Add the first non-repeating character to the result
            if q:
                result.append(q[0])
            else:
                result.append('#')  # No non-repeating character

        # Convert the result list to a string
        return ''.join(result)
