correct_password = "1234"
password = input("Sisesta parool: ")

while password != correct_password:
    print("Vale parool, proovi uuesti!")
    password = input("Sisesta parool: ")

print("Õige parool!")