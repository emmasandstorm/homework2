
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		counted_dict = Counter(f.read().split())
		top_5 = counted_dict.most_common(5)
		for word, count in top_5:
			print(word,":", count)
	return counted_dict.most_common(5)

word_count("document.txt")



