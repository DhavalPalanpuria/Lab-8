"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path
import pandas as pd 
import csv

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    cursor.execute('''
    SELECT person1.name, person2.name, start_date, type FROM relationship 
    JOIN people person1 on person1 = person1.id
    JOIN people person1 on person2 = person2.id
    WHERE type = 'spouse';
    '''
    )
    all_relationship = cursor.fetchall()
    con.commit
    con.close
    return

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    married_couples = ['name1', 'name2', 'anniversary']
    with open('married_couples.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(married_couples)
    
    return

if __name__ == '__main__':
   main()