import time
from tkinter import Tk, Canvas
import os

def loading_animation(): #for option 2
    global current_slice

    canvas.delete("all")

    canvas.create_text(100, 50, text=f"{current_slice}%", font=("Arial", 18))

    slice_width = 30
    fill_level = (current_slice / 100) * canvas.winfo_width()  # Adjust width for canvas size

    canvas.create_rectangle(0, 80, fill_level, 100, fill="green")

    current_slice = (current_slice + 1) % 101

    root.after(20, loading_animation)

def loading_bar(current, total, bar_length=20):
  filled_length = int(round(bar_length * (current / total)))
  bar = '█' * filled_length + '-' * (bar_length - filled_length)
  print(f'Loading: [{bar}] {current}/{total} ({int(current / total * 100)}%)', end='\r')



while True:
  print("""Loading animation options:
    1. Simple
    2. Simple loading bar (in external window)
    3. Simple loading bar (in console)""")

  choice = int(input("Pick one (the corresponding number): "))

  if choice == 1:
      animation = ['|', '/', '-', '\\']
      a = 0
      for i in range(20):
          if a == 3:
              a=0
          print(animation[a])
          time.sleep(0.2)
          a += 1
          os.system('cls')

      print("Done!")
      time.sleep(2)
      os.system('cls')

  if choice == 2:
      root = Tk()
      root.title("Loading Animation")
      canvas = Canvas(root, width=300, height=120)
      canvas.pack()
      current_slice = 0

      loading_animation()
      root.mainloop()

  if choice == 3:
      for i in range(101):
          loading_bar(i, 100)
          time.sleep(0.05)

      print("\nDone")
