def word(s):
    main=list(s)
    indexed= []
    vowels= []

    for letter in s:
        if letter in ["a" , "e" , "i", "o", "u"]:
         ind = main.index(letter)
        indexed.append(ind)
        vowels.append(letter)
    vowels= vowels[::-1]

    for i in range(0, len(vowels)):
        val =  indexed[i]
        main[val] =  vowels[i]

        st =  ""
        for i in main:
            st += i

        return st

        print(word("Happinessu"))