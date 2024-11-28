def main():
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }
    total = 0
    student_id = list(students_dict.keys())
    print(student_id)
    for items in students_dict.items():
        total+= items[1][3]
    print(total)
    # numbers_list = ["42-039-4736", "61-315-0160",
    #                 "10-450-1203", "75-421-2310", "07-103-5621"]
    # names_list = ["Clint Huish", "Amelia Davis",
    #               "Ana Soares", "Abdul Ali", "Amelia Davis"]
    # new_dict = dict(zip(numbers_list,names_list))
    # print(new_dict)
if __name__ == "__main__":
    main()