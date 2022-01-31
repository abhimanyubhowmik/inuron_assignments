import os
import PDF_Logging



logging = PDF_Logging.pdf_logging()

class File_Maneger:

    def __init__(self, file_path) -> None:
        self.file_path = file_path

            
    def file_finder(self):
        try:
            path = os.listdir(self.file_path)
            out = ''
            for i in path:
                out +=  str(i) + "\n"
            return out
        except Exception as e:
            logging.error(e)


    def pdf_finder (self):
        try:
            path = os.listdir(self.file_path)
            pdf = []
            for i in path:
                if(i[-4::] == ".pdf"):
                    pdf.append(i)
            return pdf
        except Exception as e:
            logging.error(e)



