books = []

users = {}

def add_book(book_id, title, author, copies):
    books.append((book_id, title, author, copies))
    print(f'Book "{title}" added to the library.')
    
    
def register_user(user_id, user_name):
    if user_id not in users:
        users[user_id] = (user_name, [])
        print(f'User "{user_name}" registered successfully.')
        
    else:
        print("User ID already exists.")
        
        
def borrow_book(user_id, book_id):
    if user_id not in users:
        print("User not found. Please register first.")
        return
    
    for i, (id, title, author, copies) in enumerate(books):
        if id == book_id:
            if copies > 0:
                
                books[i] = (id, title, author, copies - 1)
                
                users[user_id][1].append(book_id)
                print(f'User "{users[user_id][0]}" borrowed "{title}".')
                
            else:
                print("No copies available.")
            return
    print("Book not found.")
    
    
def return_book(user_id, book_id):
    if user_id not in users:
        print("User not found.")
        return
    
    if book_id not in users[user_id][1]:
        print("User hasn't borrowed")