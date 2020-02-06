import re
p=re.compile('[a-e]')
r=re.compile('\d+')
print(p.findall("Aye, at 10 am said Mr. johnbenson Stark"))
print(r.findall("Aye, at 10 am said Mr. johnbenson Stark"))

# \w is equivalent to [a-zA-Z0-9_].
s = re.compile('\w')
print(s.findall("the prince is lionshifter"))

o=re.compile('ab*')
print(o.findall('abababa'))

print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE))

print(re.sub('ub', 'al' , 'Subject has Uber booked already', flags = re.IGNORECASE))


print(re.subn('ub', '&&' , 'Subject has Uber booked already'))
t = re.subn('ub', '##' , 'Subject has Uber booked already', flags = re.IGNORECASE)
print(t)
print(len(t))


print(re.escape("This is Awseome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW")) 