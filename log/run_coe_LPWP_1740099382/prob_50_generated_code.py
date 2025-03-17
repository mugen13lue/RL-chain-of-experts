import gurobipy as gp
from gurobipy import GRB

def prob_50(staff_teachers, substitute_teachers, requires_constraint, budget_constraint):
    """
    Args:
        staff_teachers: an integer, indicating the number of staff teachers
        substitute_teachers: an integer, indicating the number of substitute teachers
        requires_constraint: an integer, indicating the number of teaching availability required
        budget_constraint: an integer, indicating the budget limit
    Returns:
        total_number_of_teachers: an integer, indicating the total number of teachers
    """
    
    # Create a new model
    model = gp.Model("teacher_hiring")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="staff_teachers")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="substitute_teachers")
    
    # Set objective function: minimize total number of teachers
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(6*x + 3*y >= requires_constraint)
    model.addConstr(300*x + 100*y <= budget_constraint)
    
    # Optimize model
    model.optimize()
    
    # Get the total number of teachers
    total_number_of_teachers = model.objVal
    
    return total_number_of_teachers