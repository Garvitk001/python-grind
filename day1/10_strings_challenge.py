'''Function naam  : analyze_text
Input          : koi bhi sentence (string)
Output         : 
    - Total words
    - Total characters (spaces ke bina)
    - Longest word
    - Kitni baar 'a' aaya
    - Sentence ko reverse karo'''


'''len(sentence.split()) — words
len(sentence.replace(" ", "")) — characters without spaces
max(sentence.split(), key=len) — longest word
sentence.count("a") — count
" ".join(reversed(sentence.split())) — reverse'''



sentence = "I want to become a data scientist in India"

print("=====Text Analysis=====\n")

print(f"Sentence   : {sentence}")
print(f"Words      : {len(sentence.split())}")
print(f"Character  : {len(sentence.replace(" ",""))}")
print(f"Longest    : {max(sentence.split(),key=len)}")
print(f"Count of a : {sentence.count("a")}")
print(f"Reversed   : {" ".join(reversed(sentence.split()))}")
print(f"    {sentence[::-1]}")