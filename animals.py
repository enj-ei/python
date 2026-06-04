animals = {"dog","cat","lion","tiger","monkey"}
print(animals)

#add


animals.add("hippo")
print(animals)

#update


animals.update({"leopard","bears"})
print(animals)

#remove
animals.remove("cat")
print(animals)

#functio use
print(len(animals))


#delete 
del animals
print("deleted")


#set
animals = {"Dog", "Cat", "Lion", "Tiger", "Elephant"}

#Convert set to list
animal_list = list(animals)
print("List:", animal_list)

#Convert set to tuple
animal_tuple = tuple(animals)
print("Tuple:", animal_tuple)

#Convert set to dictionary
animal_dict = dict.fromkeys(animals, "Animal")
print("Dictionary:", animal_dict)







