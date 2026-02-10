"""Selection algorithms module.

Selection algorithms find the kth smallest/largest element.

TODO:
    - Implement QuickSelect (O(n) average)
    - Implement Median of Medians (O(n) guaranteed)
"""

from . import median_of_medians, quickselect

__all__ = ["quickselect", "median_of_medians"]
