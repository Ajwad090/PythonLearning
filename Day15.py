#Week 3
#Day 15 : Python Lists 3
alist = ["apple" , "banana" , "cherry"]
print(len(alist))
alist.append("orange")
print(alist)
alist.insert(1 , "orange")
print(alist)
alist.remove("orange")
print(alist)
alist.pop()
print(alist)
alist.pop(1)
print(alist)
one = ["apple" , "banana" , "cherry"]
#two = one.copy() after research a problem AttributeError the method "copy() is not compatible with python 2.x and python 3.x, "
#use keyword "list(one)"
two = list(one)
one.pop(0)
print(one)
print(two)

newList = list(("apple","banana","cherry"))
print(newList)

