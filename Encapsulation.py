class Name:
	def setFirstName(self, firstname):
		self.firstname = firstname 

	def setMiddleName(self, middletname):
		self.middletname = middletname 

	def setLastName(self, lastname):
		self.lastname = lastname 

	def getFirstName(self):
		return self.firstname

	def getMiddleName(self):
		return self.middletname

	def getLastName(self):
		return self.lastname
	 
# Set variables
name = Name()
name.setFirstName("Ken Dan")
name.setMiddleName("S.")
name.setLastName("Tinio")

# Display the values
print(name.getFirstName())
print(name.getMiddleName())
print(name.getLastName())