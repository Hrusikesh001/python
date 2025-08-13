name = "Hrusi"
a = len(name)
print(a)

text = " hello world "
print(text.upper(), text)  # Output: " HELLO WORLD "
print(text.lower())        # Output: " hello world "
print(text.strip())        # Output: "hello world"
print(text.replace("world", "Python")) # Output: " hello Python "
print(text.split())        # Output: ['hello', 'world']
print(text.capitalize())
print(text.title())     #More specifically, words start with uppercased characters and all remaining cased characters have lower case.

text = "Python is fun"
print(text.find("is"))
print(text.replace("fun","awesome"))


text = "Apples,Bananas,Pineapples"
print(text.split(","))
print("," .join(['Apples', 'Bananas', 'Pineapples']))


text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False