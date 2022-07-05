class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.fizz(i) for i in range(1, n + 1)]
    
    def fizz(self, n) -> str:
        if n % 15 == 0:
            return "FizzBuzz"
        elif n % 5 == 0:
            return "Buzz"
        elif n % 3 == 0:
            return "Fizz"
        return str(n)