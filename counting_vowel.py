vowel=['a','e','i','o','u']
word="Sayantan samanta"
count=0
for i in word:
  if i in vowel:
    count+=1
print(count)