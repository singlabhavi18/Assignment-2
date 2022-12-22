str = input("Enter the string: ")
len = len(str)
rev_str = str[::-1]
slice = str[10:26]
print("The length of the given string is", len)
print(rev_str)
print(slice)
new_str = str.replace("a case sensitive", "object oriented")
print("The new string is", new_str)
indx = str.index("a")
print("The index of the letter a is", indx)
no_spc = str.replace(" ", "")
print(no_spc)