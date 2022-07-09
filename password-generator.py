import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"

lenght = 10
all = lower + upper + num
password = "".join(random.sample(all, lenght))
print(password)
