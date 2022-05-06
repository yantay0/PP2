import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='madina2626'
)

current = config.cursor()


def check(name):
    select = '''
            SELECT phone_number FROM phonebook WHERE name = %s;
    '''
    current.execute(select, [name])
    DICT = current.fetchone()
    if DICT == None:
        return True
    else:
        return False


print("SELECT:", "1-Insert", "2-Delete", "3-Pagination", "4-Query", sep="\n")

choice = int(input())


if choice == 1:
 #upgrade:
    upd = '''
        create or replace procedure update(id integer,username varchar, phone_number varchar)
        as
        $$
            begin
                UPDATE phonebook 
                SETphone_number = $2 
                WHERE name = $1;
            end;
        $$ language plpgsql;
        call update(%s,%s,%s);
    '''
    #insert:
    insert = '''
        create or replace procedure insert(id integer,name varchar, phone_number varchar)
        as
        $$
            begin
                insert into phonebook(id,name, phone_number) values ($1, $2,$3);
            end; 
        $$ language plpgsql; 
        call insert(%s,%s,%s);
    '''

    print("How many people you would like to add?")
    n = int(input())
    for _ in range(0, n):
        id = int(input())
        name = str(input())
        number = str(input())
        if(check(name)):
            current.execute(insert, (id, name, number))
        else:
            current.execute(upd, (id, name, number))


if choice == 2:
    #delete:
    delete = '''
        create or replace procedure delete(data varchar)
        as
        $$
            begin
                delete from phonebook where id = $1 or name = $1  or phone_number = $1; 
            end;
        $$ language plpgsql;
        call delete(%s);
    '''

    data = str(input())
    current.execute(delete, [data])


if choice == 3:
    print("type your limit and offset")
    limit = int(input())
    offset = int(input())
    pa = '''
        select * from phonebook offset %s limit %s;
    '''
    current.execute(pa, (limit, offset))
    print(current.fetchall())


if choice == 4:
    #querying:
    query = '''
        create or replace function querying(data varchar)
            returns table (
                namee varchar,
                phonenumberr varchar
            )
        as
        $$
            begin
                return query
                    select * from phonebook where name ilike $1 or phone_number ilike $1 or id ilike $1;
            end;
        $$ language plpgsql;

        select querying(%s);
    '''

    pat = str(input())
    current.execute(query, ["%"+pat+"%"])
    print(current.fetchall())


current.close()
config.commit()
config.close()
