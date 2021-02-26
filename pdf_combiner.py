import PyPDF2

# storing the pdf file we are reading into an object
myPDF1 = open('/users/user/desktop/file1.pdf','rb')

# reading our file object
reader1 = PyPDF2.PdfFileReader(myPDF1)


# display the number of pages in the document

print(reader1.numPages)

# combining current document with another
myPDF2 = open('/users/user/desktop/file2.pdf','rb')
reader2 = PyPDF2.PdfFileReader(myPDF2)

# writer object to write the read files 1 and 2
writer = PyPDF2.PdfFileWriter()

# for loop to write all the pages of both files
for pages in range(reader1.numPages):
    page = reader1.getPage(pages)
    writer.addPage(page)
# each iteration add a page to the pdf

for pages in range(reader2.numPages):
    page = reader2.getPage(pages)
    writer.addPage(page)

# file object to export the combined file to hard drive
combined = open('/users/user/desktop/combined.pdf','wb')

# writing it down and closing the project
writer.write(combined)
combined.close()


