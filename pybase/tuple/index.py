#-*- coding:utf-8 –*-
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tuple4 = tup2 + tup3
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
print tuple4

print len(tuple4)
print len(tuple4 * 4)
print 'a' in tuple4
tuple5 = tuple4
print 'compare tuple', cmp(tup3,tuple4)
if cmp(tuple5 , tuple4) == 1:
    print 'not equal'
else:
    print 'equal 试试中文'