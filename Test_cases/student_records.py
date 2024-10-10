def process_student_records(students):
    processed_records = {}

    for student in students:
        top = sorted(student[2], reverse=True)[:3]
        average = sum(top) / len(top)
        if average > 80:
            processed_records[student[0]] = (student[1], average)

    return dict(sorted(processed_records.items()))
    # Remove this line when you add your implementation

# List of test cases
test_cases = [
    # Test Case 1
    {
        "input_students": [
            ('Alice', 20, [85, 90, 95]),
            ('Bob', 22, [70, 75, 80]),
            ('Charlie', 19, [88, 92]),
            ('David', 21, [100, 100, 100, 100])
        ],
        "expected_output": {
            'Alice': (20, 90.0),
            'Charlie': (19, 90.0),
            'David': (21, 100.0)
        }
    },
    # Test Case 2
    {
        "input_students": [
            ('Eve', 23, [82, 79, 84]),
            ('Frank', 20, [78, 76, 80]),
            ('Grace', 22, [95]),
            ('Heidi', 21, [88, 89, 90])
        ],
        "expected_output": {
            'Eve': (23, 81.66666666666667),
            'Grace': (22, 95.0),
            'Heidi': (21, 89.0)
        }
    },
    # Continue adding test cases up to Test Case 20
    # ...
    # Test Case 3
    {
        "input_students": [
            ('Ivan', 20, [60, 65, 70]),
            ('Judy', 19, [85, 87, 90]),
            ('Mallory', 22, [82, 85, 88]),
            ('Niaj', 21, [79, 81, 78])
        ],
        "expected_output": {
            'Judy': (19, 87.33333333333333),
            'Mallory': (22, 85.0)
        }
    },
    # Test Case 4
    {
        "input_students": [],
        "expected_output": {}
    },
    # Continue adding the rest of the test cases...
    # Test Case 5 to Test Case 20
    {
        "input_students": [
            ('Oscar', 23, [100, 100]),
            ('Peggy', 20, [80, 82, 79]),
            ('Quentin', 22, [75, 78, 72]),
            ('Ruth', 21, [85, 88, 90, 92])
        ],
        "expected_output": {
            'Oscar': (23, 100.0),
            'Peggy': (20, 80.33333333333333),
            'Ruth': (21, 90.0)
        }
    },
    # Add the rest of the test cases (Test Case 6 to Test Case 20) here
    # ...
    # Test Case 20
    {
        "input_students": [
            ('Wendy', 19, [88, 90, 92]),
            ('Xavier', 22, [85, 87, 89]),
            ('Yasmine', 20, [95, 93, 94]),
            ('Zane', 21, [78, 80, 82])
        ],
        "expected_output": {
            'Wendy': (19, 90.0),
            'Xavier': (22, 87.0),
            'Yasmine': (20, 94.0)
        }
    }
]

# Initialize counters and a list to hold failed test cases
passed_tests = 0
failed_tests = 0
failed_test_cases = []

# Run test cases
for idx, test_case in enumerate(test_cases, 1):
    input_students = test_case["input_students"]
    expected_output = test_case["expected_output"]

    try:
        output = process_student_records(input_students)
        assert output == expected_output, (
            f"Expected: {expected_output}\nGot: {output}"
        )
        print(f"Test Case {idx} passed!")
        passed_tests += 1
    except AssertionError as e:
        print(f"Test Case {idx} failed for input: {input_students}\n{e}\n")
        failed_tests += 1
        failed_test_cases.append({
            "Test Case": idx,
            "Input": input_students,
            "Expected": expected_output,
            "Got": output
        })
    except Exception as e:
        print(f"Test Case {idx} encountered an error: {e}\n")
        failed_tests += 1
        failed_test_cases.append({
            "Test Case": idx,
            "Input": input_students,
            "Error": str(e)
        })

# Print summary
print("\n=== Test Summary ===")
print(f"Total Tests: {passed_tests + failed_tests}")
print(f"Passed: {passed_tests}")
print(f"Failed: {failed_tests}")

if failed_tests > 0:
    print("\nFailed Test Details:")
    for test in failed_test_cases:
        print(f"Test Case {test['Test Case']} Failed")
        print(f"Input: {test['Input']}")
        if "Error" in test:
            print(f"Error: {test['Error']}\n")
        else:
            print(f"Expected Output: {test['Expected']}")
            print(f"Actual Output: {test['Got']}\n")