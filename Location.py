import geocoder

our_ip = geocoder.ip("5.156.11.83")

location = our_ip.latlng
print(location)
print(our_ip)