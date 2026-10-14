
def test_fun_1():
    print("Fun 1")
    assert True


def test_fun_2():
    print("Fun 2")
    assert True



def test_answer(cmdopt):
    if cmdopt == "type1":
        print('First')
    else:
        print("Second")

