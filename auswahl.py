#-import-------------
import subprocess
import tkinter as tk
import customtkinter

#-Dateipfad----------
Dateipfad1= r""
Dateipfad2= r""

#-root---------------
root= customtkinter.CTk()
root.title("Passwort Manager")

#-custom-------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root.geometry("250x100")

#-dev----------------
#-Passwort-Speichern
def passwortSpeichern():
    subprocess.run(["python", Dateipfad1])
    
#-Passwort-Ausgeben
def passwortAusgeben():
    subprocess.run(["python", Dateipfad2])

#-Grid---------------
#-Text
customtkinter.CTkLabel(root,text="wehle zwischen speichern und ausgeben:").grid(row=1, column=0)
#-Btn-Speichern
BtnPasswortSpeichern= customtkinter.CTkButton(root, text="Daten Speichern", command=passwortSpeichern)
BtnPasswortSpeichern.grid(row=2, column=0, columnspan=1)
#-Btn-Ausgeben
BtnPasswortAusgeben= customtkinter.CTkButton(root, text="Daten Ausgeben", command=passwortAusgeben)
BtnPasswortAusgeben.grid(row=3, column=0, columnspan=1)

root.attributes("-topmost", True)

#-Ende-------------
root.mainloop()