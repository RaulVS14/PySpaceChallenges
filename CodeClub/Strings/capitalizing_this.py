def capitalizing_this(input_string):
    word_list = input_string.split(" ")
    formatted_words = []
    for word in word_list:
        letter_list = list(word)
        for i in range(len(letter_list)):
            if i == 0:
                if letter_list[i].islower():
                    letter_list[i] = letter_list[i].upper()
            else:
                if letter_list[i].isupper():
                    letter_list[i] = letter_list[i].lower()
        formatted_words.append("".join(letter_list))
    return " ".join(formatted_words)


if __name__ == '__main__':
    assert capitalizing_this("hello world") == "Hello World"
    assert capitalizing_this("hellO worlD") == "Hello World"
    assert capitalizing_this("HELLO World") == "Hello World"
