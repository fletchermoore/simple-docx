import unittest
from simple_docx.document import Document
import simple_docx.xml as Xml
import xml.etree.ElementTree as ET


class XmlTestCase(unittest.TestCase):
    def test_tag_matches(self):
        """ is_tag_matches can determine tag by the suffix without namespace """
        doc = Document('sampleDoc.docx')
        root = ET.fromstring(doc.docXml)
        firstChild = root[0] # should be body tag
        print(firstChild.tag)
        self.assertTrue(Xml.is_tag_match(firstChild, 'body'))

    def test_get_value(self):
        """ get_attr_val can extract the attribute value of a namespaced elem """
        doc = Document('sampleDoc.docx')
        firstP = doc.paragraphs[0]
        attr = 'rsidR'
        expected_value = '00B06BB5'
        found_value = Xml.get_attr_val(firstP, attr)
        self.assertEqual(found_value, expected_value)
