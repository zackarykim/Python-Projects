a = input("File Name:")

if a.lower().strip().endswith(".gif"):
    print("image/gif")
elif a.lower().strip().endswith(".jpg") or a.strip().endswith(".jpeg"):
    print("image/jpeg")
elif a.lower().strip().endswith(".png"):
    print("image/png")
elif a.lower().strip().endswith(".pdf"):
    print("application/pdf")
elif a.lower().strip().endswith(".txt"):
    print("text/plain")
elif a.lower().strip().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

