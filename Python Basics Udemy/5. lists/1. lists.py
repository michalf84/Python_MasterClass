computer_parts=["computer",
                "monitor",
                "keyboard",
                "mouse"]
for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])

computer_parts.append("new product")
print(computer_parts)

computer_parts.append("wersalka")
computer_parts.extend("gowno")
computer_parts.extend(["gowno2"])
print(computer_parts)
