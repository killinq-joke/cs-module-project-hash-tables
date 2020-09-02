from word_count import word_count

def no_dups(s):
    # Your code here
    return ' '.join([i for i in word_count(s).keys()])
    
    


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))