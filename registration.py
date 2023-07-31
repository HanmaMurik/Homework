import sqlite3
connection = sqlite3.connect('database.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, num TEXT, loc TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT, pr_name TEXT, pr_amount INTEGER, pr_price REAL, pr_des TEXT, pr_photo TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, user_product TEXT, product_quantity INTEGER, total REAL);')

def register(id, name, num, loc):
    sql.execute('INSERT INTO users VALUES(?, ?, ?, ?);', (id, name, num, loc))
    connection.commit()


def checker(id):
    check = sql.execute('SELECT id FROM users WHERE id=?;', (id,))
    if check.fetchone():
        return True
    else:
        return False



