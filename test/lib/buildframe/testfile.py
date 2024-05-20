
from lib.build import buildStructure

import pytest


@pytest.mark.parametrize(
    'substructures', [
        ['t1', 't2', 't3']
    ]
)
def test_BuildDir(substructures):
    print("\nTEST BUILT DIR\n")
    build = buildStructure.BuildStructure(substructures=substructures)

    build.OutTreeFrame()
