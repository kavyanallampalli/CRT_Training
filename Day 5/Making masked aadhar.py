'''write a python program to read your 12 digit aadhar number as input
from the user and print the 12 digit number where the first 8 digits
are hidden and last four digits are written'''



aadhar=input("Enter your Aadhar Number")
masked=aadhar.replace(aadhar[:8],"********")
masked=masked[:4]+" "+ masked[4:8] + " " +masked[8:]
print("Masked Aadhar Number:",masked)