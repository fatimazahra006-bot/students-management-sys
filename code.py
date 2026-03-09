print("="*3, "student management system", "="*3)

averages = []
students = []

while True:
    dic = {
        1: "Add student",
        2: "Display students",
        3: "Generate report",
        4: "Exit"
    }
    for key, value in dic.items():
        print(key, ".", value)
    print("="*3, "bienvenue :", "="*3)
    n = int(input("enter the number of your choice : "))
    while n < 1 or n > 4:
        print("-"*10)
        print("please enter a number between 1 and 4.")
        n = int(input("enter the number of your choice : "))
    def add_student(a):   ##premier function
        """
            Add a new student to the global list.
            - Prompts for student ID, name, and grades.
            - Ensures the ID is unique (no duplicates).
            - Validates that all grades are between 0 and 20.
            - Calculates the average grade and assigns a class (A–F).
            - Stores the student information in the global 'students' list.
            """
        if a == 1:
            print(" ---Add student---\n You should enter these informations :")
            print("-"*50)
            while True:
                info = {}
                info["ID"] = input("enter student ID : ")
                if any(s["ID"] == info["ID"] for s in students):
                    print(f"Student ID {info['ID']} already exists!")
                    continue
                info["name"] = input("enter student name : ")

                while True:
                    e = input("Enter grades separated by space: ")
                    grades = list(map(float, e.split()))
                    if all(0 <= g <= 20 for g in grades):
                        break
                    else:
                        print("Invalid grade detected! Grades must be between 0 and 20.")
                info["grades"] = grades

                Average = sum(grades) / len(grades)
                info["average"] = Average
                averages.append(Average)
                if Average >= 16:
                    info["class"] = "A"
                elif Average >= 14:
                    info["class"] = "B"
                elif Average >= 12:
                    info["class"] = "C"
                elif Average >= 10:
                    info["class"] = "D"
                else:
                    info["class"] = "F"

                students.append(info)
                print("+"*50)
                answer = input("Do you want to add more students? (y/n) : ")
                if answer == "n":
                    break
        return students
    students = add_student(n)

    if n == 2:
        print("-"*10)
        def ecriture_en_fichier(informations, fichier):
            """
                Write student information to a text file.
                - Iterates through the list of students.
                - Saves each key/value pair (ID, name, grades, average, class).
                - Adds a separator line for readability.
                - Uses file that user chooses.
                """
            with open(fichier, "a") as f:
                for student in informations:
                    for k, v in student.items():
                        f.write(f"{k}: \t {v} \n")
                    f.write(f"{"-" * 50}\n")
            return informations, fichier

        file = input("enter the file name : ")
        file=file+".txt"
        ecriture_en_fichier(students, file)
        
        def display_students(fichier):
            """
                Display all students stored in the file.
                - the user opens the file of his choice in read mode.
                - Prints the content line by line.
                - Allows the user to view previously saved student data.
                """
            with open(fichier, "r") as f:
                print("display students :")
                for line in f:
                    print(line)
            return fichier
        display_students(file)
        print("-" * 10)

    elif n == 3:
        def generate_report(fichier, averages):
            """
                Generate a statistical report of student averages.
                - Calculates the class average.
                - Finds the highest and lowest averages.
                - Writes the results into REPORT_FILE.
                - If no averages are available, displays an error message.
                """
            print("generate report :")
            if averages:
                cv = sum(averages) / len(averages)
                with open(fichier, "w") as f:  # <-- use "w" instead of "r"
                    f.write(f"Highest average : {max(averages)}\n")
                    f.write(f"Lowest average : {min(averages)}\n")
                    f.write(f"Class average : {cv}\n")
            else:
                print("*" * 10)
                print("No averages available yet!")
            return fichier

        generate_report("generat report.txt",averages)

        def afficher_report(fichier):
            """
                Display the generated report.
                - Opens REPORT_FILE in read mode.
                - Prints the report line by line.
                """
            with open(fichier, "r") as f:
               for line in f:
                  print(line)
            return fichier
        afficher_report("generat report.txt")

    if n == 4:
        print("--- Exit program ---")
        break
