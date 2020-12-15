from eth2spec.utils.ssz.ssz_typing import uint64,boolean,Bytes32,Container,Bitlist,Bitvector,List,Vector


class TestContainer2(Container):
    field: uint64

class TestContainer(Container):
    uint: uint64
    bool: boolean
    bytes32: Bytes32
    bitlist: Bitlist[10]
    bitvector: Bitvector[20]
    basicList: List[uint64, 30]
    basicVector: Vector[boolean, 30]
    complexList: List[TestContainer2, 10]
    complexVector: Vector[TestContainer2, 10]

