from customer.customer import Customer
from state_machine.state_machine import CustomerStateMachine
from data_classes import status, rules

dados = {'name': 'Otavio', 'email': 'otavio@a.com'}

usuario = Customer(dados)
usuario.print_information()

usuario.name = 'José'
usuario.print_information()

denie = 'Payment denied'


customer_machine = CustomerStateMachine(rules.rules, usuario)
customer_machine.print_everything()

customer_machine.make_transition('Payment confirmed')
