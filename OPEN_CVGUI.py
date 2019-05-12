from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
import cv2

class OPEN_CV():
    def __init__(self,master):
        self.master = master
        self.master.title("OPEN CV")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Load Image",command = self.loadimg)
        self.file_menu.add_command(label = "Save Image",command = self.saveimg)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.show_menu = Menu(self.menu,tearoff =0)
        self.show_menu.add_command(label = "Show Image",command = self.showimg)
        self.show_menu.add_command(label = "Show Gray")
        self.show_menu.add_command(label = "Show HSV")
        self.show_menu.add_command(label = "Show LAB")
        self.menu.add_cascade(label = "Show",menu = self.show_menu)
        
        self.show_histogram = Menu(self.menu,tearoff = 0)
        self.show_histogram.add_command(label = "Grayscale Histograms")
        self.show_histogram.add_command(label = "Color Histograms")
        self.show_histogram.add_command(label = "Histogram Equalization")
        self.menu.add_cascade(label = "Histograms",menu = self.show_histogram)
        
        self.rotation_menu = Menu(self.menu,tearoff = 0)
        self.rotation_menu.add_command(label = "45 Degrees")
        self.rotation_menu.add_command(label = "90 Degrees")
        self.rotation_menu.add_command(label = "180 Degrees")
        self.menu.add_cascade(label = "Rotation",menu = self.rotation_menu)
        
        '''
        self.resize_menu = Menu(self.menu,tearoff = 0)
        self.resize_menu.add_command(label = )
        '''
        
        self.shape_menu = Menu(self.menu,tearoff = 0)
        self.shape_menu.add_command(label  = "Show Width",command = self.showwidth)
        self.shape_menu.add_command(label = "Show Height",command = self.showheight)
        self.shape_menu.add_command(label = "Show Channels",command = self.showchannels)
        self.menu.add_cascade(label = "Shape",menu= self.shape_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.about_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.master.config(menu=self.menu)
        
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
    
    def loadimg(self):
        global img
        global imgr
        img = filedialog.askopenfilename(initialdir="/",title="Select image file",
                                                   filetypes=(("image files","*.jpg"),("all files","*.*")))
        imgr = cv2.imread(img)
    
    def showimg(self):
        imgr = cv2.imread(img)
        cv2.imshow("Image",imgr)
    
    def showwidth(self):
        msg.showinfo("Width","Width:"+str(imgr.shape[1]))
    
    def showheight(self):
        msg.showinfo("Height","Height"+str(imgr.shape[0]))
    
    def showchannels(self):
        msg.showinfo("Number of Channels","Channels"+str(imgr.shape[2]))
    
    def saveimg(self):
        pass
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def aboutmenu(self):
        msg.showinfo("About","OPEN CV \nVersion 1.0")
    
    def helpmenu(self):
        pass
    
def main():
    root=Tk()
    OC = OPEN_CV(root)
    root.mainloop()
    
if __name__=='__main__':
    main()