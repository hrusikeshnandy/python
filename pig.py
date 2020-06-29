# get input from the user
original = input("Enter the sentence: ").strip().lower()

#split sentence to words
words = original.split()
print(words)

# iterate through words and formulate word
new_words=[]
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vow_pos = 0
        for letters in word:
            if letters not in "aeiou":
                vow_pos = vow_pos +1
            else:
                break
        cons = word[:vow_pos]
        rest_word = word[vow_pos:]
        new_word = rest_word + cons + "yay"
        new_words.append(new_word)

# make sentence
output = " ".join(new_words)
#output
print(output)
