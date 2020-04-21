

def add(x, y):
    # TODO: dopisz resztę funkcji dodającej 2 liczby, wynik zwróć


def my_format(s):
    s = "*** {} ***".format(s)
    # TODO: dopisz resztę funkcji zwracającej sformatowany tekst


def my_print(s):
    s = "--- {} ---".format(s)
    # TODO: uzupełnij funkcję o wypisywanie sformatowanego tekstu


# ---- testy -----

assert add(1, 1) == 2
assert add(10, 5) == 15

assert add(add(3, 5), add(1, 1)) == 10


assert my_format("test") == "*** test ***"
assert my_format("piękna pogoda") == "*** piękna pogoda ***"


assert my_print("test") is None
assert my_print("piękna pogoda") is None


print("Jeśli widzisz ten tekst, to funkcje zwracają poprawne wartości :)")