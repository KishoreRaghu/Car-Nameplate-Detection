#!/usr/bin/env python
# coding: utf-8

# In[26]:


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
import pytesseract
import numpy as np
import random
import time
import pyautogui
from tkinter import constants

window = tk.Tk()
window.geometry("1000x3000")
window.title("Car Parking Ticketer")
speed = 20

def button_clicked():
    global button_pressed
    button_pressed = True

button_pressed = False

def quitpgrm():
    while True:
        infolabel5 = tk.Label(text="Error, Please try again", font=info2font)
        infolabel5.pack()  
        break

frame = tk.Frame(window, highlightbackground="black", highlightthickness=3)
frame.pack(fill=constants.BOTH, expand=True)

mycanvas = tk.Canvas(frame)
mycanvas.pack(fill=constants.BOTH, expand=True)

myscrollbar = ttk.Scrollbar(window, orient=constants.VERTICAL, command=mycanvas.yview)
myscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mycanvas.configure(yscrollcommand=myscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollreigon = mycanvas.bbox("all")))

frame2 = tk.Frame(mycanvas)

mycanvas.create_window((0,0), window=frame2, anchor="nw")

mainfont = ("times", 32, "bold")
mainlabel = tk.Label(master=frame2, text="Car Parking Ticketer", font=mainfont, width=25)
mainlabel.pack()

infofont = ("times", 18)
infolabel = tk.Label(master=frame2, text="Enter you car nameplate to find your car and pay for ticket", font=infofont, width=50)
infolabel.pack()

entryfont = ("Transport Medium", 22, "bold")
regentry = tk.Entry(master=frame2, text="Enter you car nameplate here", font=entryfont, width=20, justify='center')
regentry.pack()

info2font = ("Transport Medium", 15)
infolabel = tk.Label(master=frame2, text="E.g. LX09 PXR", font=info2font, width=20)
infolabel.pack()

plateinfo = regentry.get()

image2 = Image.open("cardimg.jpg")
photo2 = ImageTk.PhotoImage(image2)
#image=carfoundimg

parktime = random.randint(1,24)
amt = 0
if parktime <= 2:
    amt = amt + 1.50
elif parktime > 2 and parktime <= 4:
    amt = amt + 3
elif parktime > 4 and parktime <= 6:
    amt = amt + 4.50            
elif parktime > 6 and parktime <= 8:
    amt = amt + 6
elif parktime > 8 and parktime <= 10:
    amt = amt + 7.50
elif parktime > 10 and parktime <= 12:
    amt = amt + 9
elif parktime > 12 and parktime <= 14:
    amt = amt + 10.50
elif parktime > 14 and parktime <= 16:
    amt = amt + 12
elif parktime > 16 and parktime <= 18:
    amt = amt + 13.50
elif parktime > 18 and parktime <= 20:
    amt = amt + 15
elif parktime > 20 and parktime <= 22:
    amt = amt + 16.50
elif parktime > 22 and parktime <= 24:
    amt = amt + 18

#----------------------------------------Back End-------------------------------------------
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/kisho/AppData/Local/Tesseract-OCR/tesseract.exe'

cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

global text
text = " "
global img
#img = " "

def extract_num(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nameplate = cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in nameplate:
        a, b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b, :]
        
        kernal = np.ones((1, 1), np.uint8)
        plate = cv2.dilate(plate, kernal, iterations=1)
        plate = cv2.erode(plate, kernal, iterations=1)
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        (thresh, plate) = cv2.threshold(plate_gray, 127, 225, cv2.THRESH_BINARY)
        
        text = pytesseract.image_to_string(plate)
        text = ''.join(e for e in text if e.isalnum())
        cv2.rectangle(img, (x,y), (x+w, y+h), (51,51,255), 2)
        cv2.rectangle(img, (x,y - 40), (x + w, y), (51,51,255), -1)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    
    cv2.imshow("Result", img)
    cv2.imwrite('result.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
car = "C:/Users/kisho/Desktop/CarNameplates/IK33PIT.png"
car2 = "C:/Users/kisho/Desktop/CarNameplates/KY70CWT.jpg"
car3 = "C:/Users/kisho/Desktop/CarNameplates/RV05FEP.jpg"
car4 = "C:/Users/kisho/Desktop/CarNameplates/RE74INS.png"
car5 = "C:/Users/kisho/Desktop/CarNameplates/UK23CWW.jpg"
car6 = "C:/Users/kisho/Desktop/CarNameplates/HG20POV.jpg"
extract_num(car)
extract_num(car2)
extract_num(car3)
extract_num(car4)
extract_num(car5)
extract_num(car6)

'''
global carfoundimg
carfoundimg = []
first_two_chars_entry = plateinfo[:2]
first_two_chars_detect = text[:2] 
if first_two_chars_entry == "IK":
    carfoundimg = "IK33PIT.png"
    print(carfoundimg)
elif first_two_chars_entry == "KY":
    carfoundimg = "KY70CWT.jpg"
    print(carfoundimg)
elif first_two_chars_entry == "RV":
    carfoundimg = "RV05FEP.jpg" 
    print(carfoundimg)
elif first_two_chars_entry == "IR":
    carfoundimg = "RE74INS.png"
    print(carfoundimg)
elif first_two_chars_entry == "IU":
    carfoundimg = "UK23CWW.jpg"
    print(carfoundimg)
elif first_two_chars_entry == "HG":
    carfoundimg = "HG20POV.jpg"
    print(carfoundimg)
'''
carfoundimg = "C:/Users/kisho/Desktop/CarNameplates/HG20POV.jpg"
image = Image.open(carfoundimg)
photo = ImageTk.PhotoImage(image)

#---------------------------------Front End--------------------------------------- 
def check_entry():
    plateinfo = regentry.get() 
    if plateinfo == "":
        messagebox.showerror("Error", "Entry is empty, Please enter a valid Plate")
    else:
        print("Vehicle Number:", plateinfo)
        messagebox.showinfo("Success", "You Car has been found.")
        infolabel2 = tk.Label(master=frame2, text="Is this your vehicle:", font=info2font)
        infolabel2.pack()
        image_label = tk.Label(master=frame2, image = photo)
        image_label.pack()
        def show_label():
            infolabel3 = tk.Label(master=frame2, text="You have been parked here for: "+str(parktime)+"hrs", font=info2font)
            infolabel3.pack()
            infolabel4 = tk.Label(master=frame2, text="Your amount to pay is: £"+str(amt), font=info2font)
            infolabel4.pack()  
            infolabel6 = tk.Label(master=frame2, text="Please Select Payment Type", font=info2font)
            infolabel6.pack() 
            def show_label2():
                infolabel7 = tk.Label(master=frame2, text="Please insert or tap card below: ", font=info2font)
                infolabel7.pack()
                image_label2 = tk.Label(master=frame2, image = photo2)
                image_label2.pack()
                time.sleep(0.1)
                n = 0
                while n != 5:
                    n = n + 1
                    time.sleep(1)
                    print(n)
                infolabel9 = tk.Label(master=frame2, text="Thank you for parking!", font=infofont)
                infolabel9.pack()  
                infolabel10 = tk.Label(master=frame2, text="Please come again", font=infofont)
                infolabel10.pack() 
            def show_label3():
                infolabel8 = tk.Label(master=frame2, text="Please insert cash below: ", font=info2font)
                infolabel8.pack()
                image_label2 = tk.Label(master=frame2, image = photo2)
                image_label2.pack()
                time.sleep(0.1)
                m = 0
                while m != 5:
                    m = m + 1
                    time.sleep(1)
                    print(m)
                infolabel9 = tk.Label(master=frame2, text="Thank you for parking!", font=infofont)
                infolabel9.pack()  
                infolabel10 = tk.Label(master=frame2, text="Please come again", font=infofont)
                infolabel10.pack() 
            pyautogui.time.sleep(3)
            pyautogui.scroll(-speed)
            button4 = tk.Button(master=frame2, text="Card", font=buttonfont, width=15, justify='center', bg="White", fg="black", command=show_label2)
            button4.pack()   
            button5 = tk.Button(master=frame2, text="Cash", font=buttonfont, width=15, justify='center', bg="White", fg="black", command=show_label3)
            button5.pack()
        buttonfont = ("Arial", 19, "bold")
        button2 = tk.Button(master=frame2, text="This is my car", font=buttonfont, width=15, justify='center', bg="orange", fg="black", command=show_label)
        button2.pack()
        button3 = tk.Button(master=frame2, text="This is not my car", font=buttonfont, width=15, justify='center', bg="orange", fg="black", command=quitpgrm)
        button3.pack()     
        
buttonfont = ("Arial", 19, "bold")
button = tk.Button(master=frame2, text="Enter", font=buttonfont, width=15, justify='center', bg="orange", fg="black", command=check_entry)
button.pack()


window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




