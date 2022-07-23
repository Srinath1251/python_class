from collections import Counter

nums = [1, 1, 2, 3, 4, 2, 2, 4, 5, 5, 6, 7, 7, 8, 9]

counts = Counter(nums)

print(counts)

top3 = counts.most_common(3)
