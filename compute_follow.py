#this code has infinite loop

from typing import Dict, List, Set, Tuple
from compute_first import compute_first
from seperate_variables import seperate_variables


def compute_follow(grammar: List[Tuple[str, List[str]]], first_sets: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """
    Compute the FOLLOW set for a given grammar, assuming FIRST sets are already computed.
    
    Args:
        grammar (List[Tuple[str, List[str]]]): The grammar, represented as a list of tuples.
        first_sets (Dict[str, Set[str]]): The FIRST sets for each non-terminal.
        
    Returns:
        Dict[str, Set[str]]: The FOLLOW set for each non-terminal.
    """
    separated_variables = seperate_variables(grammar)
    non_terminals, terminals = separated_variables[0], separated_variables[1]
    
    # Initialize FOLLOW sets for each non-terminal
    FOLLOW: Dict[str, Set[str]] = {non_terminal: set() for non_terminal in non_terminals}
    
    # FOLLOW of the start symbol includes the end-of-input symbol
    FOLLOW[non_terminals[0]].add('$')
    
    # Helper function to get FOLLOW(X) for a symbol X
    def follow_of(symbol: str) -> Set[str]:
        return FOLLOW[symbol]
    
    # Iteratively compute the FOLLOW sets
    changed = True
    while changed:
        changed = False
        
        # For each non-terminal and its productions
        for non_terminal, productions in grammar:
            for production in productions:
                # Reverse the production to propagate FOLLOW sets from right to left
                for i in range(len(production) - 1):
                    symbol = production[i]
                    next_symbol = production[i + 1]
                    
                    # If the current symbol is a non-terminal
                    if symbol in non_terminals:
                        # Add FIRST(next_symbol) - {ε} to FOLLOW(symbol)
                        FOLLOW[symbol] |= (first_sets.get(next_symbol, set()) - {'ε'})
                        
                        # If next_symbol can derive ε, propagate FOLLOW of the non-terminal
                        if 'ε' in first_sets.get(next_symbol, set()):
                            FOLLOW[symbol] |= follow_of(non_terminal)
                            changed = True
                    
                # If the last symbol in the production is a non-terminal, propagate FOLLOW of the non-terminal
                if production[-1] in non_terminals:
                    FOLLOW[production[-1]] |= follow_of(non_terminal)
                    changed = True
        print("hello")
    return FOLLOW

if __name__=="__main__":
    grammar = [
    ('S', ['AB', 'BC']),   # S -> AB | BC
    ('A', ['aA', 'a']),    # A -> aA | a
    ('B', ['bB', 'b']),    # B -> bB | b
    ('C', ['cC', 'c'])     # C -> cC | c
]
    first_sets=compute_first(grammar)
    print(first_sets)
    print(compute_follow(grammar,first_sets))