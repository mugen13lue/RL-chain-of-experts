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
    model = gp.Model("teacher_allocation")
    
    # Define decision variables
    staff = model.addVar(vtype=GRB.INTEGER, name="staff")
    substitute = model.addVar(vtype=GRB.INTEGER, name="substitute")
    
    # Set objective function: minimize total number of teachers
    model.setObjective(staff + substitute, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(6 * staff + 3 * substitute >= requires_constraint, "teaching_hours_constraint")
    model.addConstr(300 * staff + 100 * substitute <= budget_constraint, "budget_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the total number of teachers
    total_number_of_teachers = staff.x + substitute.x
    
    return total_number_of_teachers