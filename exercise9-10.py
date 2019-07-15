# # Exercise 9

def display(g_list):
    for item in g_list:
        print(f" * {item}")

def total_items(list_name):
    char_count = len(list_name)
    return char_count
        

grocery_list = ['beets', 'apple', 'ginger', 'spinach']


# display(grocery_list)
# grocery_list.append('rice')
# display(grocery_list)

# print(len(grocery_list))



# print(total_items(grocery_list))

# def check_item_in_list(list_name):
#     for items in list_name:
#         if 'banana' in items:
#            banana_print = 'You have bananas!'
#         else:
#             banana_print = 'No Bananas :('
#     return banana_print

# print(check_item_in_list(grocery_list))

# print(grocery_list[1])

# alpha_list = sorted(grocery_list)
# for grocery in alpha_list:
#         print(f"* {grocery}")


# EXCERCISE 10

# 1
students = {
  'cohort 1': 34,
  'cohort 2': 42,
  'cohort 3': 22
}

# 2
# def display_cohort(cohort_dictionary):
#         for cohort_id, num_students in cohort_dictionary:
#                 print(f"{cohort_id}: {num_students} students")


# print(students(display_cohort)

# 3
students.update({'cohort 4': 43})

# 4
print(students.keys())

# 5
for cohort, students_amount in students.items():
        add_students = students_amount * .95
        print(f'{cohort} has {students_amount}students')

# 6
del students['cohort 2']

# 7
