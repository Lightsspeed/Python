import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*():;,.<>/?|=+-_")

#print(characters)

chars = []

random.shuffle(characters)

for i in range(10):
    z = chars.append(random.choice(characters))    
print(chars)
print(z)