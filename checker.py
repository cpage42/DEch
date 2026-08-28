import os
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

# Define the exact folder path where the text files live
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the independent and dependent variables.
t = sp.symbols('t')
y = sp.Function('y')(t)

# Create a dictionary so the parser knows what 't', 'y', 'Derivative', and 'Eq' mean
local_dict = {'t': t, 'y': y, 'Derivative': sp.Derivative, 'Eq': sp.Eq}

# Read the string files using the absolute path
with open(os.path.join(script_dir, "def.txt"), "r", encoding="utf-8") as file:
    diff_eq_str = file.read()

with open(os.path.join(script_dir, "prop.txt"), "r", encoding="utf-8") as file:
    sol_str = file.read()

# Convert the text strings back into actual SymPy equation objects
diff_eq = parse_expr(diff_eq_str, local_dict=local_dict)
sol = parse_expr(sol_str, local_dict=local_dict)

# Using SymPy's built-in checkodesol is the safest way to check
try:
    is_solution = sp.checkodesol(diff_eq, sol)[0]
    if is_solution:
        print("yes")
    else:
        print("no")
except Exception as e:
    # If it fails to evaluate for some reason
    print("no")