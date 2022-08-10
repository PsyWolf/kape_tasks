from price_converter import PriceConverter
from currencies import Currencies

price_converter = PriceConverter()

amt = price_converter.convert_USD(20, Currencies.COP)
print(amt)

amt = price_converter.convert_USD(500, Currencies.COP)
print(amt)

amt = price_converter.convert_USD(6000, Currencies.COP)
print(amt)

amt = price_converter.convert_USD(10000, Currencies.COP)
print(amt)

amt = price_converter.convert_USD(100000, Currencies.COP)
print(amt)

amt = price_converter.convert_USD(20, Currencies.NOK)
print(amt)

amt = price_converter.convert_USD(500, Currencies.NOK)
print(amt)

amt = price_converter.convert_USD(6000, Currencies.NOK)
print(amt)

amt = price_converter.convert_USD(10000, Currencies.NOK)
print(amt)

amt = price_converter.convert_USD(100000, Currencies.NOK)
print(amt)

amt = price_converter.convert_USD(20, Currencies.EUR)
print(amt)

amt = price_converter.convert_USD(500, Currencies.EUR)
print(amt)

amt = price_converter.convert_USD(6000, Currencies.EUR)
print(amt)

amt = price_converter.convert_USD(10000, Currencies.EUR)
print(amt)

amt = price_converter.convert_USD(100000, Currencies.EUR)
print(amt)
