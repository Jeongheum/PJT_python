def Calc(currency, *rates):
    for i in rates:
        print(currency*i)

Calc(1, [120, 130])