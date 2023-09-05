s = "acb"
t = "ahbgdc"
n = len(s)
count = 0
letters = [x for x in s]
for letter in letters:
    if letter in t:
        count += 1
if count == n:
    print(True)
else:
    print(False)