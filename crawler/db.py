# -*- coding:utf-8 –*-

import psycopg2

# Connect to an existing database

def get_db_connection():
	return psycopg2.connect(host = 'localhost', port = 5432, user = 'postgres', password = 'qwe123', database = 'postgres')


def insert(conn,data):
	# Open a cursor to perform database operations
	cur = conn.cursor()

	# Execute a command: this creates a new table
	#cur.execute("CREATE TABLE test1 (id serial PRIMARY KEY, num integer, data varchar);")

	# Pass data to fill a query placeholders and let Psycopg perform
	# the correct conversion (no more SQL injections!)

	for item in data:
		sql = "INSERT INTO products ("+",".join(item.keys()) +") VALUES ("+",".join('%s' for value in item.values() )+")"
		#print sql
		cur.execute(sql, [value for value in item.values()])

	# Query the database and obtain data as Python objects

	# Make the changes to the database persistent
	conn.commit()
	cur.close()

# Close communication with the database


