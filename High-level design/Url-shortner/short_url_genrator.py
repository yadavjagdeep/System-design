"""
Shortening algorithm.
For shorting the url, we can use the following two solutions
1. URL Encoding
2. Key Generation service

URL Encoding through base62["0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]

Let's check how many chars we shall keep for our tiny url
length 5 can have 62^5= ~916 million URLs
length 6, can have 62^6 = ~56 billion URLs
length 7, can have 62^7 = ~3500 billion URLs

Let's assume we need 100 million URLs per month and expiry for 100 years
100 * 100 * 12 = 120 billion

Using length of 7 should work

1. Generate a random string and check if it does not exist in DB then store the same, else continue rolling/retrying
2. To overCome the issue in random string generation, what we can do is to use counter
-> for each server running the service assign a range of numbers, and for each time when they need tiny url it passes the
number and increments the counter at local server.

-> The problem with this approach the service generating range is single point of failure, so we can have multiple
instances of the service and use zookeeper to orchestrate the same which mange and assign the range.

"""


def generate_random_base62_string(length=7):
    import random
    max_value = 62 ** length - 1
    number = random.randint(0, max_value)

    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    # Convert the number to base62
    while number > 0:
        result = base62[number % 62] + result
        number //= 62

    return result[:length]


print(generate_random_base62_string())


def generate_base62_string(counter, length=7):
    """
  Generates a random-looking string of the specified length using base62 encoding
  for a given counter-value. Optionally adds a hash for additional security.
  """
    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    # Convert the counter to base62
    while counter > 0:
        result = base62[counter % 62] + result
        counter //= 62

    # Prepend leading zeros if necessary
    result = result.zfill(length)
    return result[:length]


print(generate_base62_string(counter=12345))
