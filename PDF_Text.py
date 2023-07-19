import fitz

pdf = fitz.Document("Test PDF file.pdf")
page = pdf[0]
text = page.get_textpage().extractText().encode("utf-8")

out = open("output.txt", "wb") # create a text output
out.write(text) # write text of page
out.write(bytes((12,))) # write page delimiter (form feed 0x0C)

out.close()
