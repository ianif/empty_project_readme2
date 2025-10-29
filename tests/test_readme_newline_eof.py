+import os
+
+
+def test_readme_ends_with_newline():
+    # Many tools expect text files to end with a trailing newline (POSIX).
+    # The README.md currently lacks a final newline, which can break
+    # concatenation, patching tools, or linters. This test documents that
+    # contract.
+    path = os.path.join(os.path.dirname(__file__), os.pardir, "README.md")
+    path = os.path.abspath(path)
+    with open(path, "rb") as f:
+        data = f.read()
+    assert data.endswith(b"\n"), "README.md should end with a newline (\\n)"
+
