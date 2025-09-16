# See https://en.wikipedia.org/wiki/Econet, especially the "Physical and data-link layers" and "Network and transport layers" sections.

from dataclasses import dataclass

class Header:
    pass


class Packet:
    pass


class Frame:
    pass


class Transmission:
    pass

@dataclass
class EconetInterface:
    # Pin definitions
    data_pos: int   # +ve
    ground: int
    clock_pos: int  # +ve
    data_neg: int   # -ve
    clock_neg: int  # -ve
