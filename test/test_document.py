import unittest
from simple_docx.document import Document
import xml.etree.ElementTree as ET

class DocumentTestCase(unittest.TestCase):
    def test_sampleDoc_unzips(self):
        """ xml string from .docx file is extracted and read """
        doc = Document('sampleDoc.docx')
        self.assertNotEqual(doc.docXml, "")

    def test_sampleDoc_rels_found(self):
        """ rels file is successfully extracted """
        doc = Document('sampleDoc.docx')
        self.assertNotEqual(doc.relsXml, "")

    def test_invalidFile_fails(self):
        """ given invalid file, it fails gracefully """
        doc = Document('gibberishish')
        self.assertEqual(doc.docXml, "")

    def test_extracts_media(self):
        """ given docx with media, reads those into dict """
        doc = Document('sampleDoc.docx')
        self.assertNotEqual(doc.mediaFiles, {})

    def test_collect_p_elems(self):
        """ assert all paragraph elements found for sample doc """
        doc = Document('sampleDoc.docx')
        l = len(doc.paragraphs)
        #print(l)
        self.assertEqual(l, 18)

    def test_extracts_rels(self):
        """ relationships are properly imported """
        doc = Document('sampleDoc.docx')
        self.assertEqual(doc.rels['rId5'][1], "media/image1.png")

    def test_get_image(self):
        """ can retreive image data by rId """
        doc = Document('sampleDoc.docx')
        # probably better to assert it is some kind of binary
        self.assertNotEqual(doc.get_image('rId5'), None)



if __name__ == '__main__':
    unittest.main()

