import random
import beverages

class CoffeeMachine:
	def __init__(self):
		self.count = 0

	class EmptyCup(beverages.HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			self.message = "This coffee machine has to be repaired."

	def repair(self):
		self.count = 0

	def serve(self, hotbeverage: beverages.HotBeverage):
		if self.count > 9:
			raise BrokenMachineException()
		else:
			self.count += 1
			if random.randint(0, 1) == 0:
				return hotbeverage
			else:
				return self.EmptyCup()

class BrokenMachineException(Exception):
	def __init__(self):
		self.message = "This coffee machine has to be repaired."
  
def main():
	coffee_machine = CoffeeMachine()
	coffee = beverages.Coffee()
	cappuccino = beverages.Cappuccino()
	try:
		for i in range(0, 15):
			print(coffee_machine.serve(coffee))
	except BrokenMachineException as e:
		print(e.message)
	coffee_machine.repair()
	try:
		for i in range(0, 15):
			print(coffee_machine.serve(cappuccino))
	except BrokenMachineException as e:
		print(e.message)
  
if __name__ == '__main__':
	main()