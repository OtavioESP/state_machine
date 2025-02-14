from data_classes.data_classes import CustomerDataClass
from data_classes.status import status

class Customer:
	def __init__(self, customer_data: CustomerDataClass):
		self._payment_status = status['not_payed']
		self._name = customer_data['name']
		self._email = customer_data['email']

	# GETER & SETER ----->
	@property
	def payment_status(self):
		return self._payment_status

	@payment_status.setter
	def payment_status(self, payment_status: str):
		self._payment_status = payment_status

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name: str):
		self._name = name

	def print_information(self):
		print(f'Name: {self._name}, Email: {self._email}')
