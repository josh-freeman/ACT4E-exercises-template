from act4e_interfaces import IOHelper, FinitePoset
import os
from typing import Dict, Any, TypeVar, Collection

class DockerIOHelper(IOHelper):
    def loadfile(self, name: str) -> Dict[str, Any]:
        """Load a file from a Docker Linux machine."""
        file_data = {}
        file_path = os.path.join("/../out-results", name) 

        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                # Read the file and populate the data dictionary
                file_data['contents'] = file.read()
        except FileNotFoundError:
            file_data['error'] = f"File '{name}' not found."

        return file_data
    
h = DockerIOHelper()


E = TypeVar("E")

class NotSortable(Exception):
    """Raise this if a collection is not sortable"""

from math import floor

def merge_sort(s: Collection[E], fp:FinitePoset[E]) -> Collection[E]:
    def merge(s1:Collection[E], s2:Collection[E]):
        """Merge two sub arrays using the finite poset fp"""
        i1, i2 = 0, 0
        c = []
        while i1 < len(s1) or i2 < len(s2):
            if i1 < len(s1):
                e1 = s1[i1]
                if i2 < len(s2):
                    e2 = s2[i1]
                    # insert the smaller of e1, e2
                    if fp.holds(e1, e2):
                        c.append(e1)
                        i1 += 1
                    elif fp.holds(e2, e1):
                        c.append(e2)
                        i2 += 1
                    else:
                        raise NotSortable(f"Collection {s} is not a chain: elements {e1} and {e2} are not comparable: {e1}R{e2} = {fp.holds(e1, e2)}, {e2}R{e1} = {fp.holds(e2, e1)}")
                else:
                    c.append(s1[i1])
                    i1 += 1
            else:
                c.append(s2[i2])
                i2+=1

        return c

    def sort(s):
        length = len(s)
        if length <= 1:
            return s
        else:
            l, r = s[:floor(length/2)], s[floor(length/2):]
            return merge(sort(l), sort(r))
        
    return sort(s)