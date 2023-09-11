import phonenumbers

print("__________.__                  .______  _______  ___ ")
print("\______   \  |__   ____   ____ |__\   \/  /\   \/  / ")
print(" |     ___/  |  \ /  _ \ /    \|  |\     /  \     /  ")
print(" |    |   |   Y  (  <_> )   |  \  |/     \  /     \  ")
print(" |____|   |___|  /\____/|___|  /__/___/\  \/___/\  \ ")
print("               \/            \/         \_/      \_/ ")
print("*created by superkar bedr*")
print("Enter phone number with reg. code:")
number = input()


from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))
