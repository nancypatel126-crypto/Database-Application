
import database


# Create Database Table
database.create_table()


def main():

    while True:

        print("\n================================")
        print("    DATABASE MANAGEMENT SYSTEM")
        print("================================")

        print("1. Insert Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            city = input("Enter City: ").strip()

            try:
                age = int(input("Enter Age: "))

                if not name or not email or not city or age < 0:
                    print("Please enter valid details!")
                    continue

                database.insert_record(
                    name, email, age, city
                )

            except ValueError:
                print("Age must be a number!")

        elif choice == "2":

            database.view_records()

        elif choice == "3":

            try:
                record_id = int(input("Enter Record ID: "))
                database.search_record(record_id)

            except ValueError:
                print("Invalid ID!")

        elif choice == "4":

            try:
                record_id = int(input("Enter Record ID: "))

                name = input("Enter New Name: ").strip()
                email = input("Enter New Email: ").strip()
                city = input("Enter New City: ").strip()
                age = int(input("Enter New Age: "))

                if not name or not email or not city or age < 0:
                    print("Invalid details!")
                    continue

                database.update_record(
                    record_id, name, email, age, city
                )

            except ValueError:
                print("Please enter valid values!")

        elif choice == "5":

            try:
                record_id = int(input("Enter Record ID: "))
                database.delete_record(record_id)

            except ValueError:
                print("Invalid ID!")

        elif choice == "6":

            print("Thank you for using Database Management System!")
            break

        else:

            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
