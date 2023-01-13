'''Write a Python program to compute following operations on String:
 a) To display word with the longest length 
 b) To determines the frequency of occurrence of particular character in the string 
 c) To check whether given string is palindrome or not 
 d) To display index of first appearance of the substring
 e) To count the occurrences of each word in a given string'''


strng=input("Enter a string: ")                          #string input
s=strng.split()
print(s)
print("Word withh longest length: ",max(s,key=len))      #longest word



p=""                                                     #Palindrome
for i in strng:
    p=i+p
if strng==p:
        print("String is palindrome")
else:
        print("String is not a palindrome")



freq={}                                   #frequency of occurrence of particular character in the string 
for i in strng:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("occurrence of particular character in the string : ",freq)



sub=input("Enter substring: ")                   #index of first appearance of the substring
f=strng.index(sub)
print("Index of first appearance of the substring: ",f)



word={}                                          #Word count
for i in s:
    if i in word:
        word[i]+=1
    else:
        word[i]=1
print("Occurrences of each word in a given string ",word)
