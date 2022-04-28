import psycopg2 ,os

config = psycopg2.connect(
 host = 'localhost',
 database = 'postgres',
 user = 'postgres',
 password = 'madina2626'
)


current = config.cursor()
#current.execute("UPDATE Phonebook SET id INTEGER PRIMARY KEY")
current.execute(
 
'''
CREATE TABLE Phonebook(
 id INTEGER PRIMARY KEY,
 name VARCHAR(50),
 phone_number VARCHAR(20)
);
''')

config.commit()
current.close()
config.close()