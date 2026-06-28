# strings

from itertools import count


name = " Garvit Khuteta"
email = "GARVIT@GMAIL.COM"
sentence= "i want to became a data scientist"

#-----Most used Strings-----

print(f"Original      : '{name}'")
print(f"Strip         : '{name.strip()}'")
print(f"Lower         : '{email.lower()}'")
print(f"Upper         : '{sentence.upper()}'")
print(f"Title         : '{sentence.title()}'")
print(f"Replace       : '{sentence.replace('data scientist', 'ML engineer')}'")
print(f"Split         : '{sentence.split()}'")
print(f"Word Count    : '{len(sentence.split())}'")
print(f"Starts with   : '{sentence.startswith('i')}'")
print(f"Contains DS   : {'data' in sentence}") 



# ---- Real DS use case - Data Cleaning ----
# Actual dataset mein aisa data aata hai - clean karna padta hai

dirty_data = [
    "  Garvit Kumar  ",
    "RAHUL SHARMA",
    "priya singh",
    "  AMIT verma  "
]


print("\n-------- Data Cleaning --------")
print(f"{'Original':<20} {'Cleaned':<20}")
print("-" * 40)

for name in dirty_data:
    cleaned = name.strip().title()
    print(f"{name.strip():<20} {cleaned:<20}")



