from src.factories.actionfactory import ActionFactory
from src.building_blocks.markovdecisionprocess import MarkovDecisionProcess
from src.building_blocks.state import State

import numpy as np


state_count = 0
states = np.ndarray(state_count, dtype=State)


def test_init():
    mdp = MarkovDecisionProcess(states)
    assert mdp is not None
    assert (state_count, ) == mdp.states.shape
    assert states.all() == mdp.states.all()


def test_add_state():
    mdp = MarkovDecisionProcess(states)
    state = State('state', 0)
    mdp.add_state(state)
    assert (state_count + 1, ) == mdp.states.shape
    assert state == mdp.states[state_count]


def test_print():  # TODO: Test other combinations
    mdp = MarkovDecisionProcess(states)
    state0 = State('state 0', 0)
    state1 = State('state 1', 0)
    state2 = State('state 2', 0)

    action1 = ActionFactory.create_action('action', 5, state1)

    state0.add_action(action1)
    state2.add_action(action1)

    mdp.add_state(state0)
    mdp.add_state(state1)
    mdp.add_state(state2)

    assert 'state 0: 0\n' + \
        'state 1: 0\n' + \
        'state 2: 0\n' == mdp.__repr__()
