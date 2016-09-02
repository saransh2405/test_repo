class first_class:
	def __init__(self):
		print "constructor"

	def func1(self):
		print "Hello World 1"


def main():
	a = first_class()
	a.func1()


if __name__ == '__main__':
	main()