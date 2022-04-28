import psycopg2 

config = psycopg2.connect(
 host = 'localhost',
 database = 'postgres',
 user = 'postgres',
 password = 'madina2626'
)


current = config.cursor()

#print("Psql version:")
current.execute(
 
'''
CREATE TABLE users(
 username VARCHAR(255),
 age INTEGER,
 registration_date DATE,
 information TEXT,
 password VARCHAR(50)
);
''')


config.commit()
config.close()