import sqlite3

DATABASE = "cars.db"
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

plate = input("Enter a number plate: ")

cursor.execute("SELECT * FROM car WHERE plate = ?", (plate,))
results = cursor.fetchall()

for car in results:
    print(f"{car[0]}")


like_plate = f"%{plate}%"
cursor.execute("SELECT * FROM car WHERE plate LIKE ?", (like_plate,))
results = cursor.fetchall()

for car in results:
    print(f"{car[0]} {car[1]:20} {car[2]}")
