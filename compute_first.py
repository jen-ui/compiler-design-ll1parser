from typing import Dict, List, Set, Tuple
from seperate_variables import seperate_variables 


def compute_first(grammar: List[Tuple[str, List[str]]]) -> Dict[str, Set[str]]:
    """
    Compute the FIRST set for a given grammar.
    
    Args:
        grammar (List[Tuple[str, List[str]]]): The grammar, represented as a list of tuples.
        
    Returns:
        Dict[str, Set[str]]: The FIRST set for each non-terminal.
    """
    # Separate non-terminals and terminals
    separated_variables = seperate_variables(grammar)
    non_terminals, terminals = separated_variables[0], separated_variables[1]
    
    # Initialize FIRST sets for each non-terminal
    FIRST: Dict[str, Set[str]] = {non_terminal: set() for non_terminal in non_terminals}
    
    # Helper function to get FIRST(X) for a symbol X
    def first_of(symbol: str) -> Set[str]:
        if symbol in terminals:
            return {symbol}  # If the symbol is a terminal, return itself
        return FIRST[symbol]  # Otherwise return its FIRST set
    
    # Iteratively compute the FIRST sets
    changed = True
    while changed:
        changed = False
        
        # For each non-terminal and its productions
        for non_terminal, productions in grammar:
            for production in productions:
                # Start with an empty FIRST set for this production
                current_first = set()
                contains_epsilon = True
                
                # Process symbols in the production
                for symbol in production:
                    current_first |= (first_of(symbol) - {'ε'})  # Add FIRST(symbol) without epsilon
                    
                    if 'ε' not in first_of(symbol):  # If no epsilon, stop further processing
                        contains_epsilon = False
                        break
                
                # If all symbols derive epsilon, add epsilon to the FIRST set
                if contains_epsilon:
                    current_first.add('ε')
                
                # Update the FIRST set for the non-terminal if there is a change
                if not current_first.issubset(FIRST[non_terminal]):
                    FIRST[non_terminal] |= current_first
                    changed = True
    
    return FIRST

if __name__=="__main__":
    grammar = [
    ('S', ['AB', 'BC']),   # S -> AB | BC
    ('A', ['aA', 'a']),    # A -> aA | a
    ('B', ['bB', 'b']),    # B -> bB | b
    ('C', ['cC', 'c'])     # C -> cC | c
]
    print(compute_first(grammar))