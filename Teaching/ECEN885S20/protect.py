import PyPDF2 as p,os



path = os.getcwd()+"/Teaching/ECEN885S20/"
files = os.listdir(path)
files =sorted(files)

print(files)

for file_ in files:
    if file_.endswith(".pdf"):
        input_stream = p.PdfFileReader(open(path+file_, "rb"))
        output = p.PdfFileWriter()
        for i in range(0, input_stream.getNumPages()):
            output.addPage(input_stream.getPage(i))

        outputstream = open(path+"protected/"+file_, "wb")

        output.encrypt("ECEN885S20", use_128bit=True)
        output.write(outputstream)
        outputstream.close()