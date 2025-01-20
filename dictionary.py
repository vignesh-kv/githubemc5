a={"name":"emc",
   "age":"10",
   "location":"chennai",
   "student":"chinna"}
a["age"]=15
a["colour"]="black"
a.update({"age":16})
del a["colour"]
del a
a.clear()
print(a)
