class Customer:
    def __init__(self, id, name, address, contact_no,penalty_amount):
        self.id = id
        self.name = name
        self.address = address
        self.contact_no = contact_no
        self.penalty_amount = penalty_amount

class Book:
    def __init__(self, id, customer_id, book_name, author_name, rental_date, due_date):
        self.id = id
        self.customer_id = customer_id
        self.book_name = book_name
        self.author_name = author_name
        self.rental_date = rental_date
        self.due_date = due_date
