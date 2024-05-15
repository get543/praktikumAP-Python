bilangan = [5, 10, 15, 20]
print(bilangan)
print(type(bilangan))

list_kosong = []
print(list_kosong)

list_string = ["satu"]
print(list_string)

# index (dimulai dari 0)
my_list = [10, 20, 30, 40]
print(my_list[3]) # 40
print(my_list[0]) # 10

# index negative (dimulai dari belakang) (-1)
print(my_list[-1]) # 40
print(my_list[-4]) # 10

print("---------------------------")

# list dengan looping
for elm in my_list:
  print(elm)

names = ["Joko", "Wati", "Budi", "Andi"]
for name in names:
  print(name)