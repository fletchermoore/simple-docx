import unittest
from simple_docx.paragraph import Paragraph
from simple_docx.document import Document
import xml.etree.ElementTree as ET


sampleXml = """<w:p w14:paraId="6866CFFC" w14:textId="23B3221B" w:rsidR="008B6084" w:rsidRDefault="008B6084" w:rsidP="008B6084">
            <w:pPr>
                <w:pStyle w:val="ListParagraph"/>
                <w:numPr>
                    <w:ilvl w:val="1"/>
                    <w:numId w:val="1"/>
                </w:numPr>
            </w:pPr>
            <w:r>
                <w:t>we</w:t>
            </w:r>
        </w:p>"""


class ParagraphTestCase(unittest.TestCase):

    def test_parse_ilvl(self):
        """ correctly determine ilvl in simple case """
        doc = Document('sampleDoc.docx')
        first_p_elem = doc.paragraphs[0]
        paragraph = Paragraph(first_p_elem)
        self.assertEqual(paragraph.ilvl, 0)

    def test_parse_text(self):
        """ correctly determine text in simple case """
        doc = Document('sampleDoc.docx')
        first_p_elem = doc.paragraphs[0]
        paragraph = Paragraph(first_p_elem)
        self.assertEqual(paragraph.text, "subject")


if __name__ == '__main__':
    unittest.main()