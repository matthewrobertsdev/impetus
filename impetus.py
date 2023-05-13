from tkinter import *
  
root = Tk()
root.title('impetus')
root.minsize(400,400)
root.wm_attributes("-transparent", True)
output_display = Text(root);
output_display.pack(side="top", fill=BOTH, expand=True)
output_display.configure(state=DISABLED, insertbackground='#00ff00', \
                         highlightcolor='#00ff00')
bottom_frame = Frame(root, width=400, height=40)
bottom_frame.pack(fill=X, side="bottom", expand=False)
command_entry = Text(bottom_frame, width=60, height=7);
command_entry.pack(fill=X, expand=False)
command_entry.configure(insertbackground='#00ff00', blockcursor=True, \
                        highlightcolor='#00ff00', fg='#00ff00')
command_entry.focus_set()
root.mainloop()
