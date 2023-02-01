from typing import List
from data_classes.data_classes import BusinessRulesDataClass
from customer.customer import Customer


class StateMachine:
	def __init__(self, business_rules: List[BusinessRulesDataClass]):
		self._business_rules = business_rules

	def _validate_transition(self, current_state: str, destination_state: str):
		return any(
			[
				rule['source'] == current_state and 
				rule['destination'] == destination_state 
				for rule in self._business_rules
			]
		)


class CustomerStateMachine(StateMachine):
	def __init__(self, business_rules: List[BusinessRulesDataClass], customer: Customer):
		super().__init__(business_rules)
		self._customer = customer

	def validate_status(self, status: str):
		if status not in [
			'Not payed',
			'Payment confirmed',
			'Payment denied',
			'Payment issued',
			'Payment waiting validation',
			'Payment expired',
		]:
			raise ValueError("Status inexistente na base atual.")
		return True

	def _general_validate(self, desired_step: str):
		self.validate_status(desired_step)
		self._validate_transition(self._customer.payment_status, desired_step)

	def make_transition(self, desired_step: str):
		self._general_validate(desired_step)
		self._customer.payment_status = desired_step

	def print_everything(self):
		print(f'{self._customer._name} -> {self._customer.payment_status} / {self._business_rules}')
