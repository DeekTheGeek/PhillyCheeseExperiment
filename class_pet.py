class Dog():
	'''An attempt to model a dog'''
	
	def __init__(self, name, age, owner, breed):
		'''initialize dog's attributes'''
		self.name = name
		self.age = age
		self.owner = owner
		self.breed = breed
		# You can set a value in a class
		self.trained = True
	
	def __str__(self):
			'''return a description using the attributes'''
			describe = ("\n" + self.name.title() + ' is a(n) '
				+ self.age + ' year old ' + self.breed.title() 
				+ ' owned by '+ self.owner.title() + '.')
			return describe
		
	def sit(self):
		'''simulate a dog sitting in response to a command'''
		print('\n' + self.name.title() + ' is now sitting.')
		
	def roll_over(self):
		'''simulate a dog rolling over in response to a command'''
		print('\n' + self.name.title() + ' rolled over.')
	
	def ready(self):
		'''simulate a dog ready and waiting for a new command'''
		print('\n' + self.name.title() + ' is ready for a new command.')
	
	def sleep(self):
		'''simulate a dog sleeping'''
		print('\n' + self.name.title() + ' is sleeping.')

	def warning(self):
		'''warn when not trained'''
		if self.trained != True:
			warn = '\nWARNING: ' + self.name.title() + ' is untrained.'
			return warn

	def untrained(self):
		'''change to untrained as needed'''
		self.trained = False


class Cat(Dog):
	'''An attempt to model a cat using dog attributes'''
	
	def __init__ (self, name, age, owner, breed):
		'''initialize cat attributes'''
		super().__init__ (name, age, owner, breed)
		self.trained = False

	def __stat__ (self):
		'''description of cat'''
		return super().__str__ (self)

	def warning(self):
		'''Warn you cannot play with cats'''
		# different value but same name as dog class
		print('\nYou cannot play with cats. Cats play you.')
