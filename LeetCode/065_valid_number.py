class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool

        beats 47.82%
        """
        #define a DFA
        state = [{},
              {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
              {'digit': 3, '.': 4},
              {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
              {'digit': 5},
              {'digit': 5, 'e': 6, 'blank': 9},
              {'sign': 7, 'digit': 8},
              {'digit': 8},
              {'digit': 8, 'blank': 9},
              {'blank': 9}]
        current_state = 1
        for c in s:
            if '0' <= c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[current_state].keys():
                return False
            current_state = state[current_state][c]
        if current_state not in [3, 5, 8, 9]:
            return False
        return True
