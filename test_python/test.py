import sqlite3

conn = sqlite3.connect('store__db.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2) NOT NULL,
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
)
''')


def insert_data():

    cursor.execute("SELECT COUNT(*) FROM store")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO store (store_id, title) VALUES (1, 'Asia')")
        cursor.execute("INSERT INTO store (store_id, title) VALUES (2, 'Globus')")
        cursor.execute("INSERT INTO store (store_id, title) VALUES (3, 'Spar')")

    cursor.execute("SELECT COUNT(*) FROM categories")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO categories (code, title) VALUES ('FD', 'Food products')")
        cursor.execute("INSERT INTO categories (code, title) VALUES ('EL', 'Electronics')")
        cursor.execute("INSERT INTO categories (code, title) VALUES ('CL', 'Clothes')")


    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (1, 'Chocolate', 'FD', 10.5, 129, 1)")
        cursor.execute(
            "INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (2, 'Jeans', 'CL', 120.0, 55, 2)")
        cursor.execute(
            "INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (3, 'T-Shirt', 'CL', 110.0, 10, 1)")

    conn.commit()


insert_data()


def display_stores():
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")
    print()


def display_products(store_id):
    query = """
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print()
    else:
        print("Нет продуктов в данном магазине.\n")


def main():
    while True:
        display_stores()

        try:
            store_id = int(input("Введите id магазина для отображения продуктов или 0 для выхода: "))
            if store_id == 0:
                print("Выход из программы.")
                break
            display_products(store_id)
        except ValueError:
            print("Пожалуйста, введите корректный номер магазина.")


if __name__ == "__main__":
    main()

conn.close()
