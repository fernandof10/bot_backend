from __future__ import annotations
from abc import ABCMeta, abstractmethod
import sqlite3
from PIL import Image
from io import BytesIO


class DataBaseInterface(metaclass=ABCMeta):
    '''
    The data collected from the cloud can be stored locally
    using different ways (e.g pickle files, excel, sqlite, mysql etc.)
    In this case, we will use the factory-method design pattern where
    each concrete class is an interface type.
    '''

    @abstractmethod
    def get_bots(self) -> dict:
        pass

    @abstractmethod
    def get_bot_by_id(self, str: bot_id) -> dict:
        pass

    @abstractmethod
    def add_bot(self, str: bot_id, bot_name) -> None:
        pass

    @abstractmethod
    def update_bot(self, str: bot_id, bot_name) -> None:
        pass

    @abstractmethod
    def delete_bot(self, str: bot_id) -> None:
        pass

    @abstractmethod
    def get_message_by_id(self, str: message_id) -> dict:
        pass

    @abstractmethod
    def get_message_by_conversation_id(self, str: conversation_id) -> dict:
        pass

    @abstractmethod
    def add_message(self, str: conversation_id, message_id, from_point, to_point, text) -> None:
        pass


class SqlInterface(DataBaseInterface):

    def __init__(self, db_file_path):
        self.db_file_path = db_file_path

    def create_connection(self):
        """ create a database connection to the db_file_path
        :param df_file_path: database file path
        :return: connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file_path)
        except sqlite3.Error as error:
            print(error)
        return conn

    def get_bots(self):
        sql_query = f'''SELECT "id", "name"
                FROM "bots";'''
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        tables = [{'id':x[0], 'name':x[1]} for x in cur.fetchall()]
        conn.close()
        return tables

    def get_bot_by_id(self, bot_id):
        sql_query = f'''SELECT "id", "name"
                FROM "bots" WHERE "id" == "{bot_id}";'''
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        table = [{'id':x[0], 'name':x[1]} for x in cur.fetchall()]
        conn.close()
        return table

    def add_bot(self, bot_id, bot_name):
        sql_query = f'INSERT INTO bots("id", "name") VALUES(?,?)'
        conn = self.create_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_query, [bot_id, bot_name])
            conn.commit()

        except sqlite3.Error as error:
            error = ';'.join(error.args)
            if 'UNIQUE' in error:
                print(f'bot {bot_id} already exists. Consider using update_bot method')
            result = False
        else:
            result = True
        conn.close()
        return result
        
    def update_bot(self, bot_id, new_bot_name):
        conn = self.create_connection()
        cur = conn.cursor()
        sql_query = f'UPDATE bots SET "name"="{new_bot_name}" WHERE id == "{bot_id}";'
        try:
            cur.execute(sql_query)
            conn.commit()
        except:
            print(f'Failed to update bot {bot_id}')
            result = False
        else:
            print(f'Successfully updated bot {bot_id}, with the name {new_bot_name}')
            result = True
        conn.close()
        return result

    def delete_bot(self, bot_id):
        conn = self.create_connection()
        cur = conn.cursor()
        sql_query = f'DELETE FROM bots WHERE id == "{bot_id}";'
        try:
            cur.execute(sql_query)
            conn.commit()
        except:
            print(f'Failed to delete bot {bot_id}')
            result = False
        else:
            print(f'Successfully deleted bot {bot_id}')
            result = True
        conn.close()
        return result

    def get_message_by_id(self, message_id):
        sql_query = f'''SELECT "id", "conversationId", "timestamp", "from", "to", "text"
                FROM "messages" WHERE "id" == "{message_id}";'''
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        table = [{'id': x[0], 'conversationId': x[1],
                  "timestamp": x[2], "from": x[3],
                  "to": x[4], "text":x[5]} for x in cur.fetchall()]
        conn.close()
        return table

    def get_message_by_conversation_id(self, conversation_id):
        sql_query = f'''SELECT "id", "conversationId", "timestamp", "from", "to", "text"
                FROM "messages" WHERE "conversationId" == "{conversation_id}";'''
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        table = [{'id': x[0], 'conversationId': x[1],
                  "timestamp": x[2], "from": x[3],
                  "to": x[4], "text":x[5]} for x in cur.fetchall()]
        conn.close()
        return table

    def add_message(self, message_id, conversation_id, timestamp, from_point, to_point, text):
        sql_query = f'''INSERT INTO messages("id", "conversationId", "timestamp",
                        "from", "to", "text")
                        VALUES(?,?,?,?,?,?)'''
        conn = self.create_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_query, [message_id, conversation_id, timestamp, from_point, to_point, text])
            conn.commit()

        except sqlite3.Error as error:
            error = ';'.join(error.args)
            if 'UNIQUE' in error:
                print(f'message {message_id} already exists.')
            result = False
        else:
            result = True
        conn.close()
        return result

if __name__ == '__main__':

    def test_get_bots(interface):
        result = interface.get_bots()
        print(result)

    def test_add_bot(interface, bot_id, bot_name):
        result = interface.add_bot(bot_id, bot_name)
        print(result)

    def test_update_bot(interface, bot_id, new_bot_name):
        interface.update_bot(bot_id, new_bot_name)

    def test_get_bot_by_id(interface, bot_id):
        result = interface.get_bot_by_id(bot_id)
        print(result)

    def test_add_message(interface, message_id, conversation_id, timestamp, from_point, to_point, text):
        result = interface.add_message(message_id, conversation_id, timestamp, from_point, to_point, text)
        print(result)

    def test_get_message_by_id(interface, message_id):
        result = interface.get_message_by_id(message_id)
        print(result)

    def test_get_message_by_conversation_id(interface, conversation_id):
        result = interface.get_message_by_conversation_id(conversation_id)
        print(result)

    def test_delete_bot(interface, bot_id):
        result = interface.delete_bot(bot_id)
        return result


    interface = SqlInterface('sqlite_database.db')
    test_add_bot(interface, "36b9f842-ee97-11e8-9443-0242ac120002", "Aureo")
    test_update_bot(interface, "36b9f842-ee97-11e8-9443-0242ac120002", "Dureo")
    test_get_bots(interface)
    test_get_bot_by_id(interface, "36b9f842-ee97-11e8-9443-0242ac120002")
    test_delete_bot(interface, "36b9f842-ee97-11e8-9443-0242ac120002")
    test_add_message(interface, 'mid-1', 'cid-1', 'time1', 'f-1', 'to-1', 'text1')
    test_get_message_by_id(interface, 'mid-1')
    test_get_message_by_conversation_id(interface, 'cid-1')
