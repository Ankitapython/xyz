s="hello"
s1=""
for i in s:
    s1=i+s1
print(s1)

st="hello world python"
sr=' '.join(word[::-1] for word in st.split(" "))
print(sr)
z = 'Best website is Tutorials Point'
print(z.find('Tutorials'))

print([ (a,b) for a in range(3) for b in range(a) ])


d0 = { 'a':1, 'b':2}
d1 = { 'a':3, 'b':4}
p=d1 > d0
print(p)

for i in ['t', 'n', 'i ', 'o', 'p'][::-1]:
   print(i)

a='19' == 19
print(a)

def total(initial =5, *num, **key):
   count = initial
   for n in num:
       count+=n
   for k in key:
       count+=key[k]
   return count
print(total(100,2,3, clouds=50, stars=100))

tinylist = [123, 'john']
print(tinylist * 2 )\

