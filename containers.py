from remerkleable.core import Path
from test_types import TestContainer
from helpers import print_test_case
from eth2spec.lightclient_patch.spec import BeaconState

testContainerAnchor = Path(TestContainer)

print_test_case(Path(BeaconState)/'next_sync_committee')
print_test_case(Path(BeaconState)/'finalized_checkpoint'/'root')

