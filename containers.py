from remerkleable.core import Path
from test_types import TestContainer
from helpers import print_test_case

testContainerAnchor = Path(TestContainer)

print_test_case(testContainerAnchor)
print_test_case(testContainerAnchor / 'uint')
print_test_case(testContainerAnchor / 'bool')
print_test_case(testContainerAnchor / 'bytes32')
print_test_case(testContainerAnchor / 'bitlist')
print_test_case(testContainerAnchor / 'bitvector')
print_test_case(testContainerAnchor / 'basicList')
print_test_case(testContainerAnchor / 'basicList' / 0)
print_test_case(testContainerAnchor / 'basicVector')
print_test_case(testContainerAnchor / 'basicVector' / 4)
print_test_case(testContainerAnchor / 'complexList')
print_test_case(testContainerAnchor / 'complexList' / 4)
print_test_case(testContainerAnchor / 'complexList' / 4 / 'field')
print_test_case(testContainerAnchor / 'complexVector')
print_test_case(testContainerAnchor / 'complexVector' / 4)
print_test_case(testContainerAnchor / 'complexVector' / 4 / 'field')

