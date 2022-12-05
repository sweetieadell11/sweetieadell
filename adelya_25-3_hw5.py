data = ["O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543"]
designations = []
codes = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
         designations.append(i)

operators = {}
i = 0
while len(operators) != len(designations):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators["Katel"]
del operators["Fonex"]

operators["O!"].add("0705")
operators["O!"].add("0703")
operators["O!"].add("0504")
operators["Megacom"].add("0550")
operators["Megacom"].add("0555")
operators["Megacom"].add("0999")
operators["Beeline"].add("0770")
operators["Beeline"].add("0222")
operators["Beeline"].add("0777")

for key, value in operators.items():
    print(f"{key}-{value}")
