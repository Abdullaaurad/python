from collections import defaultdict

# Input
n, m = map(int, input().split())  # group A size, group B size
group_a = [input().strip() for _ in range(n)]  # words belonging to group A
group_b = [input().strip() for _ in range(m)]  # words belonging to group B

# Create defaultdict to store indices of each word in group A
indices_dict = defaultdict(list)
for idx, word in enumerate(group_a, start=1):
    indices_dict[word].append(idx)

# Check occurrences of words from group B in group A
for word_b in group_b:
    if word_b in indices_dict:
        print(' '.join(map(str, indices_dict[word_b])))
    else:
        print(-1)
