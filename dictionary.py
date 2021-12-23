phone = input("phone: ")
digit_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
   output += digit_mapping.get(ch, "!") + ""
   print(output)