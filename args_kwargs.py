def fun(x, y):
	# function with exactly two arguments
	print(x + y)


fun(5, 8)
fun(y=8, x=5)



def f_args(*args):
	print(args)

f_args(23, 1, "text")



def f_kw(**kwargs):
	print(kwargs)

f_kw(a=5, b=564, c=324)



def f_ar_kw(*args, **kwargs):
	print(args)
	print(kwargs)


f_ar_kw(4, 5, 3, 2, k="sdf", x="43", y=3434)
# args: (4, 5, 3, 2)
# kwargs: {'k': 'sdf', 'x': '43', 'y': 3434}
