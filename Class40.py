class myClass:
	__privateVar = 27

	def __privMeth(self):
		print("I'm inside the class myClass.")

	def hello(self):
		print("Private Variable value: ",myClass.__privateVar)

foo = myClass()
foo.hello()
foo._myClass__privMeth()