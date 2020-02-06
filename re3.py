# Input  : Hello shubhamg199630@gmail.com Rohit neeraj@gmail.com
# Output : shubhamg199630@gmail.com neeraj@gmail.com?
import re
text="Hello shubhamg199630@gmail.com Rohit neeraj@gmail.com"
o="shubhamg199630@gmail.com neeraj@gmail.com"
e=re.findall('\S+@\S+',text)
print(e)