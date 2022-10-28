# import math
#
# z = []
# user = int(input("Enter a y: "))
# for n in range(2, user):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals to {x}*{n // x}")
#             break
#     else:
#         print(f"{n} is prime")
#         z.append(n)
# print(f"We find {len(z)} primes.")
# ************************************************************************************************************
primes = []
for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))

print(primes)
print(", ".join(primes))