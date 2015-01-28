#!/usr/bin/python
from gi.repository import Gtk, Gdk, Pango, GObject

# TODO: Write GUI version of CLI

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="New Window")
        self.set_border_width(10)
        self.set_default_size(600, 500)
        self.connect("delete-event", Gtk.main_quit)
        
        self.update()

    def update(self):
        self.show_all()

win = Window()
Gtk.main()
