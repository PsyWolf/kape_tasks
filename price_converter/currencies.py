from enum import Enum

class Currencies(Enum):
    USD = "US${amount}"
    JPY = "¥{amount}"
    GBP = "£{amount}"
    EUR = "€{amount}"
    CAD = "C${amount}"
    AUD = "A${amount}"
    SEK = "{amount} kr"
    SGD = "S${amount}"
    MXN = "Mex${amount}"
    NZD = "NZ${amount}"
    DKK = "{amount} kr"
    BRL = "R${amount}"
    NOK = "{amount} kr"
    HKD = "HK${amount}"
    CLP = "CLP${amount}"
    THB = "฿{amount}"
    ZAR = "R{amount}"
    INR = "₹{amount}"
    COP = "{amount} pesos"