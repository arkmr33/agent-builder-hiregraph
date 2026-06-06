import sys
from pathlib import Path

project_root = Path().resolve().parents[2]

sys.path.append(str(project_root))

from hiregraph.graph import build_graph

graph = build_graph()
assert graph is not None