number = int(input("Enter a number: "))
divisor_count = 0
for i in range(1, number + 1):
    if number % i == 0:
        divisor_count += 1
print(f"The divisors of {number} are {divisor_count}")

