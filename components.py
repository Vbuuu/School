"""Utility class for handeling the components"""

from enum import Enum
from tkinter import Button, Entry, Label, StringVar


class TextType(Enum):
  """Enum for the TextField"""

  PASSWORD = "*"
  NORMAL = ""


class Btn():
  """Advanced Button"""

  def __init__(self, window, text: str, function):
    # Initialize the Button

    self.window = window
    self.text = text
    self.function = function

  def draw(self):
    """Draw the Text Filed"""
    Button(self.window, text=self.text, command=self.function).pack()


class TextField():
  """Advanced TextField"""

  def __init__(self, window, text: str, textType: TextType):
    # Initialize the TextField
    self.window = window
    self.text = text
    self.textType = textType
    self.textVar = StringVar()

  def draw(self):
    """Draw the Text Filed"""
    Label(self.window, text=self.text).pack()
    Entry(self.window, show=self.textType.value,
          textvariable=self.textVar).pack()
