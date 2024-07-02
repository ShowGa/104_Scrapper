import tkinter as tk
from tkinter import messagebox
from scraper import try_scrap

# action function when clicking button
def tk_scrap_buttom():
    url = entry.get()
    job_info = try_scrap(url)
    messagebox.showinfo("Job info", job_info)

# create window
root = tk.Tk()
root.title("Job Scraper")
root.geometry("400x200")

# create input box and button
tk.Label(root, text="Job URL:").pack(pady=10) 
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
tk.Button(root, text="Scrape", command=tk_scrap_buttom).pack(pady=20)

# execute the program
root.mainloop()

# try_scrap("https://www.104.com.tw/job/7eki0?jobsource=m_index_job_c")