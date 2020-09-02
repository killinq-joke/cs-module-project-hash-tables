def word_count(s):
    # Your code here
    res = {}
    for i in ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']:
        s = s.replace(f"{i}", '')
    for i in ['\r', '\t', '\n']:
        s = s.replace(f"{i}", " ")
    s = s.lower()
    s = s.split(" ")
    for i in s:
        if i != "":
            res[f"{i}"] = s.count(i)
    return res


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))
