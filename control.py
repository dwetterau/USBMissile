#!/usr/bin/python
import sys
import usb.core
import time
import tkinter as tk

class LauncherDriver():
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x1941, idProduct=0x8021)
        if self.dev is None:
            raise ValueError('Missile launcher not found.')
        #if sys.platform == 'linux2' and self.dev.is_kernel_driver_active(0) is True:
        self.dev.detach_kernel_driver(0)
        self.dev.set_configuration()
        """self.handle = self.dev.open()
        try:
            self.handle.claimInterface(0)
        except:
            if e.message.find("could not claim interface") >= 0:
                self.handle.detachKernelDriver(0)
                self.handle.claimInterface(0)
        self.handle.setAltInterface(0)
        """
    def turretDown(self):
        try:
            self.dev.ctrl_transfer(0x21, 0x09, 0x200, 0, [0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        except:
            pass
    def turretRight(self):
        try:
            self.dev.ctrl_transfer(0x21, 0x09, 0x200, 0, [0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        except:
            pass
    def turretLeft(self):
        try:
            self.dev.ctrl_transfer(0x21, 0x09, 0x200, 0, [0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        except:
            pass
    def turretUp(self):
        try:
            self.dev.ctrl_transfer(0x21, 0x09, 0x200, 0, [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        except:
            pass
    def turretStop(self):
        try:
            self.dev.ctrl_transfer(0x21, 0x09, 0x200, 0, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
        except:
            pass
    def turretFire(self):
        try:
            self.dev.ctrl_transfer(0x21, 0x09, 0x200, 0, [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        except:
            pass

class Launcher():
    def __init__(self, root):
        self.launcher = LauncherDriver()
        frame = tk.Frame(root) 
        frame.master.title("Missle Control")
        frame.master.geometry("100x100")

        frame.master.bind("<KeyPress-Up>", self.up)
        frame.master.bind("<KeyRelease-Up>", self.stop)

        frame.master.bind("<KeyPress-Down>", self.down)
        frame.master.bind("<KeyRelease-Down>", self.stop)

        frame.master.bind("<KeyPress-Left>", self.left)
        frame.master.bind("<KeyRelease-Left>", self.stop)

        frame.master.bind("<KeyPress-Right>", self.right)
        frame.master.bind("<KeyRelease-Right>", self.stop)

        frame.master.bind("<KeyPress-Return>", self.shoot)
        frame.master.bind("<KeyRelease-Return>", self.stop)
        
        frame.master.bind("<KeyPress-Escape>", self.exit)
        
        frame.pack()
        self.frame = frame
    def left(self, event):
        self.frame.focus_set()
        self.launcher.turretLeft()
    def right(self, event):
        self.frame.focus_set()
        self.launcher.turretRight()
    def up(self, event):
        self.frame.focus_set()
        self.launcher.turretUp()
    def down(self, event):
        self.frame.focus_set()
        self.launcher.turretDown()
    def shoot(self, event):
        self.frame.focus_set()
        self.launcher.turretFire()
    def stop(self, event):
        self.frame.focus_set()
        self.launcher.turretStop()
    def exit(self, event):
        print("Exitting...")
        self.launcher.turretStop()
        sys.exit(0)

root = tk.Tk()
launcher = Launcher(root)
root.mainloop()
