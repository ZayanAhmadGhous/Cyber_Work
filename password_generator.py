import random
import string

lenght=int(input("Enter the length of the password: "))

result=(''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase+string.punctuation,k=lenght)))

print(f"The generated password is: {result}")