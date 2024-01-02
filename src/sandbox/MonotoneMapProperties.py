from act4e_solutions import MyFiniteMap, MyFiniteMonotoneMapPropertiesImpl, SolFinitePosetRepresentation
from .util import h

def test_monotone_map_properties():
    # Define the set 's' containing a carrier set and relations
    set_data = {
        "carrier": {
            "elements": ["\U0001F34E", "\U0001F36B", "\U0001F955", "\U0001F354", "\U0001F968", "\U0001F9C0", "\U0001FAD5", "\U0001F347"]
        },
        "hasse": [
            ["\U0001F955", "\U0001F968"],
            ["\U0001F968", "\U0001F34E"],
            ["\U0001F955", "\U0001F36B"],
            ["\U0001F955", "\U0001F9C0"],
            ["\U0001F347", "\U0001F354"],
            ["\U0001F347", "\U0001F9C0"],
            ["\U0001F36B", "\U0001F354"],
            ["\U0001F354", "\U0001FAD5"],
            ["\U0001F9C0", "\U0001FAD5"]
        ]
    }

    # Creating an instance of SolFinitePosetRepresentation and loading data into it
    poset_representation = SolFinitePosetRepresentation()
    poset = poset_representation.load(h, set_data)

    # Creating a monotone map with identity mappings for each element in the carrier set
    identity_map = [(elem, elem) for elem in poset.carrier().elements()]
    identity_monotone_map = MyFiniteMap(poset.carrier(), poset.carrier(), identity_map)

    # Checking if the created map is monotone within the poset
    map_properties = MyFiniteMonotoneMapPropertiesImpl()
    is_monotone = map_properties.is_monotone(poset, poset, identity_monotone_map)

    # Assertion to validate the monotonicity of the map within the poset
    assert is_monotone
