set={1,2,3,8,3,9,5,2,1,6,-3}
print(set)
print(len(set))
set.add('new')
set.remove('new')
print(set)
print(sum(set))
print(max(set))
print(min(set))
print(sorted(set))

print("set doesn't allow copies of data")
for item in set:
    print(item," ",end="") 