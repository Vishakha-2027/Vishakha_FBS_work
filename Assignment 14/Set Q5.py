string=["flower","flow","flight"]

prefix = set(string[0])
for s in string[1:]:
    prefix &= set(s)

longest_prefix = ''.join(sorted(prefix))
print("longest common prefix",longest_prefix)