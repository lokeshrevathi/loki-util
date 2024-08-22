import phonenumbers
from phonenumbers import geocoder
ph1 = phonenumbers.parse("+917904412316")
print(geocoder.description_for__number(ph1, "en"))