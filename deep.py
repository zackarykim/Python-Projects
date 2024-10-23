q = input("What is the answer to the Great Question of Life, the Universe and Everything?")

if q.lower().strip() == "42":
    print("Yes")
elif q.lower().strip() == "forty-two":
    print("Yes")
elif q.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
