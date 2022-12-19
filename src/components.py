from enum import Enum
from tkinter import Button, Entry, Label, StringVar


class TextType(Enum):
  password = "*",
  text = ""


class Btn():
  def __init__(self, window, text: str, function):
    self.window = window
    self.text = text
    self.function = function

  def draw(self):
    Button(self.window, text=self.text, command=self.function).pack()


class TextField():
  def __init__(self, window, text: str, textType: TextType):
    self.window = window
    self.text = text
    self.textType = textType
    self.textVar = StringVar()

  def draw(self):
    Label(self.window, text=self.text).pack()
    Entry(self.window, show=self.textType.value,
          textvariable=self.textVar).pack()

  def getText(self):
    return self.textVar.get()
