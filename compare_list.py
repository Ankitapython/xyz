list1, list2 = [1,2,3,4],[1,2,3,4,6]
print (cmp(list1, list2))
print (cmp(list2, list1))
list3 = list2 + [786]
print (cmp(list2, list3))

# dict
dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict.has_key('Age'))
print ("Value : %s" %  dict.has_key('Sex'))
l=[1,2,3,4,5,6]
print([x*3 for x in l if x % 2 == 0 ])