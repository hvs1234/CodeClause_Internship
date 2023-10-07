import tkinter as tk
from difflib import SequenceMatcher

def check_plagiarism():
    text1 = entry1.get("1.0", "end-1c")
    text2 = entry2.get("1.0", "end-1c")

    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    result_label.config(text=f"Similarity Ratio: {similarity_ratio * 100:.2f}%")
    
app = tk.Tk()
app.title("Plagiarism Checker")
app.resizable(False,False)
app.configure(bg='black')

img1 = tk.PhotoImage(file="E:\\pyImages\\cyber.png")
app.iconphoto(False,img1)

entry1_label = tk.Label(app, text="Text 1:",bg="black",fg="white",font=("Calibri",18))
entry1_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry1 = tk.Text(app, height=10, width=100,bg="black",fg="aqua",font=("Calibri",18),wrap="word")
entry1.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

entry2_label = tk.Label(app, text="Text 2:",bg="black",fg="white",font=("Calibri",18))
entry2_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry2 = tk.Text(app, height=10, width=100,bg="black",fg="aqua",font=("Calibri",18),wrap="word")
entry2.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

check_button = tk.Button(app, text="Check Plagiarism",bg="black",fg="yellow", command=check_plagiarism,font=("Algerian",18),activebackground="black",activeforeground="yellow",relief="groove")
check_button.grid(row=3, column=0, columnspan=3, pady=10)

result_label = tk.Label(app, text="",bg="black",fg="lime",font=("Calibri",18))
result_label.grid(row=4, column=0, columnspan=3)

app.mainloop()
