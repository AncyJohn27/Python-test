def separate_even_odd(lists):
    
    even = set()
    odd =  set()
    for x in lists:
        if x % 2 == 0:
            even.add(x)
        else:
            odd.add(x)
    return even, odd     

test_cases = [
   
    {
        "input_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "expected_output": ({2, 4, 6, 8, 10}, {1, 3, 5, 7, 9})
    },
    
    {
        "input_list": [2, 4, 6, 8, 10],
        "expected_output": ({2, 4, 6, 8, 10}, set())
    },
   
    {
        "input_list": [1, 3, 5, 7, 9],
        "expected_output": (set(), {1, 3, 5, 7, 9})
    },
   
    {
        "input_list": [],
        "expected_output": (set(), set())
    },
   
    {
        "input_list": [0, 1, 2, 3, 4, 5],
        "expected_output": ({0, 2, 4}, {1, 3, 5})
    },
  
    {
        "input_list": [10, 10, 20, 20, 30, 30],
        "expected_output": ({10, 20, 30}, set())
    },
   
    {
        "input_list": [11, 11, 13, 13, 15, 15],
        "expected_output": (set(), {11, 13, 15})
    },
    
    {
        "input_list": [-2, -4, -6, -8],
        "expected_output": ({-8, -6, -4, -2}, set())
    },
 
    {
        "input_list": [-1, -3, -5, -7],
        "expected_output": (set(), {-7, -5, -3, -1})
    },
    
    {
        "input_list": [-10, -5, 0, 5, 10],
        "expected_output": ({-10, 0, 10}, {-5, 5})
    },
   
    {
        "input_list": [1, 2, 2, 3, 3, 4, 4, 5],
        "expected_output": ({2, 4}, {1, 3, 5})
    },
   
    {
        "input_list": [1000000, 999999, 1000000, 999999],
        "expected_output": ({1000000}, {999999})
    },
   
    {
        "input_list": [0],
        "expected_output": ({0}, set())
    },
    
    {
        "input_list": [1],
        "expected_output": (set(), {1})
    },
   
    {
        "input_list": [2],
        "expected_output": ({2}, set())
    },
   
    {
        "input_list": [-100, -50, 0, 50, 100],
        "expected_output": ({0, 100, -100, -50, 50}, set())
    },
    
    {
        "input_list": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
        "expected_output": (set(), {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21})
    },

    {
        "input_list": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        "expected_output": ({2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, set())
    },
    {
        "input_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "expected_output": ({2, 4, 6, 8, 10, 12}, {1, 3, 5, 7, 9, 11})
    },
    {
        "input_list": [0, -1, -2, -3, -4, -5],
        "expected_output": ({0, -4, -2}, {-5, -3, -1})
    }
]

passed_tests = 0
failed_tests = 0
failed_test_cases = []

for idx, test_case in enumerate(test_cases, 1):
    input_list = test_case["input_list"]
    expected_output = test_case["expected_output"]

    try:
        output = separate_even_odd(input_list)
        assert output == expected_output, (
            f"Expected: {expected_output}\nGot: {output}"
        )
        print(f"Test Case {idx} passed!")
        passed_tests += 1
    except AssertionError as e:
        print(f"Test Case {idx} failed for input: {input_list}\n{e}\n")
        failed_tests += 1
        failed_test_cases.append({
            "Test Case": idx,
            "Input": input_list,
            "Expected": expected_output,
            "Got": output
        })
    except Exception as e:
        print(f"Test Case {idx} encountered an error: {e}\n")
        failed_tests += 1
        failed_test_cases.append({
            "Test Case": idx,
            "Input": input_list,
            "Error": str(e)
        })

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