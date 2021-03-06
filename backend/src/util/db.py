import datetime
import os
import psycopg2

def create_users_table():
    DATABASE_URL = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS "Users" (
            id varchar(255) NOT NULL PRIMARY KEY,
            phone_number varchar(255),
            api_key varchar(255)
        );
    """

    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_user_details(id, api_key, phone_number):
    DATABASE_URL = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    sql = """
        INSERT INTO "Users" (id, api_key, phone_number)
            VALUES (%s, %s, %s)
        ON CONFLICT (id)
            DO UPDATE SET api_key = %s, phone_number = %s;
    """

    try:
        cursor.execute(sql, (id, api_key, phone_number, api_key, phone_number))
        conn.commit()
    except Exception as e:
        print(e)

def get_user_api_key(phone_number):
    print("get_user_api_key(), params => phone number:", phone_number)

    DATABASE_URL = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    sql = """
    SELECT api_key FROM public."Users"
    WHERE phone_number = %s
    """
    val = (phone_number,)
    
    try:
        cursor.execute(sql, val)
        return cursor.fetchone()

    except Exception as e:
        print(e)

def create_event_table():
    DATABASE_URL = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    sql = """ CREATE TABLE IF NOT EXISTS public."Event" (
    id SERIAL NOT NULL PRIMARY KEY,
    scheduled_at timestamp without time zone NOT NULL,
    api_key character varying(250) NOT NULL
    ) """
    
    try:
        cursor.execute(sql)
        
        # commit the changes
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        return str(error)

# returns an array of the events from the DB!
def get_events_api_key():
    DATABASE_URL = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    sql = """SELECT id, api_key FROM public."Event" WHERE scheduled_at < NOW() - INTERVAL '15 minutes'"""
    # val = (datetime.datetime.now() - datetime.timedelta(minutes=30))

    cursor.execute(sql)

    results = cursor.fetchall()

    conn.close()

    return results

def post_event(scheduled_at, api_key):
    try:
        DATABASE_URL = os.getenv("DATABASE_URL")

        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()

        cursor.execute(""" 
        INSERT INTO public."Event" (
        scheduled_at,
        api_key
        ) VALUES (%s, %s)""", (scheduled_at, api_key))

        # commit the changes
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        return str(error)


def delete_events(id):
    try:
        DATABASE_URL = os.getenv("DATABASE_URL")

        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM public."Event"
        WHERE id = %s;
        """, (id,))

        # commit the changes
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        return str(error)
