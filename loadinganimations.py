import time
from tkinter import Tk, Canvas

def loading_animation():
    global current_slice

    canvas.delete("all")

    canvas.create_text(100, 50, text=f"Loading {current_slice}%", font=("Arial", 18))

    slice_width = 30
    fill_level = (current_slice / 100) * canvas.winfo_width()  # Adjust width for canvas size

    canvas.create_rectangle(0, 80, fill_level, 100, fill="green")

    current_slice = (current_slice + 1) % 101

    root.after(20, loading_animation)

print("""Loading animation options:
  1. Simple
  2. Basic graphical""")

choice = int(input("Pick one (the corresponding number): "))

if choice == 1:
    animation = "|/-\\"

    for i in range(100):
        print("\r" + animation[i % len(animation)], end="")

    print("\nDone!")

if choice == 2:
    root = Tk()
    root.title("Loading Animation")
    canvas = Canvas(root, width=300, height=120)
    canvas.pack()
    current_slice = 0

    loading_animation()
    root.mainloop()
