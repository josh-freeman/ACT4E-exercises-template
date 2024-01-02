from act4e_solutions import MyFinitePosetConstructionPower, MyFiniteSet

def test_MyFinitePosetConstructionPower():
    elements = [1,2]

    p = MyFinitePosetConstructionPower().powerposet(MyFiniteSet(elements))

    assert p.holds([3], [3]), "3 is not in the power set of {1,2}"


if __name__ == '__main__':
    test_MyFinitePosetConstructionPower()