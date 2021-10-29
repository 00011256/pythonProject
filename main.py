word = input('Type the word you want: ')
check_letter = input('Type the letter you want to check: ')
i = ''

def checking (i, word, letter):
    letter_count = 0
    for i in word:
        if i == letter:
            letter_count = letter_count + 1

    print(letter_count)

checking(i, word, check_letter)

