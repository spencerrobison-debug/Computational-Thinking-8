import random

# Pick a word at random
word_list = ["heart","loopy","audio","laugh","trial", "hello", "slate", "adieu", "shame", "blame", "droop", "shunt", "amble","ambos","ambry","ameba","ameer","amend","amene","amens","ament",]
hidden_word = random.choice(word_list)


# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("The word has to be 5 letters.")
else:
    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Second letter
if len(guess_word) != 5:
    print()
else:
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Third letter
if len(guess_word) != 5:
    print
else:
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter
if len(guess_word) != 5:
    print()
else:
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fifth letter
if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")


# Guess 2

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if len(guess_word) != 5:
    print("The word has to be 5 letters.")
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Second letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Third letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fifth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

# Guess 3

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if len(guess_word) != 5:
    print("The word has to be 5 letters.")
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Second letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Third letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fifth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

# Guess 4

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if len(guess_word) != 5:
    print("The word has to be 5 letters.")
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Second letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Third letter
if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
# Fifth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

# Guess 5

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if len(guess_word) != 5:
    print("The word has to be 5 letters.")
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Second letter
if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Third letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fifth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

# Guess 6

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if len(guess_word) != 5:
    print("The word has to be 5 letters.")
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Second letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Third letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fifth letter

if len(guess_word) != 5:
    print()
else:
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")




