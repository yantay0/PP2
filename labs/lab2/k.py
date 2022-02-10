snts = sorted(list(set(input().split())))
print(len(snts))
for i in snts:
   print(i[:-1] if "." in i or "?" in i or "!" in i or "," in i else i)
