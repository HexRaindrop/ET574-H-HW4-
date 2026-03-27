from dataclasses import dataclass,
import re

@dataclass
class cpu:
    brand   : str
    prefix  : str
    gen     : int
    mod     : int
    suffix  : str

    def __post_init__(self):
        brand_map = {
            'intl': "Intel",
            'amd': "AMD",
            'int': "Intel",
        }
        self.brand = brand_map.get(self.brand.lower(), self.brand.capitalize())

    def __str__(self):
        return f"{self.brand}:{self.prefix} {self.gen}{self.mod}{self.suffix}"

s = cpu('intel','i7',12,700,'k')

print(s)

s = cpu(\
input('what brand? \nexamples\n\tintl, amd\n\t\tinput:  '),\
input('which prefix?\nexample\n\tryzen5,i5\n\t\tinput:  '),\
input("which gen?: "),\
input("which cpu of the gen?\n\texample: in a i7 12700k, the \"700\" is the model number\n\t\tinput:  "),\
input("what is the suffex?\n\tin the last exampple, the \"K\" is the suffex\n\t\tinput:  "))

print(s)


s = str(s)
matches = list(re.finditer(r'\d+|[a-zA-Z]+', s))
brand, prefix, mod, suffix = matches[0].group(), matches[1].group() + matches[2].group(), matches[3].group(),matches[4].group()

print(brand)
print(prefix)
print(mod)
print(suffix)
