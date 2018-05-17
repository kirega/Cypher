import datetime
now = datetime.datetime.now()
print(now.isoformat())

f = open( 'Jobs on '+ str(now.isoformat())+'.json', "w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))