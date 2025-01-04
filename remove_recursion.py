from typing import List, Tuple

def remove_left_recursion_for_grammar(grammar: List[Tuple[str, List[str]]]) -> List[Tuple[str, List[str]]]:
    updated_grammar = []
    
    for prod_rule in grammar:
        updated_rules = remove_left_recursion(prod_rule)
        updated_grammar.extend(updated_rules)
    
    return updated_grammar

# Your original function (kept as is)
def remove_left_recursion(all_prod_rule: Tuple[str, List[str]]) -> List[Tuple[str, List[str]]]:
    lhs = all_prod_rule[0]
    rhs = all_prod_rule[1]
    
    recursive_part = []
    non_recursive_part = []
    dummy_var = f"{lhs}'"
    
    has_left_recursion = False
    
    for prod_rule in all_prod_rule[1]:
        print(prod_rule)
        if lhs == prod_rule[0]:
            recursive_part.append(prod_rule[1:])
            has_left_recursion = True
        else:
            non_recursive_part.append(prod_rule)
    print(recursive_part, non_recursive_part)
            
    if has_left_recursion:
        # Directly construct the right-hand side of the rules
        first_rule_rhs = [item + dummy_var for item in non_recursive_part]
        second_rule_rhs = [item + dummy_var for item in recursive_part] + ["#"]

        # Create the first and second rules
        first_rule = (lhs, first_rule_rhs)
        second_rule = (dummy_var, second_rule_rhs)
        
        return [first_rule, second_rule]

    return [all_prod_rule]

# Example usage
grammar = [
    ("S", ["ABC"]),
    ("A", ["abA", "ab"]),
    ("B", ["b", "BC"]),
    ("C", ["c", "cC"])
]

updated_grammar = remove_left_recursion_for_grammar(grammar)
print(updated_grammar)