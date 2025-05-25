import random
import string

length=int(input("Enter the length of the password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)
password = "".join(temp)
print("Generated Password: ", password)

    
    
