#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    calc.add.a = 10
    calc.add.b = 5
    sm = calc.add(calc.add.a, calc.add.b)
    print("{} + {} = {}".format(calc.add.a, calc.add.b, sm))

    calc.sub.a = 10
    calc.sub.b = 5
    diff = calc.sub(calc.sub.a, calc.sub.b)
    print("{} - {} = {}".format(calc.sub.a, calc.sub.b, diff))

    calc.mul.a = 10
    calc.mul.b = 5
    prd = calc.mul(calc.mul.a, calc.mul.b)
    print("{} * {} = {}".format(calc.mul.a, calc.mul.b, prd))

    calc.div.a = 10
    calc.div.b = 5
    qt = calc.div(calc.div.a, calc.div.b)
    print("{} / {} = {}".format(calc.div.a, calc.div.b, qt))
