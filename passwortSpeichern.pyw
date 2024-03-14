#-import-------------
import csv
import tkinter as tk
import customtkinter
import string

#-Dateipfad----------
dateipfad = r""

#-root---------------
root = customtkinter.CTk()
root.title("Passwort Speichern")

#-custom-------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root.geometry("230x170")

#-dev----------------
#-Speichern
def speichern():
    Name= NameRoot.get()
    nutzernamen= nutzernamenRoot.get()
    eMail= eMailRoot.get()
    Passwort= PasswortRoot.get()
    Extra= ExtraRoot.get()
    #-verschlüsselt
    shift = 25
    alphabet = "aAäÄbBcCdDeEeEfFgGhHiIjJkKlLmMnNoOöÖpPqQrRsStTuUüÜvVwWxXyYzZ0123456789!#$%&()*+,-./:;<=>?@[]^_{|}"
    shifted= alphabet[shift:] + alphabet[:shift]
    table= str.maketrans(alphabet, shifted)

    verschlüsseltnutzernamen = nutzernamen.translate(table)
    verschlüsseltEMail = eMail.translate(table)
    verschlüsseltPasswort = Passwort.translate(table)
    
    neue_daten=[Name,verschlüsseltnutzernamen,verschlüsseltEMail,verschlüsseltPasswort,Extra]

    with open(dateipfad, mode="a", newline="") as Db:
        Inhalt = csv.writer(Db, delimiter=";")
        Inhalt.writerow(neue_daten)
    NameRoot.delete(0, tk.END)
    NameRoot.insert(0, "ist Gespeichert")
    nutzernamenRoot.delete(0, tk.END)
    eMailRoot.delete(0, tk.END)
    PasswortRoot.delete(0, tk.END)
    ExtraRoot.delete(0, tk.END)



 
#-Grid---------------
#-Name
NameRoot= customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Name:").grid(row=1, column=0)
NameRoot.grid(row=1, column=1)
#-Nutzernamen
nutzernamenRoot= customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Nutzernamen:").grid(row=2, column=0)
nutzernamenRoot.grid(row=2, column=1)
#-E-Mail
eMailRoot= customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="E-Mail:").grid(row=3, column=0)
eMailRoot.grid(row=3, column=1)
#-Passwort
PasswortRoot=customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Passwort:").grid(row=4, column=0)
PasswortRoot.grid(row=4, column=1)
#-Seite
ExtraRoot = customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Extra:").grid(row=5, column=0)
ExtraRoot.grid(row=5, column=1)
#-Btn-Schreiben
SpeichernButton = customtkinter.CTkButton(root, text="Daten Speichern", command=speichern)
SpeichernButton.grid(row=6, column=0, columnspan=2)
#-Vordergrund
root.attributes("-topmost", True)




root.mainloop()

#-Recherche-qwell----
#-Verschlüsselung: https://www.youtube.com/watch?v=JEsUlx0Ps9k&t=446s&ab_channel=NeuralNine
#-Vordergrund: https://www.python-forum.de/viewtopic.php?t=51259