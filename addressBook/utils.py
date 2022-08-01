from sqlite3 import OperationalError
from conatants import *
from connection import *


def create_table():
    try:
        conn = connect_to_db('addressbook')
        conn.execute(Create_Table_Query)
        conn.commit()
        conn.close()
        print('Connected Successfully')
    except sqlite3.Error as error:
        print(error)
    finally:
        if conn:
            conn.close()
    return True


def create_address(addresses):
    try:
        conn = connect_to_db('addressbook')
        table_status = create_table()
        if table_status:
            db = conn.cursor()
            for address in addresses:
                longitude = address['longitude']
                lattitude = address['lattitude']
                insert_query = Insert_Query
                data_tuple = (longitude, lattitude)
                db.execute(insert_query, data_tuple)
            conn.commit()
            db.close()
    except sqlite3.Error as error:
        print('Connection Error', error)
    finally:
        if conn:
            conn.close()
    return 'Success'


def delete_address(addresses):
    try:
        conn = connect_to_db('addressbook')
        table_status = create_table()
        if table_status:
            for address in addresses:
                longitude = address['longitude']
                lattitude = address['lattitude']
                delete_query = Delete_Query
                db = conn.cursor()
                data_tuple = (longitude, lattitude)
                db.execute(delete_query, data_tuple)
            conn.commit()
            db.close()
    except sqlite3.Error as error:
        print('Connection Error', error)
    finally:
        if conn:
            conn.close()
    return 'Success'


def update_address(addresses):
    try:
        conn = connect_to_db('addressbook')
        table_status = create_table()
        if table_status:
            for address in addresses:
                longitude = address['longitude']
                lattitude = address['lattitude']
                new_longitude = address['new_longitude']
                new_lattitude = address['new_lattitude']
                update_query = Update_Query
                db = conn.cursor()
                data_tuple = (new_longitude, new_lattitude, longitude, lattitude)
                db.execute(update_query, data_tuple)
            conn.commit()
            db.close()
    except sqlite3.Error as error:
        return {'Connection Error': error}
    finally:
        if conn:
            conn.close()
    return 'Success'


def fetch_addresses(address, distance):
    address_list = []
    try:
        conn = connect_to_db('addressbook')
        table_status = create_table()
        if table_status:
            longitude = address['longitude']
            lattitude = address['lattitude']
            db = conn.cursor()
            db.execute(Fetch_Query)
            coordinates = db.fetchall()
            for pair in coordinates:
                x = (pair[0] - longitude)
                y = (pair[1] - lattitude)
                d = (x**2 + y**2)**(1/2)
                if d < distance:
                    address_list.append(pair)
            conn.commit()
            db.close()
    except sqlite3.Error as error:
        print('Connection Error', error)
    finally:
        if conn:
            conn.close()
    return {'Near By Addesses ': address_list}
