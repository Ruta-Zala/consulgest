def test(x,y,z):
    res = ((x+y+z)/3)
    return print("{0:.4f}".format(res))

x=3.44
y=3.25
z=9.34
test(x,y,z)


def prova():
    print("ciao")

    assert True


prova()
