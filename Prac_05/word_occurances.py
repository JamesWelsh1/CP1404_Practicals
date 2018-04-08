individual_different_words = {}
input_text = input("Text: ").lower()
words = input_text.split()
# print(words)
for word in words:
    frequency = individual_different_words.get(word,0)
    # print(frequency)
    individual_different_words[word] = frequency + 1
    # print(individual_different_words)

words = list(individual_different_words.keys())
words.sort()
# print(words)

max_length = max(len(word) for word in words)

for word in words:
    print("{:{}} : {}".format(word, max_length, individual_different_words[word]))
