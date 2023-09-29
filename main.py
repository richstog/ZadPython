with open('books.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

books = []

for line in lines:
    book_info = line.strip().split('-')

    book_info[-1] = float(book_info[-1])

    books.append(book_info)

min_price = float(input("Введите минимальную цену: "))
max_price = float(input("Введите максимальную цену: "))


count_books = 0;
for book in books:
    if min_price <= book[-1] <= max_price:
        count_books += 1
        print(f"Книга: {book[0]}, Жанр: {book[1]}, Стоимость: {book[2]}")
print("Количество книг: " + str(count_books))