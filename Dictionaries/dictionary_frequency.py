"""
Dictionary Frequency

This file contains programs for counting the frequency of characters and words using Python dictionaries. Frequency counting is one of the most
common applications of dictionaries and helps in analyzing text data.

Programs Included

1. Character Frequency
2. Word Frequency

Concepts Covered

• Dictionary creation
• Counting occurrences
• Character frequency
• Word frequency
• String traversal
• String methods
• Dictionary update
• Conditional statements
• Loops

Learning Outcomes

After completing these programs, you will be able to:

• Count the frequency of characters in a string.
• Count the frequency of words in a sentence.
• Store frequency counts using dictionaries.
• Use loops and conditional statements with dictionaries.
• Solve common interview and coding practice problems.
"""

# Character frequency 
text=input("Enter a string:")
frequency={}
for ch in text:
  if ch in frequency:
    frequency[ch]+=1
  else:
    frequency[ch]=1
print("Character Frequency:", frequency)

# Word frequency 
sentence=input("Enter a sentence:")
words=sentence.split()
frequency={}
for word in words:
  if word in frequency:
    frequency[word]+=1
  else:
    frequency[word]=1
print("Word Frequency:", frequency)
