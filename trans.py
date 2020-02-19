
from string import maketrans   # Required to call maketrans function. replace aeiou with 12345

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow"
print(min(str))

print (str.translate(trantab))
print(max(str))

