input1= input('Enter a sentence or a word - ')

vowels= {'a':0,
         'e':0,
         'i':0,
         'o':0,
         'u':0}

for i in input1:
    if i in vowels:
        vowels[i] += 1


print(vowels)





