from pdf2docx import Converter
pdf = 'C:/Users/jsssa/Documents/UNISYS THREAT LOCK.pdf'
docx = 'C:/Users/jsssa/Documents/UNISYS THREAT LOCK.docx'
cv = Converter(pdf)
cv.convert(docx)
cv.close()