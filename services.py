import datetime
from database import get_db_connection
from utils import calculate_penalty

def add_customer(name, address, contact_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO customers (name, address, contact_no)
                      VALUES (?, ?, ?)''', (name, address, contact_no))
    conn.commit()
    conn.close()

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def add_book_rental(customer_id, book_name, author_name, rental_date, due_date):
    if not validate_date(rental_date) or not validate_date(due_date):
        print("Invalid date format. Please use DD-MM-YYYY.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO books (customer_id, book_name, author_name, rental_date, due_date)
                      VALUES (?, ?, ?, ?, ?)''', (customer_id, book_name, author_name, rental_date, due_date))
    conn.commit()
    conn.close()

def list_overdue_rentals():
    conn = get_db_connection()
    cursor = conn.cursor()
    today = datetime.date.today()
    cursor.execute('''SELECT c.id, c.name, c.address, c.contact_no, b.book_name, b.author_name, b.rental_date, b.due_date
                      FROM customers c
                      JOIN books b ON c.id = b.customer_id''')
    overdue_rentals = cursor.fetchall()

    overdue_list = []
    for rental in overdue_rentals:
        due_date = datetime.datetime.strptime(rental[7], '%d-%m-%Y').date()
        if due_date < today:
            overdue_list.append(rental)

    if not overdue_list:
        print("End of List.")
    else:
        for rental in overdue_list:
            print(f'Customer ID: {rental[0]}, Name: {rental[1]}, Address: {rental[2]}, Contact: {rental[3]}')
            print(f'Book Name: {rental[4]}, Author: {rental[5]}, Rental Date: {rental[6]}, Due Date: {rental[7]}')
            print('------------------------------------------------')
    
    conn.close()



def list_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT id, name, address, contact_no, penalty_amount FROM customers''')
    customers = cursor.fetchall()
    conn.close()
    return customers

def update_customer_details(customer_id, name, address, contact_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE customers SET name = ?, address = ?, contact_no = ? WHERE id = ?''',
                   (name, address, contact_no, customer_id))
    conn.commit()
    conn.close()

def list_customer_books(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT id, book_name, author_name
                      FROM books
                      WHERE customer_id = ?''', (customer_id,))
    books = cursor.fetchall()
    conn.close()
    return books

def return_book(customer_id, book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''SELECT c.penalty_amount, b.due_date
                          FROM customers c
                          JOIN books b ON c.id = b.customer_id
                          WHERE c.id = ? AND b.id = ?''', (customer_id, book_id))
        penalty_data = cursor.fetchone()
        penalty_amount = penalty_data[0]
        due_date = datetime.datetime.strptime(penalty_data[1], '%d-%m-%Y').date()
        
        days_overdue = (datetime.date.today() - due_date).days
        penalty = calculate_penalty(days_overdue)
        
        new_penalty_amount = max(penalty_amount - penalty, 0)
        cursor.execute('''UPDATE customers SET penalty_amount = ? WHERE id = ?''', (new_penalty_amount, customer_id))
        
        cursor.execute('''DELETE FROM books WHERE customer_id = ? AND id = ?''', (customer_id, book_id))
        
        conn.commit()
        
    except Exception as e:
        print(f"Error returning book and updating penalty: {e}")
        conn.rollback()

    finally:
        conn.close()

def get_current_rentals():
    conn = get_db_connection()
    cursor = conn.cursor()
    today = datetime.date.today().strftime('%d-%m-%Y')
    cursor.execute('''SELECT c.id, c.name, c.address, c.contact_no, b.book_name, b.author_name, b.rental_date, b.due_date
                      FROM customers c
                      JOIN books b ON c.id = b.customer_id
                      WHERE b.due_date >= ?''', (today,))
    current_rentals = cursor.fetchall()
    conn.close()
    return current_rentals

def update_penalty():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        today = datetime.date.today()

        cursor.execute('''SELECT b.customer_id, b.due_date
                          FROM books b
                          JOIN customers c ON b.customer_id = c.id
                          WHERE b.due_date < ?''', (today.strftime('%d-%m-%Y'),))
        overdue_books = cursor.fetchall()

        penalties = {}

        for book in overdue_books:
            due_date = datetime.datetime.strptime(book[1], '%d-%m-%Y').date()
            days_overdue = (today - due_date).days
            penalty = calculate_penalty(days_overdue)

            if book[0] in penalties:
                penalties[book[0]] += penalty
            else:
                penalties[book[0]] = penalty

        for customer_id, penalty in penalties.items():
            cursor.execute('''UPDATE customers SET penalty_amount = ? WHERE id = ?''', (penalty, customer_id))

        conn.commit()

    except Exception as e:
        print(f"Error in update_penalty function: {e}")
        conn.rollback()

    finally:
        conn.close()
