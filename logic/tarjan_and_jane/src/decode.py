import json

with open('data/tree.txt', 'rb') as tree_file:
    tree = tree_file.read()
tree_list = [item for item in tree]

with open('data/pairs.txt', 'r') as pairs_file:
    pairs_json = json.load(pairs_file)


pairs_chars = []
for pair in pairs_json:
    pairs_chars.append((tree[pair[0]], tree[pair[1]]))

print(pairs_chars)
