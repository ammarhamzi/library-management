import sys
from services import add_customer, add_book_rental, list_overdue_rentals, list_customers, update_penalty, update_customer_details, return_book, list_customer_books, get_current_rentals, validate_date

def main_menu():
    while True:
        update_penalty()

        print("\nWelcome to Library Management System:")
        print("1. Add Customer")
        print("2. Add Book Rental")
        print("3. List Customers")
        print("4. List Current Rentals")
        print("5. List Overdue Rentals")
        print("6. Return Book")
        print("7. Edit Customer Details")
        print("8. Exit")

        if len(sys.argv) > 1:
            choice = sys.argv[1]
        else:
            choice = input("Please enter your choice (1-8): ")

        if choice == '1':
            if len(sys.argv) == 5:
                name, address, contact_no = sys.argv[2], sys.argv[3], sys.argv[4]
            else:
                name = input("Enter customer name: ")
                address = input("Enter customer address: ")
                contact_no = input("Enter customer contact number: ")
            add_customer(name, address, contact_no)
            print("Customer added successfully.")
        elif choice == '2':
            if len(sys.argv) == 7:
                customer_id, book_name, author_name, rental_date, due_date = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
            else:
                customer_id = input("Enter customer ID: ")
                book_name = input("Enter book name: ")
                author_name = input("Enter author name: ")
                while True:
                    rental_date = input("Enter rental date (DD-MM-YYYY): ")
                    if validate_date(rental_date):
                        break
                    print("Invalid date format. Please use DD-MM-YYYY.")
                while True:
                    due_date = input("Enter due date (DD-MM-YYYY): ")
                    if validate_date(due_date):
                        break
                    print("Invalid date format. Please use DD-MM-YYYY.")
            add_book_rental(customer_id, book_name, author_name, rental_date, due_date)
            update_penalty()
            print("Book rental added successfully.")
        elif choice == '3':
            customers = list_customers()
            if not customers:
                print('')
                print('---------------------------------------------------------------')
                print("No customers found.")
            else:
                print('')
                print('---------------------------------------------------------------')
                for customer in customers:
                    print(f'Customer ID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}, Contact: {customer[3]}, Penalty Amount: {customer[4]}')
                    print('---------------------------------------------------------------')
        elif choice == '4':
            current_rentals = get_current_rentals()
            if not current_rentals:
                print('')
                print('---------------------------------------------------------------')
                print("No current rentals found.")
            else:
                print('')
                print('---------------------------------------------------------------')
                for rental in current_rentals:
                    print(f'Customer ID: {rental[0]}, Name: {rental[1]}, Address: {rental[2]}, Contact: {rental[3]}')
                    print(f'Book Name: {rental[4]}, Author: {rental[5]}, Rental Date: {rental[6]}, Due Date: {rental[7]}')
                    print('---------------------------------------------------------------')
        elif choice == '5':
            update_penalty()
            print('')
            print('---------------------------------------------------------------')
            overdue_rentals = list_overdue_rentals()
            if not overdue_rentals:
                print("End of List.")
            else:
                print('')
                print('---------------------------------------------------------------')
                for rental in overdue_rentals:
                    print(f'Customer ID: {rental[0]}, Name: {rental[1]}, Address: {rental[2]}, Contact: {rental[3]}')
                    print(f'Book Name: {rental[4]}, Author: {rental[5]}, Rental Date: {rental[6]}, Due Date: {rental[7]}, Penalty: {rental[8]}')
                    print('---------------------------------------------------------------')
        elif choice == '6':
            if len(sys.argv) == 4:
                customer_id, book_id = sys.argv[2], sys.argv[3]
            else:
                customer_id = input("Enter customer ID: ")
                book_id = input("Enter book ID to return: ")
            return_book(customer_id, book_id)
            print('---------------------------------------------------------------')
            print("Book returned successfully.")
            print('---------------------------------------------------------------')
        elif choice == '7':
            if len(sys.argv) == 5:
                customer_id, name, address, contact_no = sys.argv[2], sys.argv[3], sys.argv[4]
            else:
                customer_id = input("Enter customer ID to edit details: ")
                name = input("Enter new customer name: ")
                address = input("Enter new customer address: ")
                contact_no = input("Enter new customer contact number: ")
            update_customer_details(customer_id, name, address, contact_no)
            print('---------------------------------------------------------------')
            print("Customer details updated successfully.")
            print('---------------------------------------------------------------')
        elif choice == '8':
            print('---------------------------------------------------------------')
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main_menu()
