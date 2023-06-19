import PyPDF2

pdf = ""  # Initialize the variable to store the extracted text
pdf_file_path = 'pdf_file.pdf'  # Replace with the actual path to your PDF file
with open(pdf_file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Get the total number of pages in the PDF
    num_pages = len(reader.pages)
    print(num_pages)
    # Extract text from each page
    for page_number in range(num_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        pdf += text
    
    print(pdf)