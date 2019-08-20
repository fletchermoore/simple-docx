
import xml.etree.ElementTree as ET
from .xml import is_tag_match, get_attr_val

# sampleXml = """<w:p w14:paraId="6866CFFC" w14:textId="23B3221B" w:rsidR="008B6084" w:rsidRDefault="008B6084" w:rsidP="008B6084">
#             <w:pPr>
#                 <w:pStyle w:val="ListParagraph"/>
#                 <w:numPr>
#                     <w:ilvl w:val="1"/>
#                     <w:numId w:val="1"/>
#                 </w:numPr>
#             </w:pPr>
#             <w:r>
#                 <w:t>we</w:t>
#             </w:r>
#         </w:p>"""


class Paragraph:
    def __init__(self, elem):
        self.ilvl, self.text = self.parse(elem)

    # expects ET xml for w:p tag
    # returns (int indentLevel, "textual content")
    def parse(self, pElem):
        textContent = ""
        indentLevel = -1
        for child in pElem:
            # either w:Pr, w:r, w:proofErr, w:gramErr
            if is_tag_match(child, '}r'): 
                textContent += self.parse_run(child)
            elif is_tag_match(child, '}pPr'):
                indentLevel = self.parse_indent_level(child)
            # ignore all other paragraph children for now
        return (indentLevel, textContent)


        # expect xml node for w:Pr
    # returns int indent level value or -1
    def parse_indent_level(self, prXml):
        for child in prXml:
            if is_tag_match(child, 'numPr'):
                for grandchild in child:
                    if is_tag_match(grandchild, 'ilvl'):                    
                        valStr = get_attr_val(grandchild, 'val')
                        #grandchild.get(valAttr)
                        try:
                            return int(valStr)
                        except:
                            return -1
        return -1

    # expects xml node representing w:r element
    # returns string of text contents
    def parse_run(self, rXml):
        # as far as I know, possible children include w:t and w:lastRenderedPageBreak
        text = ""
        for child in rXml:
            if is_tag_match(child, '}t'):
                text += child.text
        return text