#-import-------------
import csv
import tkinter as tk
import customtkinter
import pyautogui
import keyboard
#-Dateipfad----------
dateipfad = r""

#-root---------------
root = customtkinter.CTk()
root.title("Passwort Speichern")

#-custom-------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root.geometry("400x200")

#-dev----------------
#-Ausgeben
def Ausgeben():
    gesucht = gesuchtRoot.get()
    with open(dateipfad, mode="r") as Db:
        Inhalt = csv.DictReader(Db, delimiter=";")
        
        for row in Inhalt:
            if row["Name"] == gesucht:
                for key, value in row.items():
                    var_name = key.replace('-', '')
                    globals()[var_name] = value
                #-Entschlüsselt
                shift = -25
                alphabet = "aAäÄbBcCdDeEeEfFgGhHiIjJkKlLmMnNoOöÖpPqQrRsStTuUüÜvVwWxXyYzZ0123456789!#$%&()*+,-./:;<=>?@[]^_{|}"
                shifted= alphabet[shift:] + alphabet[:shift]
                table= str.maketrans(alphabet, shifted)

                entschlüsseltNutzernamen = Nutzernamen.translate(table)
                entschlüsseltEMail = EMail.translate(table)
                entschlüsseltPasswort = Passwort.translate(table)
                #-Name
                NameRoot.delete(0, tk.END)
                NameRoot.insert(0, Name)
                #-Nutzernamen
                nutzernamenRoot.delete(0, tk.END)
                nutzernamenRoot.insert(0, entschlüsseltNutzernamen)
                #-E-Mail
                eMailRoot.delete(0, tk.END)
                eMailRoot.insert(0, entschlüsseltEMail)
                #-Passwort
                PasswortRoot.delete(0, tk.END)
                PasswortRoot.insert(0, entschlüsseltPasswort)
                #-Extra
                ExtraRoot.delete(0, tk.END)
                ExtraRoot.insert(0, Extra)

                return entschlüsseltNutzernamen, entschlüsseltPasswort, entschlüsseltEMail
                break
        else:
            Erro= f"kein Ergebnis zu: {gesucht}"
            gesuchtRoot.delete(0, tk.END)
            gesuchtRoot.insert(0, Erro)

#-Nutzernamen-eintragen
def eintragenNutzernamen():
    entschlüsseltNutzernamen, entschlüsseltPasswort, entschlüsseltEMail = Ausgeben()
    pyautogui.confirm("Klicke auf das Textfeld und drücke 'OK'.")
    name = entschlüsseltNutzernamen
    keyboard.write(name)
#-Passwort-eintragen
def eintragenPasswort():
    Nutzernamen, entschlüsseltPasswort, entschlüsseltEMail = Ausgeben()
    pyautogui.confirm("Klicke auf das Textfeld und drücke 'OK'.")
    passwort = entschlüsseltPasswort
    keyboard.write(passwort)
#-E-Mail-eintragen
def eintragenEMail():
    Nutzernamen, entschlüsseltPasswort, entschlüsseltEMail = Ausgeben()
    pyautogui.confirm("Klicke auf das Textfeld und drücke 'OK'.")
    eMail = entschlüsseltEMail
    keyboard.write(eMail)

#-Grid---------------
#-Gesucht
gesuchtRoot = customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root, text="gesucht:").grid(row=1, column=0)
gesuchtRoot.grid(row=1, column=1)
#-Name
NameRoot= customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Name:").grid(row=2, column=0)
NameRoot.grid(row=2, column=1)
#-Nutzernamen
nutzernamenRoot= customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Nutzernamen:").grid(row=3, column=0)
nutzernamenRoot.grid(row=3, column=1)
#-E-Mail
eMailRoot= customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="E-Mail:").grid(row=4, column=0)
eMailRoot.grid(row=4, column=1)
#-Passwort
PasswortRoot=customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Passwort:").grid(row=5, column=0)
PasswortRoot.grid(row=5, column=1)
#-Extra
ExtraRoot = customtkinter.CTkEntry(root)
customtkinter.CTkLabel(root,text="Extra:").grid(row=6, column=0)
ExtraRoot.grid(row=6, column=1)
#-Btn-Ausgeben
AusgebenButton = customtkinter.CTkButton(root, text="Daten Ausgeben", command=Ausgeben)
AusgebenButton.grid(row=7, column=0, columnspan=2)
#-eintragen-Nutzernamen
eintragenNutzernamen= customtkinter.CTkButton(root, text="Nutzernamen eintragen ", command=eintragenNutzernamen)
eintragenNutzernamen.grid(row=3, column=2, columnspan=2)
#-eintragen-E-Mail
eintragenEMail = customtkinter.CTkButton(root, text="E-Mail eintragen ", command=eintragenEMail)
eintragenEMail.grid(row=4, column=2, columnspan=2)
#-eintragen-Passwort
eintragenPasswort = customtkinter.CTkButton(root, text="Passwort eintragen ", command=eintragenPasswort)
eintragenPasswort.grid(row=5, column=2, columnspan=2)
#-Vordergrund
root.attributes("-topmost", True)

root.mainloop()