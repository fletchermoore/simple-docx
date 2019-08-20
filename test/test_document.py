import unittest
from simple_docx.document import Document

class DocumentTestCase(unittest.TestCase):

    def test_alert_is_test(self):
        """Document alerts "test"?"""
        doc = Document()
        self.assertEqual(doc.alert(), "test")


if __name__ == '__main__':
    unittest.main()

