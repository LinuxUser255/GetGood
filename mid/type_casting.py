# Type casting is the process of converting one data type to another.
# str(), int(), bool(), float() etc. are used to convert one data type to another.


# Basic example of Type Casting
name = "John Doe"
age = 30
gpa = 3.8

# Convert integer to float
age_float = float(age)

# Convert float to string
gpa_string = str(gpa)

print(f"Name: {name}")
print(f"Age: {age_float}")
print(f"GPA: {gpa_string}")

# Type hinting example
name: str = "Alice"
age: int = 30
gpa: float = 3.8

print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")

# Type cast name to a boolean
name_bool = bool(name)

print(f"Name as boolean: {name_bool}")

