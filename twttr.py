post = input("Input:")
newpost = ""

for i in range(len(post)):
    if post[i].lower() not in "aeiou":
        newpost += post[i]

print("Output:", newpost)

