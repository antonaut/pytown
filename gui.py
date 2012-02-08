#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import gtk

class PyDBWin:
    
    def __init__(self):
        self.mainWin = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.mainWin.connect("delete_event",self.delete_event)
        self.mainWin.connect("destroy",self.destroy)
        self.mainWin.set_border_width(10)
        self.mainWin.show()


    def main(self):
        gtk.main()
    
    def delete_event(self,widget,event,data=None):
        return False

    def destroy(self,widget,data=None):
        gtk.main_quit()


if __name__ == "__main__":
    win = PyDBWin()
    win.main()
    
