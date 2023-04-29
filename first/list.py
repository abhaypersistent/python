#data structure
name = ["india","pakistan","bangladesh","USA","UK","Norway","Germany"]
# can be any thing string, number, boolean

# name[2] = "USA"
# print( "India" in name)
# print(name[2])
# print(name[-2])
# print(name[2:])
# print(name[:2])
# print(name)

name.append("Russia")

name.extend(["Spain","Italy"])
name.remove("pakistan")
# print(name.pop())
# print(name)


# name.insert(2,"Nepal")
name[1:1] = ["Pune", "mumbai","Kharghar"];
print(name)
# += same as extend

# copying the list
nameCopy = name[:]

# sort list
name.sort()
print(name)
print(nameCopy)

