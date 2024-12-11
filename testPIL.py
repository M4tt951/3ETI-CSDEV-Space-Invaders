from pil import Image, ImageTk
import tkinter as tk

root = tk.Tk()
image = Image.open("path_to_image.jpg")  # Remplacez par le chemin d'une image valide
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.image = photo
label.pack()

root.mainloop()

