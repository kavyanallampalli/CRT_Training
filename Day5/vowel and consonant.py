'''write a python program to check the count of vowels 
and consonants present in the string or not'''


string=input("Enter the string ")
vowel,consonant=0,0
for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel+=1
        else:
            consonant+=1
print(f"Vowel count is {vowel}")
print(f"Consonant count is {consonant}")
