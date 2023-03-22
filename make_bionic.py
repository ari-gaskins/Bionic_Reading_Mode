from termcolor import colored

raw_text = str(input("Paste your text: "))

raw_text_lines = raw_text.split('\n ')
raw_text_words = []

bionic_text_list = []

# TODO: open file for parsing

# TODO: parse lines and test
#for line in raw_text_lines:
#    print(line)

for word in raw_text_lines:
    if len(word) > 1:
        bold_half = word[0 : len(word) // 2]
        bold_half = colored(bold_half, attrs=["bold"])
        bionic_word = bold_half + word[len(word) // 2 : ]
        bionic_text_list.append(bionic_word)
        continue
    bionic_text_list.append(colored(word, attrs=["bold"]))

bionic_text = ' '.join(bionic_text_list)
print(bionic_text)
