x = 10
y = 20
def printN():
    def calc():
        global x
        x *= 10
        y = 200

    calc()
    print(x,y)

if __name__ == '__main__':
    print(x,y)
    printN()