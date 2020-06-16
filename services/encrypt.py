from PyPDF2 import PdfFileReader,PdfFileWriter
from tempfile import TemporaryFile
import shutil
import os
from cipher.settings import MEDIA_ROOT
import urllib.request
def encrypt(content):
        a=content
        b=[]
        for i in a:
                l=ord(i)
                l+=13
                i=chr(l)
                b.append(i)
        s=''
        s=s.join(b)
        return s
def encrypt1(file_in, password, file_out):
        #file_in='C:\\Users\\Tushar\\projects\\django\\cipher\\cipher'+file_in
        #try:
        file_in=MEDIA_ROOT+'/'+file_in.strip('/media/')
        #file_in='https://dipher.herokuapp.com'+file_in
        document_in = PdfFileReader(open(file_in, 'rb'))
        document_out = PdfFileWriter()
        document_out.cloneReaderDocumentRoot(document_in)
        document_out.encrypt(password)
        tmp_file=TemporaryFile()
        #tmp_file = tools.create_temp_file()
        document_out.write(open(file_out, 'wb'))
        shutil.copy(file_out, file_in)
        os.remove(file_out)
        #except :
        #    pass