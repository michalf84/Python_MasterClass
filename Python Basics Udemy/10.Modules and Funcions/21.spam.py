def spam1():

    def spam2():

        def spam3():
            z="even"
            z+=y
            print("in spam3 loacls are {}".format(locals()))
            return z
        y=" more " + x
        y += spam3()
        print("in spam 2 localas are {}".format(locals()))
        return y

    x="spam*" #+spam2() that will reject because we refer to non initated value
    x+=spam2()
    print("in spam 1 locals are {}".format(locals()))
    return x
print(spam1())
print()
print(locals())
print(globals())