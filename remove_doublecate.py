import codecs

lines = set()

path= input("enter path: ")
file = codecs.open(path, "r", "utf-8")

name = path.split("/")[-1].split(".")[0]+ "_.txt"
result = codecs.open(name, "w", "utf-8")
for line in file.readlines():
	lines.add(line)
	
for line in lines:
	result.write(line)
