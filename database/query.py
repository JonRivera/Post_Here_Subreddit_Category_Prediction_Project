"""Makes helper function for creating, and inserting into a postgres database"""
import psycopg2

with open("secrets", "r") as file:
    secrets = [i.strip('\n') for i in file.readlines()]


def conn_curs():
    """
    makes a connection to the database dont worry these are dummy keys
    """

    connection = psycopg2.connect(dbname=secrets[4], user=secrets[4],
                                  password=secrets[5], host=secrets[6])
    cursor = connection.cursor()
    return connection, cursor


def create_table():
    """
    creates the table posts, could be more modular but we really were gonna use the entire db for one table so i saw
    no need
    """
    conn, curs = conn_curs()
    create = "CREATE TABLE posts(id SERIAL PRIMARY KEY, text TEXT NOT NULL, subreddit VARCHAR(30) NOT NULL)"
    curs.execute(create)
    conn.commit()
    return


def insert_post(text, sub):
    """
    inserts a single post into the database

    @param text: str, the title and the posts text as one string
    @param sub: text str, the subreddit this post belongs to
    """
    conn, curs = conn_curs()
    insert = f"""INSERT INTO posts (text, subreddit) VALUES ('{text}', '{sub}')"""
    curs.execute(insert)
    conn.commit()
    return


if __name__ == '__main__':
    create_table()
