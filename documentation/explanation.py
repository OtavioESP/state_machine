'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|                                                                   |
|               ===    =====   =====    =====   =====               |
|              |         |    |     |     |    |                    |
|               ===      |    |=====|     |    |=====               |
|                  |     |    |     |     |    |                    |
|               ===      |    |     |     |     =====               |
|                                                                   |
|                                                                   |
|                                                                   |
|   |=   =|    =====     =====   |   |    |   |=    |    =====      |
|   | = = |   |     |   |        |   |    |   | =   |   |           |
|   |  =  |   |=====|   |        |===|    |   |  =  |   |=====      |
|   |     |   |     |   |        |   |    |   |   = |   |           |
|   |     |   |     |    =====   |   |    |   |    =|    =====      |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

How does it work ??

* For this example i will not make use of the StateMachine extension for Python

* I will make the logic and etc by hand.

* All the code in this file will be organized in the correct... organization..., 
and you will notice that all will be into the folder state_machine and other files outside 
documentation folder.

* All shown here will be made in python, but for implement it in a big 
sistem or real life company product, it can be implemented using the functionalities of a 
database to store the information of the objects and its states for example and other 
tools.

* All classes and codes in this file, specially the ones with sufix _v1, _v2 etc are not 
to be considered to work, but only a visual for ilustrate a idea, to help us build 
the thought as we continue to evolve our application.

* The _V1 and _V2 sufixes are used to express the evolving of the idea ilustrated in the 
classes.

* The working project and its classes etc, will be built outside this file.
'''

'''
Lets say you have a flow of inscription for an event
The customer need to pass in numerous steps to be able to enter that event.

Payment approval.
Documental approval.

- Just these two steps already have within them various steps for validating themselves

Lets take payment step.

A Payment step can either be ( not the best names but still ):

- Not payed
- Payment confirmed
- Payment denied
- Payment issued
- Payment waiting validation
- Payment expired

How does these steps can relate within themselves ?
Well Thats up to the business rules.
But just a sketch we can say for example:

1. A payment can only be confirmed when its waiting payment validation;
2. A payment can only be denied when its waiting payment validation;

Until there ok, simple validations, a boolean in my customer instance can do it.
But lets get more complicated.

3. A payment can only be issued when its Expired or Denied;

This businenss rule intrinsically has 2 validations just for her.
SO now wee ned two fields on the customer instance for checking it out.

And as the business rules grow in number, the booleans in my Customer need to grow 
to store the dinamism of information needed to validate the steps.

Lets work with just these 3 rules for now.
With that in mind lets build a rustic instance of my product.
''' 

class Customer_V1:
    def __init__(self, payment, document):
        self.is_not_payed = True
        self.is_payment_confirmed = False
        self.is_payment_denied = False
        self.is_payment_issued = False
        self.is_waiting_payment_validation = False
        self.is_payment_expired = False

    def confirm_payment(self):
        if self.is_waiting_validation == True:
            self.is_payment_confirmed = True
        else:
            raise Exception

    def denie_payment(self):
        if self.is_waiting_validation == True:
            self.is_payment_denied = True
        else:
            raise Exception

    def issue_payment(self):
        if self.is_payment_expired == True or self.is_payment_denied == True:
            self.is_payment_issued = True
        else:
            raise Exception

'''
Ok, we just saw that the its a lot of trouble to make the functions and validations 
just for simple transitions.

But how can we make it more simple ?
Simple... STATE MACHINE !!!

But how dows that work ?

First we make the business rules as a form of object

And for this example i will make use of the best practices for typing, validation, 
dependency injection etc...
'''

from data_classes import BusinessRulesFormat
from typing import List


business_rules: List[BusinessRulesFormat] = [
    {'source': 'Waiting payment validation', 'destination': 'Payment confirmed'}, 
    {'source': 'Waiting payment validation', 'destination': 'Payment denied'}, 
    {'source': 'Payment expired', 'destination': 'Payment issued'},
    {'source': 'Payment denied', 'destination': 'Payment issued'}
]

'''
Ok, rules implemented folowing the `BusinessRulesFormat` interface.
Now we will have to make the state machine.

How does it work, it isolates the states of the object you want to analyze and 
check its permissions.

So doesnt matter for it if you have a thousand business rules, it will take care of only
the rule you ordered and the validations for that rule.
'''

'''
So the machine will be built, and for that we only need on the generic machine, one 
function, check if the rule you are trying to apply, its valid.

And of course receive the information necessary for that checking happen.
'''

class StateMachine_V1:
    def __init__(self, business_rules: List[BusinessRulesFormat]):
        self._business_rules = business_rules

    def _validate_transition(self, current_state: str, destination_state: str, ) -> bool:
        '''
        Check if the desired state and the current state, 
        match within any of the business rules
        '''
        return any(
            [   
                rule['destination'] == destination_state and
                rule['source'] == current_state 
                for rule in self._business_rules
            ]
        )

'''
Ok our machine is built.

Notice that it works really simple and only for the scope it will be injected into

The generic machine doesnt need to know any of our business rules, it just need 
to process what being thwron at it

Now we need to inherith that into the State Machine specific for our aplication, 
in this case our Customer

But first lets create our customer.
'''

class Customer_V2:
    def __init__(self):
        pass




class CustomerStateMachine_V1:
    def __init__(
        self, 
        state: str, 
    ):
        self._state = state
        super().__init__()

    def _can_transition(self, destination: str):
        return any(
            [rule['destination'] == destination and
             rule['source'] == self._state for 
             rule in self._business_rules
            ]
        )

    
class VideoStateMachine(StateMachine):
    def _tocar(self):
        if self._can_transition('tocando'):
            self._state = 'tocando'
            print('Tocando...')
            return

        raise Exception

    def _pausar(self):
        if self._can_transition('pausado'):
            self._state = 'tocando'
            print('Pausado...')
            return

        raise Exception


initial_state = 'pausado'


business_rules = [
    {
    'source': 'pausado',
    'destination': 'tocando',
    },
    {    
    'source': 'tocando',
    'destination': 'pausado',
    }
]


state = VideoStateMachine(initial_state, business_rules)
state._tocar()
