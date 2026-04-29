def print_id_card(name, age, cls, college, blood):
    print()
    print(f"{'STUDENT ID CARD':^38}")
    print()
    print(f"  {'Name':<14} {name}")
    print(f"  {'Age':<14} {age}")
    print(f"  {'Class':<14} {cls}")
    print(f"  {'College':<14} {college}")
    print(f"  {'Blood Group':<14} {blood}")
    print()


name    = input("Full Name    : ")
age     = input("Age          : ")
cls     = input("Class        : ")
college = input("College      : ")
blood   = input("Blood Group  : ")

print_id_card(name, age, cls, college, blood)