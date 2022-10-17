import random
import logging
from typing import Callable
from gx_utils import *

logging.getLogger().setLevel(logging.INFO)

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

class State:
    def __init__(self, data : tuple):
        self._data = data
        logging.debug(f"Data: {self._data}")

    def __hash__(self):
        return hash(self._data)

    def __eq__(self, other):
        return self._data == other._data

    def __lt__(self, other):
        return self._data < other._data

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        length = 0
        for i in self._data:
            length += len(i)
        return length

    def nodes(self):
        return len(self._data)

    def coverage(self):
        tuple_set = set()
        for i in self._data:
            tuple_set |= set(i)
        return len(tuple_set)

    @property
    def data(self):
        return self._data

    def copy_data(self):
        return self._data.copy()

def search(
    initial_state: State,
    goal_test: Callable,
    goal_length: int,
    priority_function: Callable,
    unit_cost: Callable,
    lists: list,
):
    frontier = PriorityQueue()
    nodes = 0

    state = initial_state
    logging.debug(f"{initial_state}")

    while state is not None and not goal_test(state, goal_length):
        actions = possible_actions(state, lists=lists)
        logging.debug(f"Possible actions: {actions}")
        for a in actions:
            new_state = result(state, a)
            cost = unit_cost(a)
            p=priority_function(new_state)
            frontier.push(new_state, p)
            logging.debug(f"Added new node to frontier (cost={cost}, priority={p})")
        if frontier:
            state = frontier.pop()
            nodes += 1
        else:
            state = None

    path = state
    
    logging.info(f"Solved N={N} with w={len(path):,} (bloat={((len(path)-N)*100)//N}%) // nodes={nodes:,}")
    logging.debug(f"Path: {path}")
    return path

def goal_test(state: State, goal_length: int):
    coverage = state.coverage()
    logging.debug(f"{coverage}")
    return coverage == goal_length

def possible_actions(state: State, lists: list):
    return set(tuple(i) for i in lists) - set(state.data)

def result(state: State, new_tuple):
    new_data = list(state.data)
    new_data.append(new_tuple)
    return State(tuple(new_data))

def h(state : State):
    return -state.coverage()

for N, k in zip([5, 10, 20, 100, 500, 1000], [1.1, 1.1, 1.1, 4, 15, 30]):
    GOAL = set(range(N))
    logging.info(f"Goal:\n{GOAL}")

    parent_state = dict()
    state_cost = dict()
    possible_lists = problem(N, seed=42)

    final = search(
        State(tuple(())),
        goal_test=goal_test,
        goal_length=N,
        priority_function=lambda s: len(s) + k*h(s),  # we want to prioritize the coverage of the solution over its length
        unit_cost=lambda a: len(a),
        lists=possible_lists
    )