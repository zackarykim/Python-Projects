def generate_prime_numbers():
  """Generates prime numbers up to a given limit."""

  limit = int(input("Enter the limit: "))  # Get user input for limit
  primes = [2]  # Start with 2 as the first prime number

  for num in range(3, limit + 1, 2):  # Iterate over odd numbers
    if all(num % prime != 0 for prime in primes):
      primes.append(num)

  return primes

# Call the function to generate prime numbers
prime_numbers = generate_prime_numbers()

# Now the limit variable is accessible outside the function
print("Prime numbers up to :", prime_numbers)