"""
def vypocitat(x:int) -> int:
    return x*2
print(vypocitat(3))
////
data = 1,2,3,4,5,6,7,8,9,10
for i in range(len(data)):
   print(data[i])
///
data = 3,7,6,11,5,5,8,9
prev = 0
for value in data:
  if value != prev:
    print(value/(value - prev))
prev = value
////
scores = [50, 80, 45, 90, 30, 60]
seznam = []
for i in range(len(scores)):
    if scores[i] < 50:
        seznam.append(scores[i])
print(seznam)
"""

# Cílem je vytvořit dvojice jmen ze seznamu (např. pro turnaj).
#slovo
"""
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
pairs = []

for i in range(len(names)):
    if i + 1 < len(names):
        pairs.append(names[i] + " - " + names[i+1])

print(pairs)
"""
