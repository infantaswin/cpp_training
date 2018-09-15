 def printinfo( name, age =21):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return "savu"

# Now you can call printinfo function
x=printinfo( age=50, name="miki" )
y=printinfo(name="aswin")
print(x)
print(y)
