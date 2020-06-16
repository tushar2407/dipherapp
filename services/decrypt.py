from PyPDF2 import PdfFileReader,PdfFileWriter
from tempfile import TemporaryFile
import shutil
import os
from cipher.settings import MEDIA_ROOT
import urllib.request
def decrypt(content):
    a=content
    b=[]
    for i in a:
        l=ord(i)
        l-=13
        i=chr(l)
        b.append(i)
    s=''
    s=s.join(b)
    return s
def decrypt1(file_in, password,file_out):
    #file_in='C:\\Users\\Tushar\\projects\\django\\cipher\\cipher'+file_in
    file_in=MEDIA_ROOT+'/'+file_in.strip('/media/')
    #file_in='https://dipher.herokuapp.com'+file_in
    #try:
    document_in = PdfFileReader(open(file_in, 'rb'))
    if document_in.isEncrypted:
        while True:
            matched = document_in.decrypt(password)
            if matched:
                document_out = PdfFileWriter()
                document_out.cloneReaderDocumentRoot(document_in)
                #tmp_file = tools.create_temp_file()
                document_out.write(open(file_out, 'wb'))
                shutil.copy(file_out, file_in)
                os.remove(file_out)
                return True
            return True
    #except:
    #    return False 
    return False