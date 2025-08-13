# f = open("hrusi.txt", "r")
# content = f.read()
# print(content)
# f.close()


with open("hrusi.txt", "r") as f: #Context manager
    content = f.read()
    print(content)
    #No need to write f.close() because file is already closed by 
    #default when using with syntax