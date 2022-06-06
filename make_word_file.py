words = open('big_list.txt','r')

Lines = words.readlines()
possible_word_list = []
for line in Lines:
    x = line.split()
    for i in range(len(x)):
        with open('biggest_list.txt', 'a') as f:
            f.write(x[i].lower())
            f.write("\n")
        possible_word_list.append(x[i])
print(possible_word_list)

