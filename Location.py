import geocoder

our_ip = geocoder.ip("IP_ADDRESS")

location = our_ip.latlng
print(location)
print(our_ip)
