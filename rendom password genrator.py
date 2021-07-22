import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
numbers ="0123456789"
symbols="(){}[]/?<>,.:;&*+^%$#@"

all = lower + upper + numbers + symbols
length = 20
password = "".join(random.sample(all,length))
print(password)