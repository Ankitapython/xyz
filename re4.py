import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email ="ankita326@gmail.com"
if (re.search(regex, email)):
    print("Valid Email")
else:
    print("Invalid Email")

