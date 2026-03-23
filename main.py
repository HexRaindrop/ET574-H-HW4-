from dataclasses import dataclass

@dataclass
class cpu:
     brand  :       str
     prefix :       str
     gen    :       int
     mod    :       int
     suffix :       str 

    def __post_init__(self):
        brand_map = {
        'intl' :    "Intel",
        'amd'  :     "AMD",
        'int'  :     "Intel",
        }
    self.brand = brand_map.get(self.brand.lower(),self.brand.capitalize())
def __str__(self):
    return f"{self.brand} {self.prefix} {self.gen}{self.mod}{self.suffix}"

s = cpu('intel','i7',12,700,'k')

print(s)
