import re

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

a= re.search('c','abcdefghik')
print(a)
b=re.match('^c','abcdefghik')
print(b)

text = "He was carefully disguised but captured quickly by police. i went to mall from townhall"
print(re.findall(r"\w+all", text))

for m in re.finditer(r"\w+ly", text):
    print (m.start(), m.end(), m.group(0))
