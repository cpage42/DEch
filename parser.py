import sys
import os
import re
from sympy import Symbol, Function, Eq, Derivative
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def parse_math(eq_str, is_diff_eq=True):
    # 1. Define symbols (Swapped 'x' for 't')
    t = Symbol('t')
    y = Function('y')(t)
    
    # 2. Clean up spaces
    eq_str = eq_str.replace(" ", "")
    
    # 3. Handle Derivative notation if it's the differential equation
    if is_diff_eq:
        # Changed regex to look for dt instead of dx
        eq_str = re.sub(r"d\^?2y/dt\^?2", "Derivative(y,t,2)", eq_str)
        eq_str = re.sub(r"dy/dt", "Derivative(y,t)", eq_str)
        # Primes still work the same, but translate to derivatives with respect to t
        eq_str = re.sub(r"y''", "Derivative(y,t,2)", eq_str)
        eq_str = re.sub(r"y'", "Derivative(y,t)", eq_str)
    
    # 4. Split into Left and Right Hand Sides
    if '=' in eq_str:
        lhs_str, rhs_str = eq_str.split('=', 1)
    else:
        lhs_str, rhs_str = eq_str, "0"
        
    # 5. Setup transformations (enables "2t" -> "2*t")
    transformations = (standard_transformations + (implicit_multiplication_application,))
    
    # Update dictionary to use 't'
    local_dict = {'t': t, 'y': y, 'Derivative': Derivative}
    
    # 6. Parse both sides
    lhs = parse_expr(lhs_str, local_dict=local_dict, transformations=transformations)
    rhs = parse_expr(rhs_str, local_dict=local_dict, transformations=transformations)
    
    return Eq(lhs, rhs)

if __name__ == "__main__":
    # Ensure two inputs were provided
    if len(sys.argv) < 3:
        print("Error: Please provide both a differential equation and a proposed solution.")
        sys.exit(1)
        
    diff_eq_input = sys.argv[1]
    proposed_sol_input = sys.argv[2]
    
    try:
        # Parse inputs
        parsed_de = parse_math(diff_eq_input, is_diff_eq=True)
        parsed_prop = parse_math(proposed_sol_input, is_diff_eq=False)
        
        # Define output directory based on your path
        output_dir = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(output_dir, exist_ok=True)
        
        # Write SymPy syntax to text files
        with open(os.path.join(output_dir, "def.txt"), "w") as f:
            f.write(str(parsed_de))
            
        with open(os.path.join(output_dir, "prop.txt"), "w") as f:
            f.write(str(parsed_prop))
            
        # print("Success: Parsed equations written to def.txt and prop.txt")
        
    except Exception as e:
        print(f"Error parsing equations: {e}")