+# Author is ARTEMIS
import random
+import time
+import tracemalloc
+from typing import Callable, Iterable, Tuple
+
+import os
+import sys
+
+# Make local src importable when running directly
+ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
+SRC_DIR = os.path.join(ROOT, "src")
+if SRC_DIR not in sys.path:
+    sys.path.insert(0, SRC_DIR)
+
+from algos import sum_of_squares_slow, sum_of_squares
+
+
+def bench(func: Callable[[Iterable[int]], int], data: Iterable[int], repeat: int = 5) -> Tuple[float, int]:
+    """Return (best_time_seconds, peak_memory_bytes)."""
+    best = float("inf")
+    peak_bytes = 0
+    for _ in range(repeat):
+        tracemalloc.start()
+        t0 = time.perf_counter()
+        _ = func(data)
+        dt = time.perf_counter() - t0
+        current, peak = tracemalloc.get_traced_memory()
+        tracemalloc.stop()
+        best = min(best, dt)
+        peak_bytes = max(peak_bytes, peak)
+    return best, peak_bytes
+
+
+def main():
+    rng = random.Random(42)
+    n = int(os.environ.get("N", 2_000_000))
+    # List so slow version can materialize and show its extra memory
+    data = [rng.randint(-10_000, 10_000) for _ in range(n)]
+
+    t_slow, m_slow = bench(sum_of_squares_slow, data)
+    t_fast, m_fast = bench(sum_of_squares, data)
+
+    # Identify worst bottleneck (here, slow vs optimized)
+    worst = ("sum_of_squares_slow", t_slow, m_slow)
+    improved = ("sum_of_squares", t_fast, m_fast)
+
+    speedup = t_slow / t_fast if t_fast > 0 else float("inf")
+    mem_delta = m_slow - m_fast
+
+    print("Benchmark: sum of squares")
+    print(f"Items: {n}")
+    print(f"Worst (before): {worst[0]} time={worst[1]:.6f}s, peak_mem={worst[2]:,} B")
+    print(f"Improved (after): {improved[0]} time={improved[1]:.6f}s, peak_mem={improved[2]:,} B")
+    print(f"Speedup: {speedup:.2f}x")
+    print(f"Peak memory delta: {mem_delta:,} B")
+
+
+if __name__ == "__main__":
+    main()
