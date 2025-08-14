"""

Description: Provides a function to compute the union of two lists in Python.
"""

from typing import List, Any


def find_union(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Returns the union of two lists, with duplicates removed.

    Args:
        list1 (List[Any]): The first list.
        list2 (List[Any]): The second list.

    Returns:
        List[Any]: A sorted list containing the union of the two input lists.
    """
    return sorted(set(list1) | set(list2))


if __name__ == "__main__":
    # Example usage
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    
    union_result = find_union(arr1, arr2)
    print("Union of the two lists:", union_result)
