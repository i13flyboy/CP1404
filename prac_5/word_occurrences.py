word_count = {}
text = input("Tex: ")
words = text.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] =frequency + 1

words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))

# this code will take a sentence and display the number of the same words used in that sentence.