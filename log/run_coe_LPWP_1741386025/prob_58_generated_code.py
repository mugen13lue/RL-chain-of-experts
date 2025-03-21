def prob_58(x, y, glass_jar_capacity, plastic_jar_capacity, glass_jar_constraint, minimum_glass_jar_count, total_honey_capacity):
    """
    Args:
        x: an integer, representing the number of glass jars filled
        y: an integer, representing the number of plastic jars filled
        glass_jar_capacity: an integer, representing the capacity of a glass jar in ml
        plastic_jar_capacity: an integer, representing the capacity of a plastic jar in ml
        glass_jar_constraint: a string, specifying the constraint on the number of plastic jars in terms of the number of glass jars
        minimum_glass_jar_count: an integer, specifying the minimum number of glass jars to be filled
        total_honey_capacity: an integer, specifying the total capacity of the honey in ml

    Returns:
        objective_value: an integer, representing the maximum number of bottles filled
    """
    from scipy.optimize import linprog

    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[glass_jar_capacity, plastic_jar_capacity], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [total_honey_capacity, -minimum_glass_jar_count, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(20, None))  # Solving the linear programming problem

    return res.fun * -1  # Return the negative of the objective value to maximize the total number of jars filled