def string_match(str, word):
    for i in range(len(str) - len(word) + 1):
        if (str[i:i + len(word)]) == word:
            return 1
    return -1

str = "Hello World"
word = " World"
res = string_match(str, word)
if res == 1:
    print("Found")
else:
    print("not found")
