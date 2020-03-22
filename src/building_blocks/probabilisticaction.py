import numpy as np
import random as random
from .action import Action

class ProbabilisticAction:

    def __init__(self, rewards, probabilities, states):
        self.__validate_input(rewards, probabilities, states)  # The state checks is delegated to the state factory
        self.cdf = __create_cdf(probabilities)
        self.__create_derived_actions(rewards, probabilities, states)

    def get_action(self):
         rand = random.uniform(0, 1)
         return self.actions[bisect_left(self.cdf, rand)]

    def __validate_input(self, rewards, probabilities, states): # Todo: add uniqueness of states test?
        self.__validate_rewards(rewards)
        self.__validate_probabilities(probabilities)
        if not rewards.shape == probabilities.shape:
            raise ValueError("Rewards array and probabilities array have different dimensions.")
        if not probabilities.shape == states.shape:
            raise ValueError("Probabilities array and states array have different dimensions.")

    def __validate_rewards(self, rewards):
        if not isinstance(rewards, np.ndarray):
            raise TypeError("Rewards array has to be an ndarray.")
        # https://stackoverflow.com/questions/26921836/correct-way-to-test-for-numpy-dtype
        if not(rewards.dtype in (np.float32, np.float64, np.int8, np.int16, np.int32, np.int64)):
            raise TypeError("The dtype of rewards array has to be an np numerical type.")
        if rewards.size == 0:
            raise ValueError("Rewards array can't be empty.")

    def __validate_probabilities(self, probabilities):
        if not isinstance(probabilities, np.ndarray):
            raise TypeError("Probabilities array has to be an ndarray.")
        if not(probabilities.dtype in (np.float32, np.float64, np.int8, np.int16, np.int32, np.int64)):
            raise TypeError("The dtype of probabilities array has to be an np numerical type.")
        if probabilities.size == 0:
            raise ValueError("Probabilities array can't be empty.")
        if np.sum(probabilities) != 1.0:
            raise ValueError("The sample space probabilities have to sum to 1.0.")

    def __create_derived_actions(self, rewards, probabilities, states):
        self.actions = np.ndarray(rewards.shape[0], dtype=Action)
        self.action = map(__create_action, rewards, probabilities, states)

    def __create_action(reward, probability, state):
        return Action(reward, state, probability)

    def __create_cdf(probabilities):
        return np.cumsum(probabilities)

    def __repr__(self):
        return f'Reward: {self.reward} to state: {self.to.name}.'

    def __repr__(self):
        returned_string = ''
        returned_string += f'Actions included in this ProbabilisticAction:\n'
        for action in self.actions:
            returned_string += repr(action)
        returned_string += '\n'

        return returned_string
