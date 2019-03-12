import collections
frequency = collections.Counter()
with open('D:/articles.txt', 'r') as f:
     text = f.read()
     frequency = collections.Counter(text.split())
print(frequency.most_common(1))