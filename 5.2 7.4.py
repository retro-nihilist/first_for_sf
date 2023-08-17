guests = ["Boris", "Ivan", "Bob"]  

#new_guests=list(map(guests, lambda name: "Mr. " + name))

#new_guests= map(lambda name: "Mr. " + name, guests)
#print(new_guests)

new_guests= list(map(lambda name: "Mr. " + name, guests))

#new_guests= list(map(lambda: "Mr. " + name, guests)) 


print(new_guests)