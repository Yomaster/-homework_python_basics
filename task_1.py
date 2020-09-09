from sys import argv

a = argv[1]
b = argv[2]
c = argv[3]


def payroll(productivity, rate, premium):
    return int(productivity) * int(rate) + int(premium)


print(payroll(a, b, c))
