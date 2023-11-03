file = open('./collect_me', 'rb')
binary = []
for i in file.read():
   binary.append(hex(i))
Need_binary = binary[4406:18326]

for i in range(0, 10, 1):
	print(binary[i])

print("------------------------------------")

for i in range(4400, 4416, 1):
	print(binary[i])

print("------------------------------------")

for i in range(4406, 4430,1):
	print(i,":", binary[i])

String = []
for i in range(0, len(Need_binary), 15):
    String.append(chr(int(Need_binary[i+11],16)))

for i in String:
    print(i, end="")
