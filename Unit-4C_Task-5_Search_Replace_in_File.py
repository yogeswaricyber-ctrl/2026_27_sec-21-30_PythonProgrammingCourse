f = open("sample.txt", "r")
text = f.read()
f.close()

text = text.replace("Python", "Java")

f = open("sample.txt", "w")
f.write(text)
f.close()

print("Word replaced successfully")