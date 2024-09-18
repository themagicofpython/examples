import sqlite3
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
curs = conn.cursor()
query = 'SELECT * FROM Customer'
print(query)
print(sqlite3.apilevel)
curs.execute(query)
row = curs.fetchone()

if row != None:
	firstname, lastname = row[1], row[2]
	print(firstname,lastname)

for row in curs:
	print("firstname: %s, lastname: %s, company: %s, address: %s, city: %s, state: %s, country: %s" % (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

curs.execute("insert into Customer(firstname, lastname,email) values (?, ?,?)",("Gerhard", "Haering","blabla@abv.bg"))
conn.commit()
conn.close()
