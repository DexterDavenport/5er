run_program = True

guess_letters = []
not_in_letters = []

while run_program == True:
    words = open('biggest_list.txt','r')

    possible_word_list = []
    not_spot_letters = []
    spot_letters = []

    Lines = words.readlines()

    guess = input(f"What letters are in the word: {guess_letters} ")
    not_in = input(f"What letters are NOT in the word: {not_in_letters} ")
    spot1 = input("\nSpot 1: ")
    spot2 = input("Spot 2: ")
    spot3 = input("Spot 3: ")
    spot4 = input("Spot 4: ")
    spot5 = input("Spot 5: ")

    not_spot1 = input("\nNot in Spot 1: ")
    not_spot2 = input("Not in Spot 2: ")
    not_spot3 = input("Not in Spot 3: ")
    not_spot4 = input("Not in Spot 4: ")
    not_spot5 = input("Not in Spot 5: ")

    print()

    spot_letters.append(spot1)
    spot_letters.append(spot2)
    spot_letters.append(spot3)
    spot_letters.append(spot4)
    spot_letters.append(spot5)

    not_spot_letters.append(not_spot1)
    not_spot_letters.append(not_spot2)
    not_spot_letters.append(not_spot3)
    not_spot_letters.append(not_spot4)
    not_spot_letters.append(not_spot5)

    get_guess = []
    get_guess[:] = guess
    for o in get_guess:
        guess_letters.append(o)

    get_not_in = []
    get_not_in[:] = not_in

    for q in get_not_in:
        not_in_letters.append(q)

    for line in Lines:
        y = line.split()
        possible_word_list.append(y[0])

    for word in possible_word_list:
        
        in_word = True
        word_letter = []
        word_letter[:] = word

        for letter in guess_letters:
            if letter.lower() in word and in_word == True:
                in_word = True

                for i in range(5):
                    if word_letter[i] == spot_letters[i] and spot_letters[i] != '' and in_word == True:
                        in_word = True
                    elif spot_letters[i] == '' and in_word == True:
                        in_word = True
                    else:
                        in_word = False
                        break
                    if not_spot_letters[i] != '' and in_word == True:
                        letters = (list(not_spot_letters[i]))

                        for l in letters:
                            if l == word_letter[i]:
                                in_word = False
                                break
            else:
                in_word = False
        for bad in not_in_letters:
            if bad.lower() in word:
                in_word = False

        if in_word == True:
            print(word)  

    rerun = input("\nWould you like to run the program again(Y/N): ")
    # empty = input("Did you want to clear all the list(Y/N): ")
    print()

    if rerun.lower() == 'y':
        run_program = True
    else:
        run_program = False
        break
    empty = input("Did you want to clear all the list(Y/N): ")
    print()
    if empty.lower() == 'y':
        guess_letters.clear()
        not_in_letters.clear()
        print('\n---------------------------------------------------------------------------------------------\n')

    