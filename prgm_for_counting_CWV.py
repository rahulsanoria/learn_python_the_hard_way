from sys import argv
script,file_name = argv

in_file = open(file_name)
file_data = in_file.read()
print file_data

count_vowel = 0
space = 0
i = 0
for i in range(0,len(file_data)):
	if file_data[i] == " " and file_data[i + 1] != " ":
		space += 1
	elif file_data[i] == " " and file_data[i + 1] == " ":
		pass
	else:		
		if file_data[i] == 'a' or file_data[i] == 'e' or file_data[i] == 'i' or file_data[i] =='o' or file_data[i] == 'u' :
			count_vowel = count_vowel + 1

str = ""

for i in range(0,len(file_data)):
	if file_data[i] != " ":
	
		
		str = str + file_data[i] 
	
print "total characters = ",len(str)
print "total vowels = ", count_vowel
print "Words = ", space + 1