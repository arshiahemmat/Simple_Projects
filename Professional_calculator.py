from datetime import datetime
import math


class user:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return 'name of user is : {} and the current time is : {}'.format(self.name, current_time)


class history(user):
    def __init__(self, name):
        user.__init__(self, name)
        self.__hist = list()

    def add(self, task):
        self.__hist.append(task)

    def show_list(self):
        counter = 1
        for each in self.__hist:
            print('Operation number {} : {}'.format(counter, each))
            counter += 1

    def __str__(self):
        return user.__str__(self)

    def __len__(self):
        return 'number of operation which save in history is {}'.format(len(self.__hist))


def trigonometric():
    action1 = int(input('for calculate sin, enter 1\nfor calculate cos, enter 2\nfor calculate tan, enter 3\nfor '
                        'calculate cot, enter 4\nfor hypotenuse enter 5\nfor convert argument value from radians to '
                        'degrees, enter 6\nfor convert argument value from degrees to radians, enter 7\n'))
    if action1 == 1:
        num = int(input('Please enter your number\n'))
        print(math.sin(num))
    if action1 == 2:
        num = int(input('Please enter your number\n'))
        print(math.cos(num))
    if action1 == 3:
        num = int(input('Please enter your number\n'))
        print(math.tan(num))
    if action1 == 4:
        num = int(input('Please enter your number\n'))
        print(1 / math.tan(num))
    if action1 == 5:
        num1, num2 = int(input('Please enter your number\n'))
        print(math.hypot(num1, num2))
    if action1 == 6:
        num = int(input('Please enter your radians\n'))
        print(math.degrees(num))
    if action1 == 7:
        num = int(input('Please enter your degrees\n'))
        print(math.radians(num))


def weighted_average_m1(distribution, weights):
    numerator = sum([distribution[i] * weights[i] for i in range(len(distribution))])
    denominator = sum(weights)

    return round(numerator / denominator, 2)


def Average(lst):
    return sum(lst) / len(lst)


def median(a):
    a.sort()
    if len(a) / 2 != int:
        return a[len(a) / 2]
    else:
        return (a[len(a) / 2] + a[(len(a) / 2) - 1]) / 2


def index(expr):
    o_list = list()
    c_list = list()
    for each in range(len(expr)):
        if expr[each] == '(':
            o_list.append(each)
        elif expr[each] == ')':
            c_list.append(each)
    return o_list, c_list


def find_Priority(expr, start=0, end=None):
    s_list = list()
    mi_list = list()
    m_list = list()
    t_list = list()
    if start == 0 and end is None:
        for each in range(len(expr)):
            if expr[each] == '^':
                t_list.append(each)
            elif expr[each] == '*':
                m_list.append(each)
            elif expr[each] == '+':
                s_list.append(each)
            elif expr[each] == '-' and expr[each - 1].isdigit() and expr[each + 1].isdigit():
                mi_list.append(each)
    else:
        for each in range(int(start), int(end)):
            if expr[each] == '^':
                t_list.append(each)
            elif expr[each] == '*':
                m_list.append(each)
            elif expr[each] == '+':
                s_list.append(each)
            elif expr[each] == '-' and expr[each - 1].isdigit() and expr[each + 1].isdigit():
                mi_list.append(each)
    return s_list, mi_list, m_list, t_list


def define(firstNumber, secondNumber, op):
    if op == "+":
        return firstNumber + secondNumber
    elif op == "-":
        return firstNumber - secondNumber
    elif op == "*":
        return firstNumber * secondNumber
    elif op == "/":
        return firstNumber / secondNumber
    elif op == "^":
        return firstNumber ** secondNumber


def split_num(expr, index):
    f = ''
    s = ''
    fi = index
    si = index
    flagf = False
    flags = False
    # print('index is : {}'.format(index))
    for i in range(index - 1, -1, -1):
        if expr[i].isdigit():
            f += expr[i]
            fi -= 1
        else:
            if expr[i] == '-':
                f += expr[i]
                flagf = True
                fi -= 1
            break
    # print('f is : {}'.format(f))
    if expr[index + 1] == '-':
        s += '-'
        flags = True
        si += 1
        for i in range(index + 2, len(expr)):
            if expr[i].isdigit():
                s += expr[i]
                si += 1
            else:
                break
    else:
        for i in range(index + 1, len(expr)):
            if expr[i].isdigit():
                s += expr[i]
                si += 1
            else:
                break
    # print('s is : {}'.format(s))
    # print(fi, si)
    f = f[::-1]
    return f, s, fi, si, flagf, flags


def solve(sub, expr):
    s, mi, m, t = find_Priority(sub)
    real = len(mi)
    # print('real is " {}'.format(real))
    while True:
        s, mi, m, t = find_Priority(sub)
        if len(t) <= 0:
            break
        op = '^'
        fNumber, sNumber, fi, si, flagf, flags = split_num(sub, t[0])
        # print('test : ' + fNumber, sNumber, fi, si)
        fNumber = int(fNumber)
        sNumber = int(sNumber)
        # print('second test : ', fNumber, sNumber, fi, si)
        fi = int(fi)
        si = int(si)
        res = define(fNumber, sNumber, op)
        if res > 0 and flags:
            res = '+' + str(res)
        sub = sub.replace(sub[fi:si + 1], str(res))
    # print(sub)
    while True:
        s, mi, m, t = find_Priority(sub)
        if len(m) <= 0:
            break
        op = '*'
        fNumber, sNumber, fi, si, flagf, flags = split_num(sub, m[0])
        fNumber = int(fNumber)
        sNumber = int(sNumber)
        fi = int(fi)
        si = int(si)
        res = define(fNumber, sNumber, op)
        if res > 0 and flags:
            res = str(res) + '+'
        sub = sub.replace(sub[fi:si + 1], str(res))
        # print(fNumber, sNumber, res)
        # print('zarb : ' + sub)
    while True:
        s, mi, m, t = find_Priority(sub)
        if len(s) <= 0:
            break
        op = '+'
        fNumber, sNumber, fi, si, flagf, flags = split_num(sub, s[0])
        fNumber = int(fNumber)
        sNumber = int(sNumber)
        fi = int(fi)
        si = int(si)
        res = define(fNumber, sNumber, op)
        if res > 0 and flags:
            res = str(res) + '+'
        sub = sub.replace(sub[fi:si + 1], str(res))
        # print('jam : ' + sub)
    while True:
        s, mi, m, t = find_Priority(sub)
        if real <= 0:
            break
        op = '-'
        fNumber, sNumber, fi, si, flagf, flags = split_num(sub, mi[0])
        fNumber = int(fNumber)
        sNumber = int(sNumber)
        fi = int(fi)
        si = int(si)
        res = define(fNumber, sNumber, op)
        if res > 0 and flags:
            res = str(res) + '+'
        sub = sub.replace(sub[fi:si + 1], str(res))
        real -= 1
    sub = sub.replace('(', '')
    sub = sub.replace(')', '')
    # print(sub)
    return sub


name = input("Welcome to Calculator...\nplease enter your name...\n")
calc_user = history(name)
while True:
    action = int(input('If you want to do a new calculation, enter 1, otherwise enter zero to exit.\n'))
    if action == 1:
        act = int(input('for do a new of calculation, enter 1\nfor Calculate trigonometric ratios, enter 2\nfor '
                        'Calculate the average of List, enter 3\nfor Calculate the Weighted average of List, enter 4\n'
                        'for Calculate the median, enter 5\nShow History of calculation, enter 6\nfor user information,'
                        ' enter 7\n'))
        if act == 1:
            calc = input('please enter new List of calculation ... \n')
            calc = calc.replace(' ', '')
            if calc.find('(') != -1:
                while True:
                    first, last = index(calc)
                    if len(first) <= 0:
                        break
                    sub_calc = calc[first[0]:last[0] + 1]
                    # print('sub calc is :' + sub_calc)
                    sub_res = solve(sub_calc, calc)
                    calc = calc.replace(calc[first[0]:last[0] + 1], sub_res)
                    first.pop(0), last.pop(0)
                calc = '(' + calc + ')'
                final_res = solve(calc, calc)
                print('The result of your calculation is : {} \t:)))\n\n\n'.format(final_res))
                calc_user.add(calc)
            else:
                while True:
                    first, last = index(calc)
                    if len(first) <= 0:
                        break
                    sub_calc = calc[first[0]:last[0] + 1]
                    # print('sub calc is :' + sub_calc)
                    sub_res = solve(sub_calc, calc)
                    calc = calc.replace(calc[first[0]:last[0] + 1], sub_res)
                    first.pop(0), last.pop(0)
                calc = '(' + calc + ')'
                final_res = solve(calc, calc)
                print('The result of your calculation is : {} \t:)))\n\n\n'.format(final_res))
                calc_user.add(calc)
        elif act == 2:
            trigonometric()
            calc_user.add('calculate trigonometric')
        elif act == 3:
            av = input('please enter your numbers...\ne.g:2 4 5 3 63 24 52\n')
            newList = av.split()
            newList = [int(i) for i in newList]
            print(Average(newList))
            calc_user.add('calculate average of {}'.format(newList))
        elif act == 4:
            av = input('please enter your numbers...\ne.g:2 4 5 3 63 24 52\n')
            wi = input('please enter your weights...\ne.g:2 1 3 5 4 6 9 7\n')
            newList = av.split()
            newWeight = wi.split()
            newList = [int(i) for i in newList]
            newWeight = [int(i) for i in newWeight]
            print(weighted_average_m1(newList, newWeight))
            calc_user.add('calculate weighted average of {}'.format(newList))
        elif act == 5:
            av = input('please enter your numbers for calculate median...\ne.g:2 4 5 3 63 24 52\n')
            newList = av.split()
            newList = [int(i) for i in newList]
            print(median(newList))
            calc_user.add('calculate median of {}'.format(newList))
        elif act == 6:
            calc_user.show_list()
        else:
            print(calc_user.__str__())
