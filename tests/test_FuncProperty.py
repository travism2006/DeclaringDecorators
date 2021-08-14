from DeclaringDecorators.ExtraDecorator import ExtraDecorator


#               Basic testsuite
#           Basic test cases go here


# def test_uppercase():
#     assert "loud noises".upper() == "LOUD NOISES"

def test_decoratorCreated():
    test_inst1 = ExtraDecorator()
    assert test_inst1 is not None


def test_compareTwoDecorators():
    test_inst1 = ExtraDecorator("decorator1")
    test_inst2 = ExtraDecorator("decorator2")
    assert test_inst1 != test_inst2


# test case - a decorator name can be changed
def test_decoratorNameChange():
    test_inst1 = ExtraDecorator()
    test_inst1.decoratorName = "MyDecorator1"
    assert test_inst1.decoratorName is not None
    assert test_inst1.decoratorName != ""

# test case - compare the bits