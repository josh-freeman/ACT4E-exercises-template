from act4e_solutions import SolFinitePosetRepresentation, MyFiniteSet, MyFiniteRelation, MyFiniteMap, SolFiniteRelationProperties
from .util import h, merge_sort, NotSortable




def test_carrier_elements():
    elements = [1, 2, 3, 4]
    relation = [[1, 2], [2, 3], [3, 4]]  # Define a partial order relation

    d = {"carrier": {"elements": elements}, "hasse": relation}

    poset = SolFinitePosetRepresentation().load(h, d)
    
    carrier = poset.carrier()

    assert [i for i in carrier.elements()] == elements

    assert poset.r._values == relation

def test_elements_relation():
    poset = SolFinitePosetRepresentation().load(h, {"carrier": {"elements": [1, 2, 3, 4]}, "hasse": [[1, 2], [2, 3], [3, 4]]})
    
    assert poset.holds(2, 4), "2 should be related to 4"

def test_save_load_poset():
    poset = SolFinitePosetRepresentation().load(h, {"carrier": {"elements": [1, 2, 3, 4]}, "hasse": [[1, 2], [2, 3], [3, 4]]})
    poset_rep = SolFinitePosetRepresentation()

    poset_desc = poset_rep.save(h, poset)
    loaded_poset = poset_rep.load(h, poset_desc)

    assert poset.r._values == loaded_poset.r._values

def test_merge_sort_exception():
    poset = SolFinitePosetRepresentation().load(h, {"carrier": {"elements": [1, 2, 3, 4]}, "hasse": [[1, 2], [2, 3], [3, 4]]})
    
    try:
        merge_sort([1, 4, 2, 1], poset)
    except NotSortable as e:
        assert True

if __name__ == '__main__':
    test_carrier_elements()
    test_elements_relation()
    test_save_load_poset()
    test_merge_sort_exception()
