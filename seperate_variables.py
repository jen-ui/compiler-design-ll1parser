from typing import List, Tuple

def seperate_variables(grammar:List[Tuple[str,List[str]]]):
    non_terminals = [prod_rule[0] for prod_rule in grammar]
    terminals=[]
    tokenized=[]
 
    for prod_rule in grammar:
        
        tokenized = [char for string in prod_rule[1] for char in string]
        for token in tokenized:
            if token not in non_terminals:
                terminals.append(token)
        
        terminals=list(set(terminals))
    
    return [non_terminals,terminals]
        


   
    
if __name__=="__main__":
    grammar = [
    ('S', ['AB', 'BC']),   # S -> AB | BC
    ('A', ['aA', 'a']),    # A -> aA | a
    ('B', ['bB', 'b']),    # B -> bB | b
    ('C', ['cC', 'c'])     # C -> cC | c
]
    seperate_variables(grammar)