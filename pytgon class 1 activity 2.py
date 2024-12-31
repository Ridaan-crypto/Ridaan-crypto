cityname={"name":"mumbai","pincode":200001}
print(cityname)
cityname["name"]="kolkata"
print(cityname)
cityname["known for"]="vada pav"
print(cityname)
cityname.pop("known for")
print(cityname)
cityname.clear()
print(cityname)