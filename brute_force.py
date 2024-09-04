import itertools
import string
import time

password = '!2!' # password here

chars = string.printable

max_length = 10

start_time = time.time()

for length in range(1 , max_length + 1):
    for combination in itertools.product(chars , repeat=length):
        candidate = ''.join(combination)
        print(f"Trying Password: {candidate}")

        if password == candidate:
            print(f"Your password is cracked: {candidate}")
            end_time = time.time()
            print(f"Time Taken in this process is: {end_time - start_time}")
            raise SystemExit