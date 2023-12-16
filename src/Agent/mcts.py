import os
import sys
sys.path.append(".")

from copy import deepcopy
import random
import numpy as np

class Node():
    def __init__(self, state, parent=None):
        self.node_state = state
        self.parent = parent
        self.value = 0 #wins
        self.visits = 0
        self.children = {}
        
    def update_children(self):
        
        def _add_child(child_state_action):
            child = Node(child_state_action[0], self)
            self.children[str(child_state_action[1])] = child

        legal_moves = self.node_state.get_legal_moves()
        for move in legal_moves:
            state_copy = deepcopy(self.node_state)
            state_copy.make_move(move[0], move[1])
            _add_child((state_copy, move))

    def get_ucb_score(self, c=2**0.5):
        if ((self.parent) and (self.visits>0)):
            return self.value/self.visits \
                + c * (np.sqrt\
                        (np.log(self.parent.visits)\
                                /(self.visits))
                       )
        else:
            return 0
        
    def get_best_child(self):
        best_action = None
        best_child = None
        best_child_ucb_score = -1 * float("inf")
        for action, child in self.children.items():
            child_ucb_score = child.get_ucb_score()
            if child_ucb_score > best_child_ucb_score:
                best_child_ucb_score = child_ucb_score
                best_child = child
                best_action = action
        return eval(best_action), best_child
    
    def print_child_scores(self):
        for action, child in self.children.items():
            print(f"{action}: {child.value}/{child.visits}")

    def print_parent_scores(self):
        node_parent = self.parent
        while node_parent is not None:
            print(f"{node_parent}: {node_parent.value}/{node_parent.visits}")
            node_parent = node_parent.parent
            
    def __repr__(self) -> str:
        repr = ""
        for i in np.flipud(self.node_state.game_state):
            repr+=str(i)+"\n"
        return repr
    
class MCTS():
    def __init__(self, initial_node):
        self.initial_node = initial_node

    def select(self):
        if len(self.initial_node.children)==0:
            return self.initial_node
        else:
            _, best_child = self.initial_node.get_best_child()
            return best_child
        
    def expand(self, best_child):
        best_child.update_children()

    def simulate(self, n_iter=1000):
        node = self.initial_node

        for _ in range(n_iter):
            simulatipon_state = deepcopy(node.node_state)
            legal_moves = simulatipon_state.get_legal_moves()
            if legal_moves==[]:
                continue
            first_move = random.choice(legal_moves)
            simulatipon_state.make_move(first_move[0], first_move[1])

            while simulatipon_state.metadata['terminated'] == False:
                move = random.choice(simulatipon_state.get_legal_moves())
                simulatipon_state.make_move(move[0], move[1])

            #Backpropagate
            node.children[str(first_move)].visits+=1
            node.visits+=1
            if simulatipon_state.winner == 1:
                node.children[str(first_move)].value+=1
                node.value+=1    

            node_parent = node.parent
            while node_parent is not None:
                node_parent.visits+=1
                if simulatipon_state.winner == 1:
                    node_parent.value+=1
                node_parent = node_parent.parent

    def main(self):
        best_child = self.select()
        self.expand(best_child)
        self.simulate()