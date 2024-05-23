import customtkinter as ctk
from UI.backend import handle_import


def add_elements(root):

    action_frame = ctk.CTkFrame(root)
    action_frame.grid_columnconfigure(0, weight=1)
    action_frame.grid_columnconfigure(1, weight=1)

    data_frame = ctk.CTkScrollableFrame(root)

    import_btn = ctk.CTkButton(action_frame, text="Import", command=lambda: handle_import(data_frame))
    export_btn = ctk.CTkButton(action_frame, text="Export", fg_color="#fc2003", hover_color="#d11a02")

    import_btn.grid(row=0, column=0, sticky="we", padx=20)
    export_btn.grid(row=0, column=1, sticky="we", padx=20)

    action_frame.pack(fill="x")
    data_frame.pack(fill="both", expand=True)


def setup():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.title("u.gg Scraper")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    add_elements(root)

    root.mainloop()
