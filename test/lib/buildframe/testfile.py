import os.path

from lib.buildframe import BuildDir

import pytest


@pytest.mark.parametrize(
    'substructures', [
        ['t1', 't2', 't3']
    ]
)
def test_BuildDir(substructures):
    print("\nTEST BUILT DIR\n")
    build = BuildDir(substructures=substructures)

    build.OutTreeFrame()


