import unittest
import app
import pymysql


class AppTests(unittest.TestCase):

    def test_SQL_fatch(self):
        query="SELECT amount FROM money_track.spendings WHERE ID =2;"
        result = app.display_spendings(query)
        self.assertEqual(result, 89)

    def test_SQL_value(self):
        self.assertRaises(pymysql.err.ProgrammingError, app.display_spendings, "koko")

    def test_SQL_insert(self):
        pass

    def test_SQL_update(self):
        pass

    def test_SQL_connect(self):
        pass


if __name__ == "__main__":
    unittest.main()
