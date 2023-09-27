# 2.Write a function in Python to count words in a
# text file those are ending with alphabet "e" (create your own text file for that)

word_count = 0
with open("test.txt","r") as file:
    for x in file:
        split_word = x.split(" ")
        print(split_word)
        for i in split_word:
            word = i.endswith("e")
            if word:
                word_count +=1

    print(word_count)

