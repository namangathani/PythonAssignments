#dictionary item

thisdict = {
  "brand": "abc",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#dictionary change items
thisdict = {
  "brand": "abc",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["year"] == 2018)

#dictionary adding
thisdict = {
  "brand": "Ford",
  "model": "diesel",
  "year": 1999
}
thisdict["color"] = "red"
print(thisdict)

#dictionary remove items
thisdict = {
  "brand": "adc",
  "model": "efg",
  "year": 2000
}
thisdict.pop("model")
print(thisdict)

#dictionary loop
for x in thisdict:
  print(x)

#dictionary copy
thisdict = {
  "brand": "figo",
  "model": "benz",
  "year": 1675
}
mydict = thisdict.copy()
print(mydict)

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "cutie",
    "year" : 2002},
  "child2" : {
    "name" : "lovely",
    "year" : 2007},
  "child3" : {
    "name" : "dolly",
    "year" : 2011 }
}
print(myfamily)
