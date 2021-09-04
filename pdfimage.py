from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog

import os.path

def browse():
	global filename
	filename = filedialog.askopenfilename(filetypes=(("pdf files","*.pdf"),("All files","*.*")))
	text_box1.delete(0, "end")
	text_box1.insert(0, filename)

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


# Init App
app = Tk()

# App Title
app.title('PDF to Image Converter')

# Label
Label(app, text="File Location").grid(row=0, sticky=W, padx=10)



# Text Box
text_box1 = Entry(app, width=40)
text_box1.grid(row=0, column=1)

btn_browse = ttk.Button(app, text="Browse file", command=browse)
btn_browse.grid(row=0, column=2, padx=5, pady=5)


# Convert Button
btn_convert = ttk.Button(app, text="Convert", command=pdf2img)
btn_convert.grid(row=0, column=3, padx=5, pady=5)

# App Exit Button
btn_exit = ttk.Button(app, text="Exit", command=app.quit)
btn_exit.grid(row=0, column=4, padx=5, pady=5)

# Run App
app.mainloop()
