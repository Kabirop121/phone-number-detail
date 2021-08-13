import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter your number: ")

print(''' AVAILABEL COUNTRIES FOR THIS APPLICATION 

INDIA, AMERICA, SRI LANKA

''')

cn = input("Enter your country name: ")
country_name = cn.upper()

if country_name == "INDIA":
    mobileNo = "+91" + mobileNo
    
if country_name == "AMERICA":
    mobileNo = "+1" + mobileNo

if country_name == "SRI LANKA": 
    mobileNo = "94" + mobileNo

mobileNo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNo, "en"))

print('Valid Mobile number: ',phonenumbers.is_valid_number(mobileNo))

print("Checking possibility for number: ", phonenumbers.is_possible_number(mobileNo))