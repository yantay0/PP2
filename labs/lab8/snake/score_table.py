import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='madina2626'
)


current = config.cursor()
#current.execute("UPDATE Phonebook SET id INTEGER PRIMARY KEY")
current.execute(

    '''
CREATE TABLE Snake(
 user_name VARCHAR(50),
 score INTEGER,
 level INTEGER,
 date VARCHAR(12)
);
''')

config.commit()
current.close()
config.close()
