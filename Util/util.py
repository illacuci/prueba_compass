from PIL import ImageTk, Image

def read_image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))
    

def clean_windows(root):
    list = root.pack_slaves()
    for i in list:
        i.pack_forget()
