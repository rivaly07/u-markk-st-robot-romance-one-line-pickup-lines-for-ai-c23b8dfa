import os
import sys

line = "You hallucinated a whole future for us and still cited your sources - I'm in."
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry:
    entry.write(line)
