# LESSON 4 STARTER CODE: VARIABLES AND DATA TYPES

# ========================================
# PART 1: Creating Variables Practice
# ========================================
name = "Presley"
age = 16
gpa = 3.9
grade = 10

print("Student Name: " + name )
# print("Student Age: "+ age) str + int wont work
print("Student Age: ", age) 

# variables can change 
age = 17
# multiple assignment
subject, period = "CS100", 1

# ========================================
# PART 2: Data Types Practice
# ========================================
# Four main(primitive) data types
name = "Presley" #str(string)
age = 16 #int()
gpa = 3.9
is_present = True #bool(Boolean)

#Check data types via type() function
print(f"Name:{name} Type: {type(name)}")
print(f"Name:{age} Type: {type(age)}")
print(f"Name:{gpa} Type: {type(gpa)}")
print(f"Name:{is_present} Type: {type(is_present)}")

# ========================================
# PART 3: Type Conversion Practice
# ========================================
#convert between types
grade_text = "95"
# grade_text = '95"'
print(f"Original:{grade_text} {type(grade_text)}")
grade_number = int(grade_text)
print(f"As number:{grade_number}{type(grade_number)}")
gpa_number = float(gpa)
print(f"GPA: {gpa_number} {type(gpa_number)}")
gpa_text = str(gpa_number)

#practice with bool() function
print((f"bool(0) - {bool(0)}")) # false
print((f"bool(1) - {bool(1)}")) #true
print((f"bool(10) - {bool(10)}")) #true
print((f"bool('') - {bool('')}")) #ｆａｌｓｅ
print((f"bool(' ') - {bool(' ')}")) # true
# ========================================
# PART 4: Variable Operations Practice   
# ========================================
#Swapping variables
color1 = "red"
color2 = "blue"
color1, color2 = color2, color1 #swapping
print(f"Color2:{color2}")