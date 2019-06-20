import controllers.Encapsulation as en

# Set variables
name = en.Name()
name.setFirstName("Ken Dan")
name.setMiddleName("S.")
name.setLastName("Tinio")

# Display the values
print(name.getFirstName())
print(name.getMiddleName())
print(name.getLastName())
