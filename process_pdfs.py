import os

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


def pdf_drop_last(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()

    for page in range(pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
        if page == (pdf.getNumPages() - 2):
            break

    output_filename = "{}_.pdf".format(fname)
    with open(output_filename, "wb") as out:
        pdf_writer.write(out)

    print("Created: {}".format(output_filename))


def pdf_get_last(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()

    for page in range(pdf.getNumPages()):
        if page == (pdf.getNumPages() - 1):
            pdf_writer.addPage(pdf.getPage(page))

    output_filename = "{}_.pdf".format(fname)
    with open(output_filename, "wb") as out:
        pdf_writer.write(out)

    print("Created: {}".format(output_filename))


def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()

    for path in input_paths:
        pdf_merger.append(path)

    with open(output_path, "wb") as fileobj:
        pdf_merger.write(fileobj)


if __name__ == "__main__":
    path = "big1.pdf"
    pdf_drop_last(path)
    path = "big2.pdf"
    pdf_get_last(path)
    paths = ["page1.pdf", "page2.pdf"]
    merger("merged.pdf", paths)
