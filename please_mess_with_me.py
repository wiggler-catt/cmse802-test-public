# There is a mistake in the following code. Can you help correct it?

a = "1"
b = 1
c = True

# print(a + b)
print(b + c)

# To correct the mistake, we might convert a to an integer before adding
a = int(a)
print(int(a) + b)

# The following will also work:
print (a+c)
print (a*c)
print(a-b)