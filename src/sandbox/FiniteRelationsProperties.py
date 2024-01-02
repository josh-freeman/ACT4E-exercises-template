from act4e_solutions import SolFiniteRelationProperties, MyFiniteSet, MyFiniteRelation
# modify the above imports to suit the names of your FiniteSet and FiniteRelation classes.

def test_MyFiniteRelationProperties():

    # Create finite sets and values
    source_set = MyFiniteSet([1, 2])
    target_set = MyFiniteSet(['a', 'b'])
    values = [[1, 'a'], [2, 'a']]

    # Create an instance of MyFiniteRelation
    fr = MyFiniteRelation(source_set, target_set, values)

    # Check the holds method for different combinations of x and y
    results = [(fr.holds(x, y), x, y) for x in source_set.elements() for y in target_set.elements()]

    print(results, SolFiniteRelationProperties().is_injective(fr))

    assert not SolFiniteRelationProperties().is_injective(fr), f"{results} is not injective"

if __name__ == '__main__':
    test_MyFiniteRelationProperties()