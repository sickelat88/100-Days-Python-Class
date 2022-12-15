# # File not found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("somethind")
# except KeyError as error_message:
#     print(f"{error_message} key doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("test error")
#     # file.close()
#     # print("file was closed")

height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Value is invalid")

bmi = weight / (height * height)
print(bmi)
