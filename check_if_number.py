def test_if_number(x):
    try:
        return int(x)
    except ValueError:
        print("Invalid number: " + x)


test_if_number('345345345')
test_if_number('+')
test_if_number('abc')
test_if_number(12)
