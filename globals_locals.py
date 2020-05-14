a = 5


def func():
    a = 8
    print(f'a (inside a function): {a}')


func()
print(f'a (globally): {a}')



# -----------
print('--------------')




# b = 4
#
# def func_global():
#
#     global b
#     print(f'b (global, inside a func): {b}')
#     b = 10
#     print(f'b: {b}')
#
# func_global()
# print(f'b (globally): {b}')
#
#
# # -----------
# print('--------------')
#
#
# c = 7
#
#
# def global_inc():
#     print(f'c (inside a function): {c}')
#     #c = c + 1 # we can read, but we can't set new value
#
#
#
# global_inc()
# print(f'c (global): {c}')
