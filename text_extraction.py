import re

def extract_information(text, extraction_type):
  if extraction_type == "phone_number":
    pattern = r"\d{3}-\d{3}-\d{4}"
  elif extraction_type == "date":
    pattern = r"\d{2}/\d{2}/\d{4}"
  elif extraction_type == "email":
    pattern = r"\w+@\w+\.\w+"
  elif extraction_type == "url":
    pattern = r"http(s)?://\w+\.\w+"
  else:
    raise ValueError("Invalid extraction type")

  matches = re.findall(pattern, text)
  return matches

def main():
  text = input("Enter the text: ")
  extraction_type = input("Enter the extraction type (phone_number, date, email, url): ")

  results = extract_information(text, extraction_type)
  print(f"Extracted {extraction_type}s: {results}")

if __name__ == "__main__":
  main()