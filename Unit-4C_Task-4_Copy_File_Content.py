f = open("sample.txt", "r")
data = f.read()
f.close()

f = open("copy.txt", "w")
f.write(data)
f.close()

print("File copied successfully")