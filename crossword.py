pre = str(input())
bod = str(input())
length = int(input())
word_length = (len(pre) + len(bod))

if (word_length == length):
  if (len(pre) > len(bod)):
    print(bod + pre)
  else:
    print (pre + bod)
else:
	print(False)
