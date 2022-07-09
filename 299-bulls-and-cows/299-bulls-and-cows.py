from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        
        unpaired = defaultdict(int)
        # Count bulls
        for i, char in enumerate(secret):
            if guess[i] == char:
                bulls += 1
            else:
                unpaired[char] += 1
        
        # Count cows
        for i, char in enumerate(guess):
            if secret[i] == char:
                pass
            elif unpaired[char] > 0:
                unpaired[char] -= 1
                cows += 1
        
        
        return f'{bulls}A{cows}B'