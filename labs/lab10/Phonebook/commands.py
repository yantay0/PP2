import csv
import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='madina2626'
)

current = config.cursor()
data = []


sql = '''
      INSERT INTO Phonebook
      VALUES(%s,%s,%s) RETURNING *;
'''


print('SELECT:', '1-Add new number', '2-Update',
      '3-Delete', '4 - Change order', sep="\n")

choice = int(input())


if choice == 1:
   #DETAIL:  Primary key "(id)=(n)" already exist
   try:
    with open(r'C:\Users\Madina\Desktop\PP2\labs\lab10\data.csv') as f:
     rows = csv.reader(f, delimiter=',')
     for row in rows:
       row[0] = int(row[0])
     data.append(row)
    for row in data:
     current.execute(sql, row)

   except:
    id = int(input('ID: '))
    name = input('NAME: ')
    number = input('PHONE NUMBER: ')
    current.execute(sql, (id, name, number))

   print('Operation completed successfully')

if choice == 2:
  print('ID:')
  chosen_id = int(input())
  print('CHANGE: ', '1-Name', '2-Phone number', sep='\n')
  data = update = int(input())

  if update == 1:
   print("Please input new name: ")
   data = new_number = input()
   sql = '''
       UPDATE Phonebook SET name = %s WHERE id = %s;
 '''
   print('Operation completed successfully')
  elif update == 2:
   print("Please input updated phone number: ")
   data = new_name = input()
   sql = '''
      UPDATE Phonebook SET phone_number = %s WHERE id = %s;
 '''
   print('Operation completed successfully')
  else:
     print('ERROR')
  current.execute(sql, (data, chosen_id))
  config.commit()

if choice == 3:
 print("Delete by:", '1-Phone_number', '2-Name', sep='\n')
 choice = int(input())
 if choice == 1:
   number = input('PHONE NUMBER: ')
   chosen_id = input('ID: ')
   sql = '''
  delete from Phonebook  where name = %s
 '''
 if choice == 2:
   data = name = input('NAME: ')
   chosen_id = input('ID: ')
   sql = '''
  delete from Phonebook  where name = %s
 '''
 current.execute(sql, (chosen_id))
 config.commit()

if choice == 4:
 print('Output Query by: ', '1 - Alphabet order',
       '2 - Reverse order by id', sep='\n')
 order = int(input())
 if order == 1:
  postgreSQL_select_Query = "select * from Phonebook order by name asc"
 if order == 2:
   postgreSQL_select_Query = "select * from Phonebook order by id desc"
 current.execute(postgreSQL_select_Query, (id))
 contacts = current.fetchall()
 for row in contacts:
     print("id = ", row[0], )
     print("name = ", row[1])
     print("phone_number  = ", row[2])


current.close()
config.commit()
config.close()
