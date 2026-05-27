mylist =list(("Ram" , "Sam" , "Sita" , "Amy" , "Prit"))
print(mylist[0])
print(mylist[-2])

print(mylist[1:4])
print(mylist[::-3])

tuple1 = ("A" , "B" , "C" , "D" , "E")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("true", "true", "false")



print(tuple1)
print(tuple2)
print(tuple3)



pokhara = {
    "district" : "kaski",
    "country" : "Nepal",
    "university" : "pokhara university"
}


pokhara["university"] = "kathmandu university"
print(pokhara["university"])


#to print list into tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)


my_string = "hello "
my_tuple = tuple(my_string)
print(my_tuple)


#to convery tuple into list
my_tuple = ["h" , "e" , "l" , "l" , "o"]
my_list = list(my_tuple)
print(my_list)

my_tuple = tuple(my_string)
print(my_tuple)


my_tuple = ("h" , "e" , "l" , "l" , "o")

my_string = ''.join(my_tuple)
print(my_string)


#dict to tuple
my_dict = {"name": "Ram" , "age":20, "class":10}
my_tuple= tuple(my_dict.items)
print(my_tuple)

#tuple to dict
my_tuple = (('name','Ram'),('age',20),('class',10))
my_dict= dict(my_tuple)
print(my_dict)

#dict to list
my_dict = {"name": "Ram" , "age":20, "class":10}
my_list = list(my_dict.items())
print(my_list)



