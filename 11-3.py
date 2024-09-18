import sqlite3

conn = sqlite3.connect('movies.db')
conn.text_factory = str
curs = conn.cursor()

def execute_select(curs, sql, params):
	curs.execute(sql, (params,))
	row = curs.fetchone()
	result=[]
	if row!=None:
		result.append(row)
		for row in curs:
			result.append(row)
	return result

movieSelect = ''' select movies.name, casts.role from movies, casts, people
 where casts.movie_id=movies.id and
casts.person_id=people.id and
people.name like ?'''

actor = input("Enter name:")
result = execute_select(curs, movieSelect, actor)
for movie in result:
	print(movie[0],"as", movie[1])
