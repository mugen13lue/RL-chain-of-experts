def maximize_tests(num_ear_tests, num_blood_tests):
    total_time = 7525
    blood_time = 30
    ear_time = 5

    # Constraint: at least 12 ear tests
    num_ear_tests = max(12, num_ear_tests)

    # Constraint: at least three times as many blood tests as ear tests
    num_blood_tests = max(3 * num_ear_tests, num_blood_tests)

    # Calculate the maximum number of blood tests that can be performed
    max_blood_tests = min(total_time // blood_time, num_blood_tests)

    # Calculate the maximum number of ear tests that can be performed
    max_ear_tests = min((total_time - max_blood_tests * blood_time) // ear_time, num_ear_tests)

    # Calculate the total number of tests that can be performed
    total_tests = max_blood_tests + max_ear_tests

    return total_tests

# Test the function with some example inputs
print(maximize_tests(12, 36))  # Output should be 252