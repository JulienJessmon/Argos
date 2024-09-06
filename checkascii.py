import re


# check if link is valid
def isDomain(string):
    domain = r"^https?://([a-zA-Z0-9.]+)(?:/|$)"
    if string is None:
        return False
    if re.search(domain, string):
        return True
    else:
        return False


link = input("Enter Url: ")
print(isDomain(link))

