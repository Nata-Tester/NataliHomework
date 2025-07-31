from smartphone import smartphone
catalog = ([
 smartphone("Iphone", "11", "8-800-555-35-35"),
 smartphone("Iphone", "12", "8-888-555-35-35"),
 smartphone("Iphone", "13", "8-800-000-35-35"),
 smartphone("Iphone", "14", "8-800-555-55-55"),
 smartphone("Iphone", "15", "8-888-555-55-55")
 ]
)

for phone in catalog:
    print(f"{phone.firm} - {phone.model}. {phone.number}")
