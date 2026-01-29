students = []

for i in range(3):
    print(f"Student {i+1}:")
    name = input("Name: ")
    math_score = float(input("Math: "))
    phys_score = float(input("Physics: "))
    chem_score = float(input("Chemistry: "))
    
    avg = (math_score + phys_score + chem_score) / 3
    students.append({'name': name, 'avg': avg})

for s in students:
    print(f"Name: {s['name']}, Average: {round(s['avg'], 2)}")