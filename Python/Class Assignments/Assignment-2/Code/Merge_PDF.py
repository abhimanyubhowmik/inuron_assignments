from PyPDF2 import PdfFileMerger
import PDF_Logging

logging = PDF_Logging.pdf_logging()

class PDF_Merger:

    def __init__(self, file_path,pdf_list) -> None:
        self.file_path = file_path
        self.pdf_list = pdf_list
        
    def merge_pdf(self):
        try:
            pdfs = []
            for i in self.pdf_list:
                pdfs.append(str(self.file_path) +'/' + str(i))
            
            merger = PdfFileMerger(strict=False)

            for pdf in pdfs:
                merger.append(pdf)

            merger.write(str(self.file_path)+"/result.pdf")
            merger.close()
        except Exception as e:
            logging.error(e)
