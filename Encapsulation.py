# In an object oriented python program, you can restrict access to methods and variables. 
# This can prevent the data from being modified by accident and is known as encapsulation.   
# Let’s start with an example.

class Name:
	 
	def setFirstName(self, firstname):
		self.__firstname = firstname 

	def setMiddleName(self, middletname):
		self.__middletname = middletname 

	def setLastName(self, lastname):
		self.__lastname = lastname 

	def getFirstName(self):
		return self.__firstname

	def getMiddleName(self):
		return self.__middletname

	def getLastName(self):
		return self.__lastname
	 
# Set variables
name = Name()
name.setFirstName("Ken Dan")
name.setMiddleName("S.")
name.setLastName("Tinio")

# Display the values
print(name.getFirstName())
print(name.getMiddleName())
print(name.getLastName())