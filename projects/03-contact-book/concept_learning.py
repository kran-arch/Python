#I am still learning the concept


contact1 = {
    "name": "Karan Khokhar",
    "phone": "99119xxxxx",
    "email": "blabla@balbal.com"
}

contact2 = {
    "name": "person1",
    "phone": "mobile1",
    "email": "email1"
}

contact3 = {
    "name": "person2",
    "phone": "mobile2",
    "email": "email2"
}

contacts = [contact1,contact2,contact3]

contact1.update({"name": "person1"})
contact1.update({"email": "email1"})
del contact1["phone"]   
print(contact1)
for x in contacts:
    print(x["phone"])