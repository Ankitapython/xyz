import re
regex = r"([a-zA-Z]+) (\d+)"

match=re.search(regex, "I was born on June 24")
if match != None:


    print "Match at index %s, %s" % (match.start(), match.end())


    print "Full match: %s" % (match.group(0))

    # So this will print "June"
    print "Month: %s" % (match.group(1))

    # So this will print "24"
    print "Day: %s" % (match.group(2))

else:
    print "The regex pattern does not match."