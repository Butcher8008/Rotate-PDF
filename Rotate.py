import PyPDF2
import shutil

pdf_path = input("Enter PDF name: ")
rotate_right = 'r'
rotate_left = 'l'
rotate_bottom = 'b'
rotate_top = 't'

# Get user input for page numbers and rotation angles
# num_pages = int(input("Enter the number of pages: "))
# page_to_rotate = []

# for i in range(num_pages):
#     page_number = int(input(f"Enter page number for rotation (1-{num_pages}): "))
#     rotate_angle = input(f"Enter rotation angle for page {page_number} ({rotate_right}/{rotate_left}/{rotate_bottom}/{rotate_top}): ").lower()
#     page_to_rotate.append((page_number, rotate_angle))
#     print(page_to_rotate)

def rotate(page_to_rotate, pdf_path, rotate_right, rotate_left, rotate_bottom, rotate_top):
    pdf_open = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_open)
    pdf_writer = PyPDF2.PdfWriter()

    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]

        for page_to_rotate_number, rotate_angle in page_to_rotate:
            if page_number + 1 == page_to_rotate_number:

                if rotate_angle == rotate_right:
                    page.rotate(90)
                elif rotate_angle == rotate_left:
                    page.rotate(270)
                elif rotate_angle == rotate_bottom:
                    page.rotate(180)
                elif rotate_angle==rotate_top:
                    page.rotate(360)

        pdf_writer.add_page(page)

    pdf_output = open('output.pdf', 'wb')
    pdf_writer.write(pdf_output)

    pdf_open.close()
    pdf_output.close()

    shutil.move('output.pdf', pdf_path)

rotate([(3,'b')], pdf_path, rotate_right, rotate_left, rotate_bottom, rotate_top)
