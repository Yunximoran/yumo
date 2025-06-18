import sys
from pathlib import Path
from plugs.convtert import svgtoico

try:
    size = int(sys.argv[1])
except Exception:
    size = 256

cwd = Path.cwd()
icons = cwd.joinpath("icons")
icons.mkdir(parents=True, exist_ok=True)

for svg in cwd.glob(r"*.svg"):
    ico = icons.joinpath(f"{svg.stem}.ico")
    svgtoico(str(svg), str(ico), size)