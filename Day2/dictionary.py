address = {
    "state":"Bagmati",
    "province_number": 3,
    "metro": "Kathmandu",
    "street": "Sifal"
}

example_dictionary = {
    "name": "Sharad", 
    "age": 24, 
    "allowance": 45000.50,
    "married": False,
    "marks":[10, 20, 30, 40],
    "address": address
}

address_value = example_dictionary["address"]
street = address_value["street"]

print(street)