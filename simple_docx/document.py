

from zipfile import ZipFile, is_zipfile
import xml.etree.ElementTree as ET
from .xml import is_tag_match
#import re


class Document:
    def __init__(self, path):

        self.docXml = ""
        self.relsXml = ""
        self.paragraphs = []
        self.mediaFiles = {}

        self.load(path)

        if self.is_loaded():
            self.paragraphs = self.collect_p_elems(self.docXml)


    def load(self, path):
        """ reads files from docx
        reads document.xml to docXml
        reads document.xml.rels to relsXml
        reads word/media folder files to mediaFiles """
        if is_zipfile(path) != False:
            try:
                z = ZipFile(path)
                # extract relevant xml
                self.docXml = z.read('word/document.xml')
                self.relsXml = z.read('word/_rels/document.xml.rels')
                # extract media
                names = z.namelist()
                for name in names:
                    if name.startswith('word/media/'):
                        filename = name.split('/')[-1]
                        self.mediaFiles[filename] = z.read(name)
                z.close()
            except:
                z.close()


    def is_loaded(self):
        return self.docXml != ""


    def collect_p_elems(self, xml):
        paragraphs = []
        root = ET.fromstring(xml) # w:document
        for child in root: # w:body, could it be something else?
            for grandchild in child: # children could be p or sections stuff
                if is_tag_match(grandchild, 'p'):
                    paragraphs.append(grandchild)
        return paragraphs



                

        

        