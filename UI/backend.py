import customtkinter as ctk
import importer


def handle_import(frame):
    champions = importer.import_data_from_lolalytics()

    row_count = 0
    for champion in champions:
        name_label = ctk.CTkLabel(frame, text=champion.name)
        position_label = ctk.CTkLabel(frame, text=champion.position)
        winrate_label = ctk.CTkLabel(frame, text=champion.winrate)

        name_label.grid(row=row_count, column=0, sticky="we", padx=20)
        position_label.grid(row=row_count, column=1, sticky="we", padx=20)
        winrate_label.grid(row=row_count, column=2, sticky="we", padx=20)

        row_count += 1

