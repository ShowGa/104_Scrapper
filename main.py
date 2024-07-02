import tkinter as tk
from tkinter import messagebox
from scraper import try_scrap

# action function when clicking button
def tk_scrap_buttom():
    url = entry.get()
    job_info = try_scrap(url)
    job_info_organize = (
        f"工作名稱: {job_info['工作名稱']}\n\n"
        f"公司名稱: {job_info['公司名稱']}\n\n"
        f"職務類別: {job_info['職務類別']}\n\n"
        f"工作待遇: {job_info['工作待遇']}\n\n"
        f"工作性質: {job_info['工作性質']}\n\n"
        f"上班地點: {job_info['上班地點']}\n\n"
        f"遠端工作: {job_info['遠端工作']}\n\n"
        f"上班時段: {job_info['上班時段']}\n\n"
        f"休假制度: {job_info['休假制度']}\n\n"
        f"可上班日: {job_info['可上班日']}\n\n"
        f"需求人數: {job_info['需求人數']}\n\n"
        f"工作經歷: {job_info['工作經歷']}\n\n"
        f"學歷要求: {job_info['學歷要求']}\n\n"
        f"科系要求: {job_info['科系要求']}\n\n"
        f"語文條件: {job_info['語文條件']}\n\n"
        f"擅長工具: {job_info['擅長工具']}\n\n"
        f"工作技能: {job_info['工作技能']}\n\n"
        f"其他條件: {job_info['其他條件']}"
    )
    messagebox.showinfo("Job info", job_info_organize)

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