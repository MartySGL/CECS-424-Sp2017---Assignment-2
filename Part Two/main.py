def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_primes():
    sum = 1
    primes = get_primes(0)
    for i in primes:
        if (i >= 2000000):
            print(sum)
            return
        sum = sum + i

def get_primes(n):
    while True:
        if is_prime(n):
            yield n
        n += 1

def main():
    sum_primes()

if __name__ == "__main__":
    main()
