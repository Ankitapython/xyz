import time

ticks=time.localtime(time.time())
p= time.asctime( time.localtime(time.time()) )
print(ticks)
print(p)

print( "time.altzone %d " % time.altzone)


t = time.localtime()
print "time.asctime(t): %s " % time.asctime(t)
print "time.ctime() : %s" % time.ctime()