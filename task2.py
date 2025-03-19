pages = 140
rows_per_page = 52
chars_per_row = 48
total_chars = pages * rows_per_page * chars_per_row
bytes_per_char = 2
total_bytes = total_chars * bytes_per_char
print(f"Кількість інформації для збереження книги: {total_bytes} байт")

cd_capacity = 700 * 1024 * 1024
num_books = cd_capacity // total_bytes
print(f"Кількість книг, які помістяться на компакт-диск: {num_books}")