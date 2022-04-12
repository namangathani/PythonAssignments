#list
thislist = ["a", "n", "u"]
print(thislist[1])


#change list items
thislist = ["a", "n", "u"]
thislist[1] = "k"
print(thislist)


#add list items
thislist = ["a", "n", "u"]
thislist.append("k")
print(thislist)


#remove list item
thislist = ["a", "n", "u","o"]
thislist.remove("o")
print(thislist)


#loop list
thislist = ["a", "n", "u"]
for x in thislist:
 print(x)


#list compensation
alphabets= ["a", "n", "u", "s", "h"]
newlist = []

for x in alphabets:
  if "a" in x:
    newlist.append(x)

print(newlist)


#list sort
thislist = ["a", "n", "u", "s", "h"]
thislist.sort()
print(thislist)


#copy list
thislist = ["a", "n", "u"]
mylist = thislist.copy()
print(mylist)


#join list
list1 = ["a", "n", "u"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)