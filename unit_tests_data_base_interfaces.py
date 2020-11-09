from data_base_interfaces import SqlInterface
import unittest

unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y,x)

interface = SqlInterface('sqlite_database.db')

class TestSqlInterface(unittest.TestCase):

    def test_01(self):
        #_add_bot
        self.assertEqual(interface.add_bot('36b9f842-ee97-11e8-9443-0242ac120002', 'Aureo'), True)
        self.assertEqual(interface.add_bot('77b9f842-ee97-11e8-9443-0242ac120002', 'Bureo'), True)

    def test_02(self):
        #_02_update_bot
        self.assertEqual(interface.update_bot('36b9f842-ee97-11e8-9443-0242ac120002', 'Aaureo'), True)

    def test_03(self):
        #_get_bots
        self.assertEqual(interface.get_bots()[1], {'id': '77b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Bureo'})

    def test_04(self):
        #_get_bot_by_id
        self.assertEqual(interface.get_bot_by_id("77b9f842-ee97-11e8-9443-0242ac120002"), {'id': '77b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Bureo'})

    def test_05(self):
        #delete_bot
        self.assertEqual(interface.delete_bot("77b9f842-ee97-11e8-9443-0242ac120002"), True)

