# write a program to replace a word by another word in a sentence

sentence:str = str(input("Enter the sentence: "))
wordto:str = str(input("Enter the word to replace: "))
replaceby:str = str(input("Replace by : "))

sentence=sentence.replace(wordto,replaceby)

print(sentence)