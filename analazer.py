import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("browser")

        # Janela amarela
        self.root.configure(bg='red')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="get page", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="new address", command=self.copy_file)
        self.copy_button.pack(pady=5)

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")
                return True
        return False
    def build_kernel(self):
        
       

        
        x=self.text_area.get("1.0","end-1c")
        print(x)
        self.execute_command(f'curl "{x}" -o /tmp/my.html',True)
        

    def run_kernel(self):
        r1="error"
        self.execute_command("python3 report.py",False)
        t=True
        t=self.execute_command("geany /tmp/my2.html",False)
        if t:
            t=self.execute_command("mousepad /tmp/my2.html",False)
        if t:         
            try:
                f1=open("/tmp/my.html","r")
                r1=f1.read()
                f1.close()
            
            except:       
                r1="error"
              
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END,r1)
    def copy_file(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END,"https://github.com/linesky")


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
