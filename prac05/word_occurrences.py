count_words = {}
# gets the word/sentence from the user
get_text = input("Enter your text: ")

# splits get_text into a list
words = get_text.split()

# iterates through words, adding each word to count_words then counts each word by 1
for word in words:
    frequency = count_words.get(i, 0)
    count_words[i] = frequency + 1

# sorts words alphabetically
words = list(count_words.keys())
words.sort()

# finds longest word
max_length = max((len(word) for word in words))

# iterates through word, so we able to print out a list of the words
# counted in a presentable format.
for word in words:
    print("{:{}} : {}".format(word, max_length, count_words[word]))
