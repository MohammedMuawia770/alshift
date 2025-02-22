def revers_word(sentence):
    words = sentence.split(" ")

    new_word = [word[::-1] for word in words]

    rev = " ".join(new_word)
    return rev

name = "mohammed muawia awadalla mostafa"
print(name)
