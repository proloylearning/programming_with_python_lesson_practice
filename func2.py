def addition(num1, num2):
    answer = num1 + num2
    return answer


x = addition(5, 6)
print('Addition:', x)


def website(font='San Serif', bg='white', font_color='black', font_size=11):
    print('Font:', font)
    print('Background:', bg)
    print('Font Color:', font_color)
    print('Font Size:', font_size)


website(bg='grey')

x = 6


def example1():
    z = 5
    print('example1-x:', x)
    print('example1-z:', z)


example1()


def example2():
    z = 5
    y = x + 1
    print('example2-z:', z)
    print('example2-y:', y)


example2()


def example3():
    z = 5
    y = x + 1
    print('example3-z:', z)
    print('example3-y:', y)
    return y


x = example3()
print('new value of x:', x)


def example4():
    global x
    x += 1
    print('example4-x:', x)


example4()
