def word_frequency(text):
    text = text.lower().split()
    freq = {}

    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


# Main program
sentence = input("Enter a sentence: ")
result = word_frequency(sentence)

print("\nWord Frequency Count:")
for word, count in result.items():
    print(f"{word} : {count}")
