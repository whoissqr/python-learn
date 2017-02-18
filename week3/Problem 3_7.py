"""
Problem 3_7:
Write a function that would read a CSV file that looks like this, flowers.csv:

petunia,5.95
alyssum,3.95
begonia,5.95
sunflower,5.95
coelius,4.95

and look up the price of a flower and print out that price.  Remember to import
the necessary library.

Here is my run on the above CSV file:
problem3_7("flowers.csv","alyssum")
3.95

Solution starter:
"""
#%%
import csv

def problem3_7(csv_pricefile,flower):
    flowerDict={}
    with open(csv_pricefile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
             flowerDict[row[0]]=row[1]
    print(flowerDict[flower])
#%%