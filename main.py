import sqlite3
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


def delete1():
    try:
        sqlite_connection = sqlite3.connect('hotels.db')
        cursor = sqlite_connection.cursor()
        print("Підключено до SQLite")

        sqlite_select_query = """DELETE ALL from busket"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()  # отримання всіх записів таблиці

        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Зєднання з SQLite закрите")

def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('hotels.db')
        cursor = sqlite_connection.cursor()
        print("Підключено до SQLite")

        sqlite_select_query = """SELECT * from busket"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()  # отримання всіх записів таблиці

        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Зєднання з SQLite закрите")

def read_sqlite_table1():
    try:
        sqlite_connection = sqlite3.connect('hotels.db')
        cursor = sqlite_connection.cursor()
        print("Підключено до SQLite")

        sqlite_select_query = """SELECT DISTINCT name FROM busket;"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()  # отримання всіх записів таблиці

        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Зєднання з SQLite закрите")





@app.route('/')
def main():
    return render_template('index.html')


@app.route('/busket')
def hello_world2():
    data = read_sqlite_table()
    data1 = read_sqlite_table1()
    print(data1)
    food = []
    number = 1
    for i in data1:
        repeat = 0
        price = 0
        for g in data:
            if g[1] == i[0]:
                repeat +=1
                price = g[2]
        food.append((number,i[0],price,repeat))
    count = [i+1 for i in range(len(data1))]
    print(food)
    return render_template("Busket.html", data=food, count=count)

@app.route('/basa', methods=["POST"])
def add_hotel():
    name = request.form['title']
    price = request.form['price-weight']
    print(name, price)
    conn = sqlite3.connect('hotels.db')
    c = conn.cursor()
    c.execute('''
            INSERT INTO busket (name,price) VALUES (?, ?)
        ''', (name, price))
    conn.commit()
    conn.close()
    return render_template("Busket.html")

@app.route('/delete')
def delete():
        with sqlite3.connect("hotels.db") as connection:
            cursor = connection.cursor()
            print(1)
            cursor.execute("DELETE FROM busket;")
            print(2)
            connection.commit()

        return render_template("index.html")

@app.route('/delete/<int:id>', methods=['POST'])
def delete1(id):
        with sqlite3.connect("hotels.db") as connection:
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM busket WHERE id='{id}'")

            connection.commit()

        return render_template("index.html")

@app.route('/pizza')
def main1():
    return send_file("pizza.html")


@app.route('/sushi')
def main2():
    return render_template("sushi.html")


@app.route('/salats')
def main3():
    return render_template("salats.html")


@app.route('/gariachistravi')
def main4():
    return render_template("gariachistravi.html")


@app.route('/garnirs')
def main5():
    return render_template("garnirs.html")


if __name__ == '__main__':
    app.run(port=32000, debug=True)
