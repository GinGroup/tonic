from tonic.parameters import Parameter, ChildParameter


def test_create_child():
    p1 = Parameter(0.0, is_variable=False)

    child = p1 + 3.0
    assert child.value == 3.0
    assert p1 in child.parents
    assert len(child.parents) == 1


def test_create_child_multiple_parent():
    p1 = Parameter(0.0, is_variable=False)
    p2 = Parameter(1.0)
    p3 = Parameter(2.0)

    child = p1 * p2 + p3 / (p1 + 1.0)
    assert child.value == 2.0
    assert p1 in child.parents
    assert p2 in child.parents
    assert p3 in child.parents

    assert len(child.parents) == 3


def test_child_of_child():
    p1 = Parameter(0.0, is_variable=False)

    child1 = p1 + 3.0
    child2 = child1 * 2.0

    assert child2.value == 6.0

    assert p1 in child2.parents
    assert len(child1.parents) == 1
    assert len(child2.parents) == 1

    assert child1 in p1.children
    assert child2 in p1.children
    assert len(p1.children) == 2


def test_children_w_many_parents():
    p1 = Parameter(0.0, is_variable=False)
    p2 = Parameter(1.0)
    p3 = Parameter(2.0)

    child1 = p1 * p2
    child2 = child1 / p3
    assert child1 in p1.children
    assert child2 in p1.children
    assert len(p1.children) == 2

    assert child1 in p2.children
    assert child2 in p2.children
    assert len(p2.children) == 2

    assert child1 not in p3.children
    assert child2 in p3.children
    assert len(p3.children) == 1
