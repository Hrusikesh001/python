#Append to an existing file called John.txt
# It should add data about John Hometown

f = open("John.txt","a")

string= '''
John initially lived in New York. He moved to Delhi.
'''
f.write(string)

f.close()

#If i run this code then the "John initially lived in New York. He moved to Delhi." will be appended or add to the existing file John.txt