
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		counted_dict = Counter(f.read().split())
		top_5 = counted_dict.most_common(5)
		for word, count in top_5:
			print(word,":", count)

word_count("document.txt")





file = open('document.txt', 'r')
read_data = file.read()
per_word = read_data.split()


print("Total words:", len(per_word))

