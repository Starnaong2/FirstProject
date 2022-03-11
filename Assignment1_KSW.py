#!/usr/bin/env python
# coding: utf-8

# # Introduction to Data Analytics
# ## Python Assignment 1 - Due Nov 5, 2021
# 

# 1.Write a program in Python which reads 10 numbers from a user (e.g. input). Print out the count and sum of the numbers. If the user enters anything other than a number, detect their mistake and print an error message and skip to the next number.

# In[1]:


# Fill in the blank spaces with appropriate code
count=0
tot=0
maxi=None
mini=None
for i in range(1,11):
    
    try:
        numbr = int(input("Please enter %d of 10 numbers : "%i))
        count +=1
        tot += numbr      
        
        if maxi is None or maxi < numbr :
            maxi=numbr
        if mini is None or mini > numbr  :
            mini=numbr
            
    except:
        print(" Not a number !")
        
print("count= ",count)
print("sum= ",tot)
print("maximum= ",maxi)
print("minimum= ",mini)


# 2.	Modify your previous program (in part 1), in addition to the count and sum, print both the maximum and minimum of the numbers entered.

# In[2]:


# Get the name of the file and open it
# Fire paht c:/Download/Emails.txt
name = input('Enter file:')
try:
    handle = open(name, 'r')
except:
    print("Please check File name or File path")
    exit(1)
else:
# Count word frequency
# hint: use the appropriate symbol to split by
 counts = dict()
 for line in handle:
     words = line.split("@")
     for word in words:
         counts[word] = counts.get(word,0) + 1

# Find the most common word
 bigcount = None
 bigword = None
 for word,count in counts.items():
     if bigcount is None or count > bigcount:
         bigword = word
         bigcount = count

# All done
 print(bigword, bigcount)


# ## 3. I have a long list of emails saved in the file Emails.txt (attached to this assignment). Please help me find the most common host or domain (for example in lgguzman@umich.edu, the host is umich.edu). Use the code below and make the appropriate change.

# In[ ]:


# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency
# hint: use the appropriate symbol to split by
counts = dict()
for line in handle:
    words = line.split("@")
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)


# In[ ]:




