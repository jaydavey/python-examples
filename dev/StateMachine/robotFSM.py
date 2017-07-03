# to use this class
#>>> python3
#>>> from robotFSM import MobileNest
#>>> koala = MobileNest("Koala")
#>>> koala.state
#'waiting_for_trajectory'
#>>> koala.received_trajectory()
#>>> koala.state
#'navigating_trajectory'

# for more info: https://github.com/pytransitions/transitions

import sys
sys.path += ['/home/jay/python/python-examples/dev/StateMachine', '/home/jay/python/transitions']
from transitions import Machine
import random

class MobileNest(object):

    # Define some states. 
    states = ['charging', 'waiting_for_trajectory', 'navigating_trajectory', 'scheduling_re-charge_stop']

    def __init__(self, name):

        # MobileNest name. Can be literally anything that's unique. An ID string, some animal
        self.name = name

        # How many deliveries have we done?
        self.deliveries = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=MobileNest.states, initial='waiting_for_trajectory')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # A)  At some point, every mobile nest should reach the end of it's trajectory and we will begin waiting for a new trajectory
        self.machine.add_transition(trigger='reached_end_of_trajectory', source='navigating_trajectory', dest='waiting_for_trajectory', after='update_deliveries')

        # B)  At some point, every waiting nest will receive a new trajectory to begin navigating
        self.machine.add_transition(trigger='received_trajectory', source='waiting_for_trajectory', dest='navigating_trajectory')
        
        # X)  At some point, every mobile nest will have fully recharged it's batteries
        self.machine.add_transition(trigger='fully_charged', source='charging', dest='waiting_for_trajectory')

        # Y)  At some point, every mobile nest will need to be sent home to recharge it's batteries
        self.machine.add_transition(trigger='battery_depleted', source='*', dest='scheduling_re-charge_stop')
        
        # LB) At some point, every mobile nest will be scheduled to recharge it's batteries
        self.machine.add_transition(trigger='recharge_scheduled', source='scheduling_re-charge_stop', dest='navigating_trajectory')

        # RB) At some point, every mobile nest reach a recharge station
        self.machine.add_transition(trigger='reached_charging_station', source='navigating_trajectory', dest='charging')

    def update_deliveries(self):
        '''Update delivery counter'''
        self.deliveries += 1

    def low_batt(self):
        """ Basically a coin toss for now.  later we will read the batt level. """
        return random.random() < 0.5

