# There is a string method called count that is similar to the function in the previous exercise. 
# 
# Write an invocation that counts the number of times the letter a occurs in “banana”.

# word = "banana"
# char_num = word.count("a")
# print(char_num)

data = "From stephen.marquard@ uct.ac.za Sat Jan  5 09:14:16 200"

at_pos = data.find("@")
space_pos = data.find(" ", at_pos + 2)
get_host = data[at_pos + 2:space_pos]
print(get_host)