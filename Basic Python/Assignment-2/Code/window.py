from tkinter import *
from tkinter import StringVar, ttk
from File_Search import *
from Merge_PDF import *
import PDF_Logging



logging = PDF_Logging.pdf_logging()
root = Tk()
root.title('PDF Merger')


root.geometry("800x500")
frm = ttk.Frame(root, padding=50)
frm.pack()
path = StringVar()
Output = Text(root, height = 500, width = 250,bg = "light cyan")
Output.pack()

def submit_input():
    try:
        path_var = path.get()
        file = File_Maneger(path_var)
        out = file.file_finder()
        Output.insert(END, out)
        try:
            pdf_file = file.pdf_finder()
            if len(pdf_file) == 0:
                popupmsg('No PDF Found.')
                logging.info('No PDF Found')
            elif len(pdf_file) == 1:
                popupmsg('1 PDF found at :' + path_var + '/' + pdf_file[0])
                logging.info('1 PDF Found')
            else:
                marger = PDF_Merger(path_var,pdf_file)
                marger.merge_pdf()
        except Exception as e:
            popupmsg(e)
            logging.error(e)
        else:
            popupmsg('Created a pdf at :' + path_var + '/' + 'result.pdf')
            logging.info('PDF Merged Successfully')
    except Exception as e:
        logging.error(e)



ttk.Label(frm, text="Enter the file path").pack()
ttk.Entry(frm, textvariable= path ).pack()
ttk.Button(frm, command=lambda:submit_input(),text= 'Submit').pack()

def popupmsg(msg):
    try:
        popup = Tk()
        popup.wm_title("Result")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    except Exception as e:
        logging.error(e)





root.mainloop()


