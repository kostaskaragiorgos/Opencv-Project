from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog

import matplotlib.pyplot as plt
import cv2
import numpy as np

class OPEN_CV():
    def __init__(self,master):
        self.master = master
        self.master.title("OPEN CV")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.img = ""
        self.imgr = ""
        self.flagfile = 0
        # menu
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Load Image",accelerator = 'Alt+O',command = self.loadimg)
        self.file_menu.add_command(label = "Save Image",accelerator = 'Ctrl+S',command = self.saveimg)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.show_menu = Menu(self.menu,tearoff =0)
        self.show_menu.add_command(label = "Show Image",accelerator = 'Ctrl+F5',command = self.showimg)
        self.show_menu.add_command(label = "Show Gray",accelerator = 'Ctrl+G',command = self.showgr)
        self.show_menu.add_command(label = "Show HSV",accelerator  = 'Ctrl+F9',command = self.showhsv)
        self.show_menu.add_command(label = "Show LAB",accelerator = 'Ctrl + L',command = self.showlab)
        self.menu.add_cascade(label = "Show",menu = self.show_menu)
        
        self.show_histogram = Menu(self.menu,tearoff = 0)
        self.show_histogram.add_command(label = "Grayscale Histograms",accelerator = 'Alt + H',command = self.grhisto)
        self.show_histogram.add_command(label = "Color Histograms",accelerator = 'Alt + C',command = self.colrhisto)
        self.show_histogram.add_command(label = "Histogram Equalization",accelerator = 'Alt + E',command = self.histoequal)
        self.menu.add_cascade(label = "Histograms",menu = self.show_histogram)
        
        self.rotation_menu = Menu(self.menu,tearoff = 0)
        self.rotation_menu.add_command(label = "45 Degrees",accelerator = 'Ctrl + 4',command = self.dec45)
        self.rotation_menu.add_command(label = "90 Degrees",accelerator = 'Ctrl + 9',command = self.dec90)
        self.rotation_menu.add_command(label = "180 Degrees",accelerator ='Ctrl + R',command = self.dec180)
        self.menu.add_cascade(label = "Rotation",menu = self.rotation_menu)
        
        self.resize_menu = Menu(self.menu , tearoff = 0)
        self.resize_menu.add_command(label = "25% smaller")
        self.resize_menu.add_command(label = "50% smaller")
        self.resize_menu.add_command(label = "75% smaller")
        self.resize_menu.add_command(label = "Custom size")
        self.menu.add_cascade(label = "Resize",menu = self.resize_menu)
        
        self.shape_menu = Menu(self.menu,tearoff = 0)
        self.shape_menu.add_command(label  = "Show Width",accelerator ='Ctrl + W',command = self.showwidth)
        self.shape_menu.add_command(label = "Show Height",accelerator = 'Ctrl + H',command = self.showheight)
        self.shape_menu.add_command(label = "Show Channels",accelerator = 'Ctrl + C',command = self.showchannels)
        self.menu.add_cascade(label = "Shape",menu= self.shape_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.about_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.master.config(menu=self.menu)
        
        #file menu 
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Alt-o>',lambda event: self.loadimg())
        self.master.bind('<Control-s>',lambda event: self.saveimg())
        
        #show menu
        self.master.bind('<Control-F5>',lambda event:self.showimg())
        self.master.bind('<Control-g>',lambda event:self.showgr())
        self.master.bind('<Control-F9>',lambda event:self.showhsv())
        self.master.bind('<Control-l>',lambda event:self.showlab())
        
        #histogram
        self.master.bind('<Alt-h>',lambda event:self.grhisto())
        self.master.bind('<Alt-c>',lambda event:self.colrhisto())
        self.master.bind('<Alt-e>',lambda event:self.histoequal())
        
        #rotation
        self.master.bind('<Control-4>',lambda event:self.dec45())
        self.master.bind('<Control-9>',lambda event:self.dec90())
        self.master.bind('<Control-R>',lambda event:self.dec180())
        
        #shape menu
        self.master.bind('<Control-w>',lambda event:self.showwidth())
        self.master.bind('<Control-h>',lambda event:self.showheight())
        self.master.bind('<Control-c>',lambda event:self.showchannels())
        
        #about menu
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
    
    def loadimg(self):
        self.img = filedialog.askopenfilename(initialdir="/",title="Select image file",
                                        filetypes=(("image files","*.jpg"),("all files","*.*")))
        if self.img.endswith('.jpg'):
            self.flagfile = 1

            self.imgr = cv2.imread(self.img)
        else:
            self.flagfile = 0
    
    def showimg(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            self.imgr = cv2.imread(self.img)
            cv2.imshow("Image",self.imgr)
    
    def dec45(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
        else:
            (h,w) = self.imgr.shape[:2]
            center = (w//2,h//2)
            M = cv2.getRotationMatrix2D(center,45,1.0)
            rotated = cv2.warpAffine(self.imgr,M,(w,h))
            cv2.imshow("Rotated by 45 Dec",rotated)
            
    def dec90(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            (h,w) = self.imgr.shape[:2]
            center = (w//2,h//2)
            M = cv2.getRotationMatrix2D(center,90,1.0)
            rotated = cv2.warpAffine(self.imgr,M,(w,h))
            cv2.imshow("Rotated by 90 Dec",rotated)
            
    
    def dec180(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            (h,w) = self.imgr.shape[:2]
            center = (w//2,h//2)
            M = cv2.getRotationMatrix2D(center,180,1.0)
            rotated = cv2.warpAffine(self.imgr,M,(w,h))
            cv2.imshow("Rotated by 180 Dec",rotated)
    
    def grhisto(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
        else:
            hist = cv2.calcHist([self.imgr],[0],None,[256],[0,256])
            plt.figure()
            plt.title("Grayscale Histogram")
            plt.plot(hist)
            plt.show()
    
    def colrhisto(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
        else:
            chans = cv2.split(self.imgr)
            colors = ("b","g","r")
            plt.figure()
            plt.title("Color Histogram")
            for (chan , color) in zip(chans , colors):
                hist = cv2.calcHist([chan],[0],None,[256],[0,256])
                plt.plot(hist , color = color)
                plt.xlim([0,256])
            plt.show()
            
    def histoequal(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
        else:
            imGC = cv2.cvtColor(self.imgr,cv2.COLOR_BGR2GRAY)
            eq  = cv2.equalizeHist(imGC)
            cv2.imshow("Histogram Equalization",np.hstack([imGC,eq]))
    
    
    def showgr(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
        else:
            imGC = cv2.cvtColor(self.imgr,cv2.COLOR_BGR2GRAY)
            cv2.imshow("GRAY",imGC)
            if msg.askyesno("Save Gray image","Do you want to save the image?") == True:
                print("save")
            else:
                msg.showwarning("NOT SAVED","The image is not saved")
            
    def showhsv(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
        else:
            hsv = cv2.cvtColor(self.imgr,cv2.COLOR_BGR2HSV)
            cv2.imshow("HSV",hsv)
            if msg.askyesno("Save HSV image","Do you want to save the image?") == True:
                print("save")
            else:
                msg.showwarning("NOT SAVED","The image is not saved")
                
    def showlab(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            lab = cv2.cvtColor(self.imgr,cv2.COLOR_BGR2LAB)
            cv2.imshow("L*A*B",lab)
            if msg.askyesno("Save LAB image","Do you want to save the image?") == True:
                print("save")
            else:
                msg.showwarning("NOT SAVED","The image is not saved")
    
    def showwidth(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            msg.showinfo("Width","Width:"+str(self.imgr.shape[1]))
    
    def showheight(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            msg.showinfo("Height","Height"+str(self.imgr.shape[0]))
    
    def showchannels(self):
        if self.flagfile == 0 :
            msg.showerror("Error","Not image inserted")
        else:
            msg.showinfo("Number of Channels","Channels"+str(self.imgr.shape[2]))
    
    def saveimg(self):
        if self.flagfile == 0:
            msg.showerror("Error","Not image inserted")
    
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
