from dataclasses import dataclass,field
from typing import List
from datetime import date

@dataclass(frozen=True)
class Address:
    street:str
    city:str
    state:str
    zipcode:str

@dataclass(frozen=True)
class ImmutableEmp:
    name:str
    id:str
    doj:date
    adresses:List[Address]=field(default_factory=list)

if __name__=="__main__":
    home_adress=Address(street="222 main streer", city="madanapalle", state="andrapradesh", zipcode="517325")
    office_adress=Address(street="main rd 76", city="banglore", state="andrapradesh", zipcode="876543")  

    employee=ImmutableEmp(
        name="sravani",
        id="EMP76",
        doj=date(2024,6,23),
        adresses=[home_adress,office_adress]
)       

print(employee)
            



#try to add employee name

try:
    employee.name="xyz"
except AttributeError as ae:
    print(f"Error:{ae}") 


#try to modify addresses list
try:
    employee.adresses.append(Address(street="56 hgb", city="karnatakta", state="andrapradesh", zipcode="578655"))
except AttributeError as ae:
    print(f"Error:{ae}")        