import random
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

obj = {}
for i in ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']:
    words = words.replace(f"{i}", '')
for i in ['\r', '\t', '\n']:
    words = words.replace(f"{i}", " ")
words = words.split(" ")
words = [i.lower() for i in words if i]
for i in range(len(words)):
    if i == len(words) - 1:
        obj[words[i]] = "."
    elif words[i] in obj:
        obj[words[i]].append(words[i + 1])
    else:
        obj[words[i]] = [words[i + 1]] 
# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    phrase = ""
    word = random.choice(list(obj.keys()))
    phrase += f"{word} "
    while word != "." and (word in obj or word in obj.values()):
        word = random.choice(obj[word])
        phrase += f"{word} "
    phrase += "\n"
    print(phrase)

