from eth2spec.phase0.spec import *
from remerkleable.core import * 

def pretty_path(p: Path) -> str:  # not the default repr, yet.
    return p.anchor.__name__ + ' ' + '/'.join(str(k) for k, _ in p.path)

def printTestCase(p: Path) -> None:
    print(f"{pretty_path(p)} {p.gindex()}")

stateAnchor = Path(BeaconState)
attestationAnchor = Path(Attestation)

slotPath = stateAnchor / 'slot'
finalizedRootPath = stateAnchor / 'finalized_checkpoint' / 'root'
deepStatePath = stateAnchor / 'validators' / 1 / 'slashed'
blockRootsList4Path = stateAnchor / 'block_roots' / 4
justificationBitsPath = stateAnchor / 'justification_bits'
justificationBits7Path = stateAnchor / 'justification_bits' / 2
randaoMixesVector2Path = stateAnchor / 'randao_mixes' / 2
aggregationBits0Path = attestationAnchor / 'aggregation_bits' / 0

printTestCase(slotPath)
printTestCase(finalizedRootPath)
printTestCase(deepStatePath)
printTestCase(blockRootsList4Path)
printTestCase(justificationBitsPath)
printTestCase(justificationBits7Path)
printTestCase(randaoMixesVector2Path)
printTestCase(aggregationBits0Path)
