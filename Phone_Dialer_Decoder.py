number = "3662277"
number = list(number)
words = ["foo","bar","baz","emo","cap","foobar","car","cat"]

dial_pad = {2:['a','b','c'],'3':['d','e','f'], '4':['g','h','i'],'5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
output = []
final_output = []
# converting string input to a list
num_of_words = len(words)
for word in range(num_of_words):
    words[word] = list(words[word])


alphabets = 0
numbers = 0

# for every word in the list of words
for word in range(num_of_words):

    # while the number index is below the total length AND alphabet index is less than total length
    while numbers < len(number) and alphabets < len(words[word]):
        # if number at that index is less than or eq to 1, move to the next index of number
        if int(number[numbers]) <= 1:
            numbers += 1
        # if number at that index is 2,3,4,5,6,7,8,9 then search if the corresponding alphabets falls in the dictionary value


        elif int(number[numbers]) == 2:
            if words[word][alphabets] == dial_pad[2][0] or words[word][alphabets] == dial_pad[2][1] or words[word][alphabets] == dial_pad[2][2]:
                # if YES, increase the number index as well as alphabet index
                numbers += 1
                alphabets += 1
            else:
                numbers += 1


        elif int(number[numbers]) == 3:
            if words[word][alphabets] == dial_pad['3'][0] or words[word][alphabets] == dial_pad['3'][1] or words[word][alphabets] == dial_pad['3'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1
        elif int(number[numbers]) == 4:
            if words[word][alphabets] == dial_pad['4'][0] or words[word][alphabets] == dial_pad['4'][1] or words[word][alphabets] == dial_pad['4'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1

        elif int(number[numbers]) == 5:

            if words[word][alphabets] == dial_pad['5'][0] or words[word][alphabets] == dial_pad['5'][1] or words[word][alphabets] == dial_pad['5'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1

        elif int(number[numbers]) == 6:
            if words[word][alphabets] == dial_pad['6'][0] or words[word][alphabets] == dial_pad['6'][1] or words[word][alphabets] == dial_pad['6'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1

        elif int(number[numbers]) == 7:
            if words[word][alphabets] == dial_pad['7'][0] or words[word][alphabets] == dial_pad['7'][1] or words[word][alphabets] == dial_pad['7'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1

        elif int(number[numbers]) == 8:
            if words[word][alphabets] == dial_pad['8'][0] or words[word][alphabets] == dial_pad['8'][1] or words[word][alphabets] == dial_pad['8'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1

        elif int(number[numbers]) == 9:
            if words[word][alphabets] == dial_pad['9'][0] or words[word][alphabets] == dial_pad['9'][1] or words[word][alphabets] == dial_pad['9'][2]:
                numbers += 1
                alphabets += 1
            else:
                numbers += 1
    # at the end of each loop, check if word was found , if yes, add that word to the output list
    if alphabets == len(words[word]):
        final_output.append("".join(words[word]))

    # at the end of each cylce when either word is found or not, increase the word index

    word += 1


print(final_output)