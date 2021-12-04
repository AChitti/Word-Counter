sentence=input("Enter a Sentence")
print(sentence)
carCount=0
wordCount=1
for s in sentence:
    carCount=carCount+1
    if(s==' '):
        wordCount=wordCount+1
print("#ofWords: ")
print(wordCount)
print("#ofCharacters: ")
print(carCount)