#!/usr/bin/env python3
"""
Magic Number Generator
A fun program that generates a "magic number" based on your input
and explains the mathematical reasoning behind it.
"""
import math
import random


class MagicNumberGenerator:
    def __init__(self):
        self.magic_algorithms = [
            self._fibonacci_magic,
            self._prime_magic,
            self._digital_root_magic,
            self._golden_ratio_magic,
            self._collatz_magic,
            self._factorial_magic,
            self._perfect_square_magic,
            self._sum_of_digits_magic,
        ]

    def generate_magic_number(self, input_number):
        """Generate a magic number and explanation based on input"""
        try:
            num = int(input_number)

            # Choose algorithm based on input characteristics
            algorithm = self._choose_algorithm(num)
            magic_number, explanation = algorithm(num)

            return {
                "input": num,
                "magic_number": magic_number,
                "explanation": explanation,
                "algorithm_used": algorithm.__name__.replace("_", " ").title(),
            }
        except ValueError:
            return {
                "error": "Please enter a valid number",
                "magic_number": 42,
                "explanation": "Since you didn't provide a valid number, here's the ultimate answer to everything!",
            }

    def _choose_algorithm(self, num):
        """Choose which algorithm to use based on number characteristics"""
        abs_num = abs(num)

        if abs_num == 0:
            return self._digital_root_magic
        elif abs_num <= 10:
            return self._fibonacci_magic
        elif self._is_prime(abs_num):
            return self._prime_magic
        elif abs_num % 10 == 0:
            return self._factorial_magic
        elif abs_num > 100:
            return self._digital_root_magic
        elif abs_num % 2 == 0:
            return self._collatz_magic
        else:
            return random.choice(self.magic_algorithms)

    def _fibonacci_magic(self, num):
        """Generate magic number using Fibonacci sequence"""
        abs_num = abs(num)
        fib_sequence = [0, 1]

        while len(fib_sequence) <= abs_num + 5:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        if abs_num < len(fib_sequence):
            magic_number = fib_sequence[abs_num]
        else:
            magic_number = fib_sequence[abs_num % len(fib_sequence)]

        explanation = f"I used the Fibonacci sequence! Your number {num} corresponds to the {abs_num}th Fibonacci number: {magic_number}. The Fibonacci sequence starts with 0, 1 and each subsequent number is the sum of the two preceding ones."

        return magic_number, explanation

    def _prime_magic(self, num):
        """Generate magic number using prime number properties"""
        abs_num = abs(num)

        if self._is_prime(abs_num):
            # Find the next prime
            next_prime = self._next_prime(abs_num + 1)
            magic_number = next_prime
            explanation = f"Your number {num} is prime! The magic number is the next prime after it: {magic_number}. Prime numbers are special because they're only divisible by 1 and themselves."
        else:
            # Find nearest prime
            nearest_prime = self._nearest_prime(abs_num)
            magic_number = nearest_prime
            explanation = f"Your number {num} isn't prime, so I found the nearest prime number: {magic_number}. This creates a mystical connection to the fundamental building blocks of mathematics!"

        return magic_number, explanation

    def _digital_root_magic(self, num):
        """Generate magic number using digital root calculation"""
        abs_num = abs(num)
        digital_root = self._calculate_digital_root(abs_num)

        # Create magic number by multiplying digital root with a pattern
        magic_number = digital_root * 111 + digital_root

        explanation = f"I calculated the digital root of {num}! Keep adding the digits until you get a single digit: {digital_root}. Then I multiplied it by 111 and added itself to get the magic number {magic_number}. Digital roots reveal the hidden essence of numbers!"

        return magic_number, explanation

    def _golden_ratio_magic(self, num):
        """Generate magic number using golden ratio"""
        abs_num = abs(num)
        golden_ratio = (1 + math.sqrt(5)) / 2

        magic_number = int(abs_num * golden_ratio)

        explanation = f"I multiplied your number {num} by the golden ratio (φ ≈ 1.618)! This divine proportion appears throughout nature - in flower petals, spiral shells, and even the human body. Your magic number {magic_number} now carries this natural harmony!"

        return magic_number, explanation

    def _collatz_magic(self, num):
        """Generate magic number using Collatz conjecture steps"""
        abs_num = abs(num) if abs(num) > 0 else 1
        steps = 0
        current = abs_num

        # Calculate Collatz sequence steps
        while current != 1 and steps < 100:  # Limit steps to prevent infinite loops
            if current % 2 == 0:
                current = current // 2
            else:
                current = 3 * current + 1
            steps += 1

        magic_number = steps * 7 + abs_num % 10  # Add some magic multiplier

        explanation = f"I used the mysterious Collatz conjecture! Starting with {abs_num}, it took {steps} steps to reach 1 by following the rule: if even, divide by 2; if odd, multiply by 3 and add 1. Your magic number {magic_number} represents this mathematical journey!"

        return magic_number, explanation

    def _factorial_magic(self, num):
        """Generate magic number using factorial properties"""
        abs_num = abs(num)

        # Use a smaller number for factorial to avoid huge numbers
        factorial_base = min(abs_num % 10 + 1, 7)
        factorial_result = math.factorial(factorial_base)

        magic_number = factorial_result + abs_num

        explanation = f"I calculated the factorial of {factorial_base} (derived from your number {num}) which equals {factorial_result}! Then added your original number to get {magic_number}. Factorials represent the number of ways to arrange things - pure mathematical magic!"

        return magic_number, explanation

    def _perfect_square_magic(self, num):
        """Generate magic number using perfect squares"""
        abs_num = abs(num)

        # Find the nearest perfect square
        sqrt_num = int(math.sqrt(abs_num))
        lower_square = sqrt_num**2
        upper_square = (sqrt_num + 1) ** 2

        if abs(abs_num - lower_square) <= abs(abs_num - upper_square):
            nearest_square = lower_square
            root = sqrt_num
        else:
            nearest_square = upper_square
            root = sqrt_num + 1

        magic_number = nearest_square + root

        explanation = f"I found the nearest perfect square to {num}, which is {nearest_square} (√{nearest_square} = {root}). Added the square root to get your magic number {magic_number}. Perfect squares represent completeness and harmony in mathematics!"

        return magic_number, explanation

    def _sum_of_digits_magic(self, num):
        """Generate magic number using sum of digits"""
        abs_num = abs(num)
        digit_sum = sum(int(digit) for digit in str(abs_num))

        # Create magic pattern
        magic_number = digit_sum**2 + digit_sum * 3

        explanation = f"I added all the digits in {num} to get {digit_sum}, then squared it and added triple the sum to create {magic_number}. The sum of digits reveals the numerical DNA of your number!"

        return magic_number, explanation

    # Helper methods
    def _is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def _next_prime(self, n):
        """Find the next prime number after n"""
        while not self._is_prime(n):
            n += 1
        return n

    def _nearest_prime(self, n):
        """Find the nearest prime number to n"""
        if n <= 2:
            return 2

        lower = n - 1
        upper = n + 1

        while lower > 1 or upper < n + 100:
            if lower > 1 and self._is_prime(lower):
                return lower
            if self._is_prime(upper):
                return upper
            lower -= 1
            upper += 1

        return 2  # Fallback

    def _calculate_digital_root(self, n):
        """Calculate the digital root of a number"""
        while n >= 10:
            n = sum(int(digit) for digit in str(n))
        return n


def main():
    generator = MagicNumberGenerator()

    print("🎭 Welcome to the Magic Number Generator! 🎭")
    print(
        "Enter any number and I'll generate a magic number with a mystical explanation!"
    )
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("Enter a number: ").strip()

        if user_input.lower() in ["quit", "exit", "q"]:
            print("✨ Thanks for exploring the magic of numbers! ✨")
            break

        result = generator.generate_magic_number(user_input)

        print(f"\n🔮 Magic Number Result:")
        print(f"   Input: {result.get('input', user_input)}")
        print(f"   Magic Number: {result['magic_number']}")
        print(f"   Algorithm: {result.get('algorithm_used', 'Special Magic')}")
        print(f"   Explanation: {result['explanation']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
