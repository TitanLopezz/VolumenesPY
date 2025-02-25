import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def Validacion(Valor):
    try:
        return float(Valor)
    except ValueError:
        return None

def Calcular_Volumen():
  
    volume_type = volume_choice.get()

  
    radio = Validacion(entry_radio.get())
    Altura = Validacion(entry_Altura.get())
    lado = Validacion(entry_lado.get())
    Apotema = Validacion(entry_Apotema.get())
    Altura_Prisma = Validacion(entry_Altura_Prisma.get())

    if volume_type == 'Cilindro':
        if radio is None or Altura is None:
            messagebox.showerror("Error", "Por favor, ingresa los valores del cilindro.")
            return
        Volumen_cilindro = 3.1416 * (radio ** 2) * Altura
        messagebox.showinfo("Resultados", f"Volumen del cilindro es: {Volumen_cilindro:.2f}")
    
    elif volume_type == 'Prisma':
        if lado is None or Apotema is None or Altura_Prisma is None:
            messagebox.showerror("Error", "Por favor, ingresa los valores del prisma.")
            return
        Volumen_Prisma = 3 * lado * Apotema * Altura_Prisma
        messagebox.showinfo("Resultados", f"Volumen del prisma es: {Volumen_Prisma:.2f}")

    else:
        messagebox.showerror("Error", "Selecciona un tipo de volumen a calcular.")
        return

Root = tk.Tk()
Root.title("Calculadora Prismas y cilindros")

tk.Label(Root, text="Ingresa el radio (Cilindro): ").grid(row=0, column=0)
entry_radio = tk.Entry(Root)
entry_radio.grid(row=0, column=1)

tk.Label(Root, text="Ingresa la Altura del cilindro: ").grid(row=1, column=0)
entry_Altura = tk.Entry(Root)
entry_Altura.grid(row=1, column=1)

tk.Label(Root, text="Ingresa el lado del prisma: ").grid(row=2, column=0)
entry_lado = tk.Entry(Root)
entry_lado.grid(row=2, column=1)

tk.Label(Root, text="Ingresa el Apotema del prisma: ").grid(row=3, column=0)
entry_Apotema = tk.Entry(Root)
entry_Apotema.grid(row=3, column=1)

tk.Label(Root, text="Ingresa la Altura del prisma: ").grid(row=4, column=0)
entry_Altura_Prisma = tk.Entry(Root)
entry_Altura_Prisma.grid(row=4, column=1)

tk.Label(Root, text="Selecciona el tipo de volumen a calcular:").grid(row=5, column=0)
volume_choice = ttk.Combobox(Root, values=["Cilindro", "Prisma"])
volume_choice.grid(row=5, column=1)
volume_choice.set("Cilindro") 

tk.Button(Root, text="Calcular Volumen", command=Calcular_Volumen).grid(row=6, column=0, columnspan=2)

Root.mainloop()