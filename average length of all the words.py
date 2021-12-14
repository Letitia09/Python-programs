import math
a=input()# input is "this phrase has multiple words"
word=1
letter=0
for i in range(len(a)):
    if a[i]==' ':
        word+=1
    if a[i]>='a' and a[i]<='z':
        letter+=1
#print(word) --5
#print(letter)  --26
avg_word_length=letter/word  #26/5=5.20
#A number representing the average length of each word, rounded up to the nearest whole number.
print(math.ceil(avg_word_length))
#expected output is 6 .so, we need to use ceil function
# The string in question has five words with a total of 26 letters (spaces do not count). The average word length is 5.20 letters, rounding it up to the nearest whole numbers results in 6.
