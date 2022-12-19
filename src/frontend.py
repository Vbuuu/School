"""This is the main Frontend with login Ui"""

from tkinter import Tk
from components import Btn, TextField, TextType
import main


def start():
  """Starts the ui"""
  def validateLogin():
    """Validates username and password"""
    if username.textVar.get() == "Max" and password.textVar.get() == "Max":
      bgWindow.destroy()
      fgWindow.destroy()

  def close():
    pass
  # LoginForm
  fgWindow = Tk()
  fgWindow.title("Login")
  fgWindow.attributes("-topmost", 1)

  # Background
  bgWindow = Tk()
  bgWindow.title("Barrier")
  bgWindow.attributes("-topmost", 2)
  bgWindow.attributes("-fullscreen", True)
  bgWindow.attributes("-disabled", True)
  bgWindow.attributes("-alpha", 0.2)
  bgWindow.configure(background="darkgray")

  # Init Components
  username = TextField(fgWindow, "Username", TextType.NORMAL)
  password = TextField(fgWindow, "Password", TextType.PASSWORD)
  button = Btn(fgWindow, "Login", validateLogin)

  # Draw Components
  username.draw()
  password.draw()
  button.draw()

  bgWindow.protocol("WM_DELETE_WINDOW", close)
  fgWindow.protocol("WM_DELETE_WINDOW", close)
  bgWindow.mainloop()
  fgWindow.mainloop()


if __name__ == "__main__":
  main.main()
