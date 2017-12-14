def delete_frame(frame):
    for widget in frame.winfo_children():
        widget.grid_forget()
