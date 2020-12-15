from remerkleable.core import Path 
from test_types import TestContainer

def pretty_path(p: Path) -> str:  # not the default repr, yet.
    return p.anchor.__name__ + ' ' + '/'.join(str(k) for k, _ in p.path)

def print_test_case(p: Path) -> None:
    print(f"{pretty_path(p)} {p.gindex()}")