
def char_frequency(string):
    text_no_spaces = string.replace(" ", "")
    count = {}
    for char in text_no_spaces.lower():
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count
    

# List of test cases
test_cases = [
    # Test Case 1
    {
        "input_str": "Hello World",
        "expected_output": {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    },
    # Test Case 2
    {
        "input_str": "The quick brown fox jumps over the lazy dog",
        "expected_output": {'t': 2, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}

    },
    # Continue adding all other test cases up to Test Case 20
    # ... (Test Cases 3 to 20)
    {
        "input_str": "12345 67890",
        "expected_output": {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}
    },
    {
        "input_str": "!@#$%^&*()_+",
        "expected_output": {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1, '_': 1,
                            '+': 1}
    },
    {
        "input_str": "aaAAaa",
        "expected_output": {'a': 6}
    },
    {
        "input_str": "",
        "expected_output": {}
    },
    {
        "input_str": "Python is fun!",
        "expected_output": {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 2, 'i': 1, 's': 1, 'f': 1, 'u': 1, '!': 1}
    },
    {
        "input_str": "   Spaces   Everywhere   ",
        "expected_output": {'s': 2, 'p': 1, 'a': 1, 'c': 1, 'e': 5, 'v': 1, 'r': 2, 'y': 1, 'w': 1, 'h': 1}
    },
    {
        "input_str": "Case Insensitive CASE insensitive",
        "expected_output": {'c': 2, 'a': 2, 's': 6, 'e': 6, 'i': 6, 'n': 4, 't': 2, 'v': 2}
    },
    {
        "input_str": "123abcABC!@#",
        "expected_output": {'1': 1, '2': 1, '3': 1, 'a': 2, 'b': 2, 'c': 2, '!': 1, '@': 1, '#': 1}
    },
    {
        "input_str": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "expected_output": {'l': 3, 'o': 4, 'r': 3, 'e': 5, 'm': 3, 'i': 6, 'p': 2, 's': 4, 'u': 2, 'd': 2, 't': 5, 'a': 2, ',': 1, 'c': 3, 'n': 2, 'g': 1, '.': 1}
    },
    {
        "input_str": "Numbers: one, two, three, four, five.",
        "expected_output": {'n': 2, 'u': 2, 'm': 1, 'b': 1, 'e': 5, 'r': 3, 's': 1, ':': 1, 'o': 3, ',': 4, 't': 2, 'w': 1, 'h': 1, 'f': 2, 'i': 1, 'v': 1, '.': 1}
    },
    {
        "input_str": "Repeated letters!!!",
        "expected_output": {'r': 2, 'e': 5, 'p': 1, 'a': 1, 't': 3, 'd': 1, 'l': 1, 's': 1, '!': 3}
    },
    {
        "input_str": "Palindromes are fun: racecar, level, rotor.",
        "expected_output": {'p': 1, 'a': 4, 'l': 3, 'i': 1, 'n': 2, 'd': 1, 'r': 6, 'o': 3, 'm': 1, 'e': 5, 's': 1, 'f': 1, 'u': 1, ':': 1, 'c': 2, ',': 2, 'v': 1, 't': 1, '.': 1}
    },
    {
        "input_str": "Mix of UPPER and lower CASE letters.",
        "expected_output": {'m': 1, 'i': 1, 'x': 1, 'o': 2, 'f': 1, 'u': 1, 'p': 2, 'e': 5, 'r': 3, 'a': 2, 'n': 1, 'd': 1, 'l': 2, 'w': 1, 'c': 1, 's': 2, 't': 2, '.': 1}
    },
    {
        "input_str": "Special characters: ~`!@#$%^&*()-_=+[]{}|;:',<.>/?",
        "expected_output": {'s': 2, 'p': 1, 'e': 2, 'c': 3, 'i': 1, 'a': 3, 'l': 1, 'h': 1, 'r': 2, 't': 1, ':': 2, '~': 1, '`': 1, '!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1, '-': 1, '_': 1, '=': 1, '+': 1, '[': 1, ']': 1, '{': 1, '}': 1, '|': 1, ';': 1, "'": 1, ',': 1, '<': 1, '.': 1, '>': 1, '/': 1, '?': 1}

    },
    {
        "input_str": "1234567890!@#$%^&*()_+",
        "expected_output": {
            '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1,
            '!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1,
            '_': 1, '+': 1
        }
    },
    {
        "input_str": "New\nLine\nCharacters",
        "expected_output": {'n': 2, 'e': 3, 'w': 1, '\n': 2, 'l': 1, 'i': 1, 'c': 2, 'h': 1, 'a': 2, 'r': 2, 't': 1, 's': 1}
    },
    {
        "input_str": "Tabs\tand\tSpaces",
        "expected_output": {'t': 1, 'a': 3, 'b': 1, 's': 3, '\t': 2, 'n': 1, 'd': 1, 'p': 1, 'c': 1, 'e': 1}
    },
    {
        "input_str": "Emoji 😊 test 😊",
        "expected_output": {
            'e': 2, 'm': 1, 'o': 1, 'j': 1, 'i': 1, 't': 2, 's': 1, '😊': 2
        }
    }
]

# Initialize counters and a list to hold failed test cases
passed_tests = 0
failed_tests = 0
failed_test_cases = []

# Run test cases
for idx, test_case in enumerate(test_cases, 1):
    input_str = test_case["input_str"]
    expected_output = test_case["expected_output"]

    try:
        output = char_frequency(input_str)
        assert output == expected_output, (
            f"Expected: {expected_output}\nGot: {output}"
        )
        print(f"Test Case {idx} passed!")
        passed_tests += 1
    except AssertionError as e:
        print(f"Test Case {idx} failed for input: {input_str}\n{e}\n")
        failed_tests += 1
        failed_test_cases.append({
            "Test Case": idx,
            "Input": input_str,
            "Expected": expected_output,
            "Got": output
        })
    except Exception as e:
        print(f"Test Case {idx} encountered an error: {e}\n")
        failed_tests += 1
        failed_test_cases.append({
            "Test Case": idx,
            "Input": input_str,
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