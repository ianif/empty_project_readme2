+"""
+Algorithms module with slow and optimized implementations.
+
+We choose sum_of_squares over iterables as our example. The naive version
+creates an intermediate list and uses Python-level loops; the optimized
+version avoids materialization and leverages generator-based computation to
+reduce both runtime and memory usage.
+"""
+
+# Author is ARTEMIS
from __future__ import annotations
+
+from typing import Iterable, List
+
+
+def sum_of_squares_slow(nums: Iterable[int]) -> int:
+    """
+    Intentionally slow and memory-inefficient implementation.
+
+    Anti-patterns used here (for demonstration):
+    - Materializes an intermediate list of squares (O(n) extra memory)
+    - Uses Python-level for loops and list append operations (overhead)
+    - Converts to list even if already a list (wastes memory/time)
+    """
+    # Convert to list to demonstrate extra memory footprint
+    lst: List[int] = list(nums)
+    squares: List[int] = []
+    for x in lst:
+        squares.append(x * x)
+    total = 0
+    for s in squares:
+        total += s
+    return total
+
+
+def sum_of_squares(nums: Iterable[int]) -> int:
+    """
+    Optimized implementation that minimizes overhead:
+    - Avoids intermediate lists by using a generator expression
+    - Uses built-in sum which iterates in C
+    - Works efficiently with any iterable without extra materialization
+    - Keeps constant additional memory and significantly less Python overhead
+    """
+    return sum(x * x for x in nums)
+
+
+__all__ = ["sum_of_squares_slow", "sum_of_squares"]
