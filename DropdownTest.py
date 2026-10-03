import customtkinter as ctk
from PIL import Image, ImageTk
import ctypes
import webbrowser

try:
    myappid = 'DropdownTest' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except: pass

dropdownData = [
    {"type":"d", "text":"Dropdown1", "subs":[
        {"type":"a", "text":"Dropdown2", "action": lambda: print("Adding a Dropdown Here")}
    ]}
]

#App init
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("600x800")
app.title("Dropdown Test")
app.resizable(False, False)

#Customization
version = "1.0.0"
githubLink = "https://github.com/ojblaster/DropdownTest"

bgColor = "#2C2C2C"
buttonColor = "#3F3F3F"
buttonHoverColor = "#4B4B4B"
black = "#000000"

fontL = ctk.CTkFont(family="Inter", weight="bold", size=25, slant="italic")
fontN = ctk.CTkFont(family="Inter", weight="bold", size=25)

buttonHeight = 40
buttonPadding = 2

treeSize = buttonHeight + buttonPadding*2 #dont change

#Images
dropdownLImage = ctk.CTkImage(light_image=Image.open("dropL.png"), dark_image=Image.open("dropL.png"), size=(treeSize, treeSize))
dropdownTImage = ctk.CTkImage(light_image=Image.open("dropT.png"), dark_image=Image.open("dropT.png"), size=(treeSize, treeSize))
dropdownSImage = ctk.CTkImage(light_image=Image.open("dropS.png"), dark_image=Image.open("dropS.png"), size=(treeSize, treeSize))
githubImage = ctk.CTkImage(light_image=Image.open("github.png"), dark_image=Image.open("github.png"), size=(45,45))
iconImage = ctk.CTkImage(light_image=Image.open("icon.png"), dark_image=Image.open("icon.png"), size=(45, 45))

app.iconbitmap("icon.ico")

#Top Banner
banner = ctk.CTkFrame(app, bg_color=buttonColor, height=50, corner_radius=0)
banner.pack_propagate(False)
banner.pack(side="top", fill="x")

icon = ctk.CTkLabel(banner, image=iconImage, text="")
icon.pack(side="left")

seperator = ctk.CTkFrame(app, fg_color=black, height=5, corner_radius=0)
seperator.pack(side="top", fill="both")

title = ctk.CTkLabel(banner, text=f"Dropdown Test V{version} ", font=fontL)
title.pack(side="left", padx=10)

githubButton = ctk.CTkButton(banner, image=githubImage, text="", command=lambda: webbrowser.open("https://github.com/ojblaster/DropdownTest"), width=0, fg_color=bgColor, hover_color=bgColor)
githubButton.pack(side="right", padx=5)

#Dropdown
mainFrame = ctk.CTkScrollableFrame(app, corner_radius=0, fg_color="transparent")
mainFrame.pack(fill="both", expand="True")

def changeTreeIcons(frame):
    parent = frame.master
    if not parent: return None
    slaves = parent.pack_slaves()
    try: idx = slaves.index(frame)
    except ValueError: return None

    prevFrame = slaves[idx-1] if idx > 0 else None
    nextFrame = slaves[idx+1] if idx < len(slaves) - 1 else None

    if prevFrame: prevFrame.treeImage.configure(image=dropdownTImage)

def actionButton(parent, item):
    buttonFrame = ctk.CTkFrame(parent, height=treeSize, fg_color="transparent")
    buttonFrame.pack(side="top", fill="x")
    treeImage = ctk.CTkLabel(buttonFrame, image=dropdownLImage, text="")
    treeImage.pack(side="left")
    buttonFrame.treeImage = treeImage 
    button = ctk.CTkButton(buttonFrame, text=item["text"], font=fontN, command=item["action"], fg_color=buttonColor, hover_color=buttonHoverColor, height=buttonHeight, anchor="w")
    button.pack(side="right", fill="x", pady = buttonPadding, expand="True")
    changeTreeIcons(buttonFrame)

def dropdownButton(parent, item):
    pass

actionButton(mainFrame, {"type":"a", "text":"Example Button", "action": lambda: print("Hello!")})
actionButton(mainFrame, {"type":"a", "text":"Example Button", "action": lambda: print("Hello!")})
actionButton(mainFrame, {"type":"a", "text":"Example Button", "action": lambda: print("Hello!")})
actionButton(mainFrame, {"type":"a", "text":"Example Button", "action": lambda: print("Hello!")})
actionButton(mainFrame, {"type":"a", "text":"Example Button", "action": lambda: print("Hello!")})

app.mainloop() 