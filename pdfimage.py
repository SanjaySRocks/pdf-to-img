from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog
import os.path
from docx2pdf import convert
import time

def browse():
	global filename
	filename = filedialog.askopenfilename(filetypes=(("pdf files","*.pdf"),("All files","*.*")))
	text_box1.delete(0, "end")
	text_box1.insert(0, filename)

def browse_word_to_pdf():
	global filename
	filename = filedialog.askopenfilename(filetypes=(("Word files", "*.doc;*.docx"), ("All files", "*.*")))
	text_box2.delete(0, "end")
	text_box2.insert(0, filename)

def pdf2img():
	
	# Check if box is empty
	if text_box1.get() == '':
		messagebox.showinfo("Error Path", "Path is required");
		return

	# Replaces quotes from input path
	pdf_file = str(text_box1.get().replace('"', ''))

	# Check if its a valid file
	if not os.path.isfile(pdf_file):
		messagebox.showinfo("Error File", "File not found")
		return
	
	# Check if its a valid file format
	if not pdf_file.endswith('.pdf'):
		messagebox.showinfo("Error Format", "Only PDF file type supported")
		return

	# Convert
	try:
		output_file = pdf_file.replace('.pdf', '')

		images = convert_from_path(pdf_file, 500, poppler_path='poppler-0.68.0\\bin')
		for i, image in enumerate(images):
			output_img = output_file+'_'+str(i+1)+'.jpg'
			image.save(output_img, "JPEG")

	except Exception as e:
		print(e)
		messagebox.showinfo("Error", e)

	else:
		Result = f"Pdf Page Count: {len(images)} \nFile Converted Success"
		messagebox.showinfo("Result", Result)

def convert_word2pdf():
	unix_time = int(time.time())
	print(unix_time)

	print(str(text_box2.get()))

	# convert(word_file, "file.pdf")


def set_window_size(root):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate desired window size (e.g., 80% of the screen)
    window_width = int(screen_width * 0.45)
    window_height = int(screen_height * 0.2)

    # Set the window size
    root.geometry(f"{window_width}x{window_height}")

# Init App
app = Tk()

# set the app window size
set_window_size(app)

# App Title
app.title('PDF to Image Converter')

''' PDF to Image Convert '''
# Label
Label(app, text="Pdf to Image").grid(row=0, sticky=W, padx=10, pady=30)

# Text Box
text_box1 = Entry(app, width=40)
text_box1.grid(row=0, column=1)

# Browse Button
btn_browse = ttk.Button(app, text="Browse file", command=browse)
btn_browse.grid(row=0, column=2, padx=5, pady=5)

# Convert Button
btn_convert = ttk.Button(app, text="Convert", command=pdf2img)
btn_convert.grid(row=0, column=3, padx=5, pady=5)

# App Exit Button
btn_exit = ttk.Button(app, text="Exit", command=app.quit)
btn_exit.grid(row=0, column=4, padx=5, pady=5)

''' Doc to PDF Convert '''
Label(app, text="Doc to Pdf").grid(row=1, sticky=W, padx=10, pady=0)

text_box2 = Entry(app, width=40)
text_box2.grid(row=1, column=1)

# Browse Button
word2pdf_btn_browse = ttk.Button(app, text="Browse file", command=browse_word_to_pdf)
word2pdf_btn_browse.grid(row=1, column=2, padx=5, pady=5)

# Convert Button
word2pdf_btn_convert = ttk.Button(app, text="Convert", command=convert_word2pdf)
word2pdf_btn_convert.grid(row=1, column=3, padx=5, pady=5)



# Run App
app.mainloop()
