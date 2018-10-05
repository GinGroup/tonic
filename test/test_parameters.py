from tonic.parameters import Parameter, ChildParameter

def test_addition_1():
    p1 = Parameter(0., is_variable=False)
    p2 = Parameter(1.)
    assert (p1 + p2 == 1.)
    assert (p1 - p2 == -1.)

def test_child():
    p1 = Parameter(0., is_variable=False)
    p2 = Parameter(1.)

    child = p1 + 3.
    assert(child.value == 3.)
    assert(child.parent == p1)
    assert(child.parent != p2)

def test_child_of_child():
    p1 = Parameter(0., is_variable=False)
    p2 = Parameter(1.)

    child = p1 + 3.

    child2 = child * 2.
    assert(child2.value == 6.)
    assert(child2.parent == p1)