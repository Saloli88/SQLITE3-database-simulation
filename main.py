import os
import sqlite3


list = [
    "Employee name",
    "Employee surname",
    "Job description",
    "Employee ID",
    "Employee's age",
    "Driving license",
    "Primary Key",
]
database = "Employees.db"


class OPTIONS(object):
    def CREATE_DATABASE():
        with sqlite3.connect(database) as connect:
            cursor = connect.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS EMPLOYEES(name TEXT,surname TEXT,job_desc TEXT,employee_id TEXT,age INT,driving license TEXT)"
            )

            return connect

    def ADD_DATA():
        with sqlite3.connect(database) as connect:
            cursor = connect.cursor()
            name = input("Employee name:")
            surname = input("Employee surname:")
            job_desc = input("Job description:")
            employee_id = input("Employee ID:")
            age = int(input("Employee's age:"))
            driving_license = input("Does employee have driving license?")
            cursor.execute(
                f"INSERT INTO EMPLOYEES values('{name}','{surname}','{job_desc}','{employee_id}',{age},'{driving_license}')"
            )

    def DELETE():
        with sqlite3.connect(database) as connect:
            cursor = connect.cursor()
            for i in range(len(list)):
                print(i, list[i])
            parameter = input("Choose a parameter to delete an employee:")
            if parameter == "0":
                name = input("Name:")
                cursor.execute(f"DELETE FROM EMPLOYEES WHERE name ='{name}'")
                print("Employee has been deleted")
            elif parameter == "1":
                surname = input("Surname:")
                cursor.execute(f"DELETE FROM EMPLOYEES WHERE surname ='{surname}'")
                print("Employee has been deleted")
            elif parameter == "2":
                job_desc = input("Description:")
                cursor.execute(f"DELETE FROM EMPLOYEES WHERE job_desc ='{job_desc}'")
                print("Employee has been deleted")
            elif parameter == "3":
                employee_id = input("ID:")
                cursor.execute(
                    f"DELETE FROM EMPLOYEES WHERE employee_id ='{employee_id}'"
                )
                print("Employee has been deleted")
            elif parameter == "4":
                age = input("Age:")
                cursor.execute(f"DELETE FROM EMPLOYEES WHERE age ={age}")
                print("Employee has been deleted")
            elif parameter == "5":
                driving_license = input("License:")
                cursor.execute(
                    f"DELETE FROM EMPLOYEES WHERE driving_license ='{driving_license}'"
                )
                print("Employee has been deleted")
            elif parameter == "6":
                primary_key = input("Primary key:")
                cursor.execute(f"DELETE FROM EMPLOYEES WHERE rowid='{primary_key}'")
                print("Employee has been deleted")
            else:
                OPTIONS.DELETE()

    def SHOW():
        with sqlite3.connect(database) as connect:
            cursor = connect.cursor()
            select2 = input(
                "1.Show every employee,2.Show ages,3.Show driving licenses,4.Show IDs,5.Show description,6.Show names\nSelect:"
            )
            if select2 == "1":
                cursor.execute("SELECT * from EMPLOYEES")
                for i in cursor.fetchall():
                    print(i)
            elif select2 == "2":
                cursor.execute("SELECT age from EMPLOYEES")
                for i in cursor.fetchall():
                    print(i)
            elif select2 == "3":
                cursor.execute("SELECT driving_license from EMPLOYEES")
                for i in cursor.fetchall():
                    print(i)
            elif select2 == "4":
                cursor.execute("SELECT employee_id from EMPLOYEES")
                for i in cursor.fetchall():
                    print(i)
            elif select2 == "5":
                cursor.execute("SELECT job_desc from EMPLOYEES")
                for i in cursor.fetchall():
                    print(i)
            elif select2 == "6":
                cursor.execute("SELECT name from EMPLOYEES")
                for i in cursor.fetchall():
                    print(i)
            else:
                OPTIONS.SHOW()

    def UPDATE():
        with sqlite3.connect(database) as connect:
            cursor = connect.cursor()
            for i in range(len(list[0:6])):
                print(i, list[i])
            parameter = input("Choose a parameter to update an employee:")
            if parameter == "0":
                name = input("Name:")
                new_name = input("New name:")
                cursor.execute(
                    f"UPDATE EMPLOYEES SET name = '{new_name}' where name= '{name}' "
                )
            elif parameter == "1":
                surname = input("Surname:")
                new_surname = input("New surname:")
                cursor.execute(
                    f"UPDATE EMPLOYEES SET surname = '{new_surname}' where surname= '{surname}' "
                )
            elif parameter == "2":
                job_desc = input("Description:")
                new_desc = input("New description:")
                cursor.execute(
                    f"UPDATE EMPLOYEES SET job_desc = '{new_desc}' where job_desc= '{job_desc}' "
                )
            elif parameter == "3":
                employee_id = input("ID:")
                new_id = input("New ID:")
                cursor.execute(
                    f"UPDATE EMPLOYEES SET employee_id = '{new_id}' where employee_id= '{employee_id}' "
                )
            elif parameter == "4":
                age = input("Age:")
                new_age = input("New age:")
                cursor.execute(
                    f"UPDATE EMPLOYEES SET age = '{new_age}' where age= '{age}' "
                )
            elif parameter == "5":
                driving_license = input("License:")
                new_license = input("New age:")
                cursor.execute(
                    f"UPDATE EMPLOYEES SET driving_license = '{new_license}' where driving_license= '{driving_license}' "
                )

            else:
                OPTIONS.UPDATE()


while True:
    option = input("1.Open database \n2.Exit\nSelect:")
    if option == "1":
        OPTIONS.CREATE_DATABASE()
        print("Database has been opened")
        print(f"Currently on {database}")
        choice = input(
            "1.Add employee\n2.Delete employee\n3.Show employees\n4.Update info\n5.Return to menu \n6.Exit\nSelect:"
        )

        if choice == "1":
            OPTIONS.ADD_DATA()
        elif choice == "2":
            OPTIONS.DELETE()
        elif choice == "3":
            OPTIONS.SHOW()
        elif choice == "4":
            OPTIONS.UPDATE()
        elif choice == "5":
            continue
        elif choice == "6":
            print("Closing the program")
            print("...")
            break
    elif option == "2":
        break
    else:
        continue
