"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime
from random import random, choice
import random

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    connect = sqlite3.connect('social_network.db')
    cursor = connect.cursor()
    relationship_table = '''
    CREATE TABLE IF NOT EXISTS relationship
    (
        person1 INTEGER PRIMARY KEY,
        person2 INTEGER NOT NULL,
        start_date DATE NOT NULL,
        type TEXT NOT NULL
        );
    '''
    cursor.execute(relationship_table)
    connect.commit()
    connect.close()

    # TODO: Function body
    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    connect = sqlite3.connect('social_network.db')
    cursor = connect.cursor()
    fake = Faker()
    for a in range(100):
        person1 = random.randint(1,100)
        person2 = random.randint(1,100)
        while person2 == person1:
            person2 = random.randint(1,100)
        type = choice(('Friend','Spouse','Partner','Relative'))
        start_date = fake.date_between(start_date='-50y', end_date='today')
    cursor.execute('INSERT INTO relationship (person1, person2, start_date, type) VALUES (?, ?, ?, ?)', (person1, person2, type, start_date))
    connect.commit()
    connect.close()
    return 

if __name__ == '__main__':
   main()