# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import random
from string import ascii_uppercase

obj = {}
common_char = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
arr = []
# Read in all the words in one go
with open("ciphertext.txt") as f:
    words = f.read()

for c in ascii_uppercase:
    obj[c] = words.count(c)
    
obj = sorted(obj.items(), key=lambda x: x[1], reverse=True)
for i in obj:
    arr.append(i[0])

with open("ciphertext.txt") as f:
    bop = f.read()


trantab = str.maketrans("".join(arr), "".join(common_char))

print(bop.translate(trantab))