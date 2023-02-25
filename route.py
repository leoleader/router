## class that represents a routing address with the fields provided
## in the update message, along with the CIDR of the network and netmask. 
class Route:

    def __init__(self, dict, peer):

        self.network = dict["network"]
        self.netmask = dict["netmask"]
        self.peer = peer
        self.localpref = dict["localpref"]
        self.ASPath = dict["ASPath"]
        self.selfOrigin = dict["selfOrigin"]
        self.origin = dict["origin"]

        self.CIDR = convertCIDR(self.network, self.netmask)


## takes in a network address and subnet mask and converts it to CIDR notation
def convertCIDR(network, mask):

    ##converting the mask to binary and counting the number of 1s
    mask_binary = ''.join([bin(int(x)+256)[3:] for x in mask.split('.')])
    cidr_notation = str(mask_binary.count('1'))

    return network + "/" + cidr_notation

                        