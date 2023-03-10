##  Questions...

"""
1. In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?
2. From a PdfFileReader object, how do you get a Page object for page 5?
3. What PdfFileReader variable stores the number of pages in the PDF document?
4. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do
before you can obtain Page objects from it?
5. What methods do you use to rotate a page?
6. What is the difference between a Run object and a Paragraph object?
7. How do you obtain a list of Paragraph objects for a Document object that’s stored in a 
variable named doc?
8. What type of object has bold, underline, italic, strike, and outline variables?
9. What is the difference between False, True, and None for the bold variable?
10. How do you create a Document object for a new Word document?
11. How do you add a paragraph with the text &#39;Hello, there!&#39; to a Document object 
stored in avariable named doc?
12. What integers represent the levels of headings available in Word documents?

"""

## Answers....

"""
1. The PdfFileReader() and PdfFileWriter() File objects should be opened in read-binary 
('rb') and write-binary ('wb') modes, respectively.

------------------------------------------------------------------------------------------

2. To get a Page object for page 5 from a PdfFileReader object, you can use the 
getPage() method and pass it the page number as an argument: 
page_five = pdf_reader.getPage(4) (remember that pages are zero-indexed).

------------------------------------------------------------------------------------------

3. The numPages variable stores the number of pages in the PDF document for a 
PdfFileReader object: num_pages = pdf_reader.numPages

------------------------------------------------------------------------------------------

4. If a PdfFileReader object’s PDF is encrypted with the password 'swordfish', you 
must call the decrypt() method and pass the password as an argument before you can 
obtain Page objects from it: pdf_reader.decrypt('swordfish')

------------------------------------------------------------------------------------------

5. To rotate a page, you can use the rotateClockwise() or rotateCounterClockwise() 
method on a Page object: page.rotateClockwise(90) will rotate the page 90 degrees clockwise.

------------------------------------------------------------------------------------------

6. A Paragraph object represents a single paragraph of text, while a Run object 
represents a contiguous run of text with the same formatting.

------------------------------------------------------------------------------------------

7. To obtain a list of Paragraph objects for a Document object stored in a variable 
named doc, you can use the doc.paragraphs attribute: paragraphs = doc.paragraphs

------------------------------------------------------------------------------------------

8. A Run object has bold, underline, italic, strike, and outline variables.

------------------------------------------------------------------------------------------

9. False means the formatting is not applied, True means the formatting is applied, 
and None means that the value is inherited from the style hierarchy.

------------------------------------------------------------------------------------------

10.To create a Document object for a new Word document, you can use the docx.Document() 
constructor: doc = docx.Document()

------------------------------------------------------------------------------------------

11. To add a paragraph with the text 'Hello, there!' to a Document object stored in a 
variable named doc, you can use the add_paragraph() method: doc.add_paragraph('Hello, there!')

------------------------------------------------------------------------------------------

12. The integers 0-8 represent the levels of headings available in Word documents, 
with 0 being the Title style and 1-8 representing Heading 1 through Heading 8.

------------------------------------------------------------------------------------------



"""