import pygame
from agent import Agent

class MyAgent(Agent):
    """
        Compute the action to perfom on the current state
        of the game. The must be compute in at most time_left
        seconds.

        state: the current state
        time_left: the number of second left

    """

    def __init__(self):
        self.id = None

    def get_action(self, state, last_action, time_left):
        pass

    def get_name(self):
        return 'student agent'

    """
    Set the id of the agent in the game. In a two player 
    game it will be either 0 if we play first of 1 otherwise.
    """

    def set_id(self, id):
        self.id = id