from act4e_interfaces import InvalidValue, FiniteSet
from act4e_solutions import SolSemiCategoryRepresentation, MyFiniteSet
from .util import h

category_data = {
    "objects": {
        "X": {
            "obdata": 1,
            "identity": {
                "mordata": "id_X"
            }
        },
        "Y": {
            "obdata": 0,
            "identity": {
                "mordata": "id_Y"
            }
            
        }
    },
    "morphisms": {
        "f": {
            "mordata": "dd",
            "source": "X",
            "target": "Y"
        },

        "g": {
            "mordata": "dd",
            "source": "Y",
            "target": "Z"
        }
    },
    "equations": ["f;f=f"]
}
# Define the composition function
def compose(ob1, ob2, ob3, m1, m2):
    if m1 == 'id_X':
        return m2
    if m2 == 'id_X':
        return m1
    return f"{m1};{m2}"

# Define the test function

# Load the category using SolSemiCategoryRepresentation
representation = SolSemiCategoryRepresentation()
io_helper = h  # Using dummy IOHelper
ob_data_setoid = MyFiniteSet([])
mor_data_setoid = MyFiniteSet([])
semi_category = representation.load(
    h=io_helper,
    data=category_data,
    ObData=ob_data_setoid,
    MorData=mor_data_setoid,
    compose=compose
)

def test_catHasId():
    # Verify the identity of each object
    for obj in semi_category.objects().elements():
        
        try: 
            identity_morphism = semi_category.identity(obj)
        except InvalidValue:
            assert False, f"identity not found for {obj}: the proposed semicategory is not a category."
        else:
            print(f"The identity morphism for object {obj.label} exists, as it should: '{identity_morphism.mordata}'")
    print(f"Every object in the proposed category has an identity morphism!")

def test_homNotFiniteIfNone():
    # Verify that the homset is not finite if None
    for obj1 in semi_category.objects().elements():
        for obj2 in semi_category.objects().elements():
            if ob_data_setoid.equal(obj1, obj2):
                continue
            homset = semi_category.hom(obj1, obj2, uptolevel= None)
            assert not isinstance(homset, FiniteSet), f"The homset of ({obj1.label}, {obj2.label}) is finite, but it should be infinite with uptolevel = None!"
        
    print(f"The homset of every object in the proposed category is infinite, as it should be!")


if __name__ == '__main__':
    test_catHasId()
    test_homNotFiniteIfNone()
    