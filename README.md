+<!-- Author is ARTEMIS -->
# empty_project_readme2
+
+# Performance Optimization Example
+
+This repo demonstrates identifying a worst-ranked bottleneck and rewriting the code to improve runtime and memory. We use a simple but illustrative function: computing the sum of squares of integers.
+
+What changed
+- Before: sum_of_squares_slow materializes an intermediate list of squares and loops in Python, causing O(n) extra memory and extra interpreter overhead.
+- After: sum_of_squares uses a generator expression with the built-in sum, eliminating the intermediate list and reducing Python-level overhead. This cuts peak memory and typically speeds up execution.
+
+How to run the micro-benchmark
+1) Create a virtual environment (optional) and install nothing (standard library only).
+2) Run:
+   python bench/benchmark.py
+
+Environment variables
+- N: number of items to generate (default 2,000,000). Example:
+  N=5000000 python bench/benchmark.py
+
+Files added
+- src/algos.py: slow and optimized implementations.
+- bench/benchmark.py: micro-benchmark that times and measures memory using tracemalloc, and reports speedup and memory delta.
<!-- artemis testing -->