
import sqlite3

conn = sqlite3.connect('dz8.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO countries (title) VALUES
 ('Кыргызстан'), ('Китай'), ('Германия')
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY(country_id) REFERENCES countries(id)
    )
''')

cursor.execute('''

    INSERT INTO cities (title, area, country_id) VALUES
        ('Бишкек', 100, 1),
        ('Ош', 80, 1),
        ('Берлин', 891.8, 3),
        ('Пекин', 16411, 2),
        ('Мюнхен', 310.7, 3),
        ('Шанхай', 6340.5, 2),
        ('Франкфурт', 248.3, 3)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY(city_id) REFERENCES cities(id)
)
''')


cursor.execute('''
    INSERT INTO students (first_name, last_name, city_id) VALUES
        ('Иван', 'Иванов', 1),
        ('Петр', 'Петров', 2),
        ('Сидор', 'Сидоров', 3),
        ('Алексей', 'Алексеев', 4),
        ('Дмитрий', 'Дмитриев', 1),
        ('Данила', 'Сарапулов', 2),
        ('Кирилл ', 'Сарапулов', 5),
        ('Александр', 'Сергеевич', 4),
        ('Дмитрий', 'Анатольев', 3)
''')

conn.commit()



def get_students_by_city():

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    # Получаем список городов с их id
    cursor.execute('SELECT id, title FROM cities GROUP BY title;')
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}: {city[1]}")  # Выводим id и название города

    # Ввод id города пользователем
    city_id = input("Введите id города: ")
    if city_id == '0':
        print("Выход из программы.")
        conn.close()
        return

    # Получаем информацию об учениках в выбранном городе
    cursor.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    GROUP BY students.first_name, students.last_name;
    ''', (city_id,))
    rows = cursor.fetchall()

    # Вывод информации об учениках
    if rows:
        print("\nИнформация об учениках:")
        for row in rows:
            print(f"Имя: {row[0]}, Фамилия: {row[1]}, Страна: {row[2]}, Город: {row[3]}, Площадь: {row[4]} км²")
    else:
        print("Нет учеников в данном городе.")

    conn.close()

if __name__ == '__main__':
    get_students_by_city()

conn.close()