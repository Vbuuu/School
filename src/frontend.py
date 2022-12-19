from tkinter import Tk
from components import Btn, TextField, TextType
import main


def start():
  def validateLogin():
    if usernameVar.getText() == "Max" and passwordVar.getText() == "Max":
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
  usernameVar = TextField(fgWindow, "Username", TextType.text)
  passwordVar = TextField(fgWindow, "Password", TextType.password)
  buttonVar = Btn(fgWindow, "Login", validateLogin)

  # Draw Components
  usernameVar.draw()
  passwordVar.draw()
  buttonVar.draw()

  bgWindow.protocol("WM_DELETE_WINDOW", close)
  fgWindow.protocol("WM_DELETE_WINDOW", close)
  bgWindow.mainloop()
  fgWindow.mainloop()


if __name__ == "__main__":
  main.main()
