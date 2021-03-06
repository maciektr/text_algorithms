from parser import Parser
from nfa import Nfa, State


class Regex:
    def __init__(self, regex, verbose=False):
        if verbose:
            print('Regex:', regex)
        postfix = Parser.parse_regex(regex, verbose)
        if verbose:
            print('Regex in reversed polish notation:', postfix)
        self.nfa = Nfa.from_postfix(postfix)

    def match(self, text: str):
        current_states = self.nfa.start.walk_eps()
        for char in text:
            next_states = []
            for state in current_states:
                if char in state.transitions:
                    next_states.extend(state.transitions[char].walk_eps())
                if Parser.MATCH_ALL_OP in state.transitions:
                    next_states.extend(state.transitions[Parser.MATCH_ALL_OP].walk_eps())
            current_states = next_states

        for state in current_states:
            if state.final:
                return True
        return False
