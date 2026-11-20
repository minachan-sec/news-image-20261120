"""news-image-20261120 entry program (Python 3.13, standard library only).

The entry image is the entry.png beside this file. This program copies it to
/output/entry.png. The grader runs it twice; both runs must write identical
bytes. No network, no third-party packages: shutil + pathlib only.

Local test:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
