import tkinter as tk
from tkinter import messagebox
import statistics
def calculate():
 numbers = entry.get()
 numbers = [float(num) for num in numbers.split()]

 if not numbers:
    messagebox.showerror("Error", "Please enter a list of numbers.")
    return
 selected_option = option_var.get()

 if selected_option == "Mean":
  result.set(statistics.mean(numbers))
 elif selected_option == "Median":
   result.set(statistics.median(numbers))
 elif selected_option =="Mode":
  result.set(statistics.mode(numbers))
 elif selected_option =="HMean":
   result.set(statistics.harmonic_mean(numbers))     
 elif selected_option =="GMean":
   result.set(statistics.geometric_mean(numbers))
 elif selected_option == "Standard Deviation":
   result.set(statistics.stdev(numbers))
 elif selected_option =="Variance":
   result.set(statistics.variance(numbers))
 elif selected_option =="CoeffOfVariance":
   result.set(statistics.mean(numbers)/statistics.stdev(numbers))
 elif selected_option =="Mdeviation":
   result.set(statistics.mean(numbers)/len(numbers))
 elif selected_option =="Range":
   result.set(max(numbers)-min(numbers))
 else:
   messagebox.showerror("Error", "Please select a calculation option.")
root = tk.Tk()
root.title("Measure Of Central Tendency and Dispersion")
label1 =tk.Label(root,text ="Measure of Central Tendency :",font=('Arial',16))
label2 =tk.Label(root,text ="Measure of Dispersion :",font=('Arial',16))
input_label = tk.Label(root, text="Enter a list of numbers (separated by spaces):")
entry = tk.Entry(root)
option_var = tk.StringVar()
mean_radio = tk.Radiobutton(root, text="Arithmetic Mean", variable=option_var,
value="Mean")
median_radio = tk.Radiobutton(root, text=" Median ",
variable=option_var, value="Median")
g_mean_radio = tk.Radiobutton(root,text = "Geometric Mean",variable=option_var,value="GMean")
h_mean_radio = tk.Radiobutton(root,text ="Harmonic Mean",variable
=option_var,value="HMean")
mode_radio =tk.Radiobutton(root,text =" Mode ",variable=option_var, value ="Mode")
std_dev_radio = tk.Radiobutton(root, text=" Standard Deviation ",variable=option_var, value="Standard Deviation")
var_radio =tk.Radiobutton(root, text=" Variance",variable =option_var,value="Variance")
coff_variance =tk.Radiobutton(root, text =" Coefficient Of Variance ",variable = option_var,value="CoeffOfVariance")
mean_deviation = tk.Radiobutton(root, text =" Mean Deviation",variable=option_var, value="Mdeviation")
range_radio = tk.Radiobutton(root, text=" Range   ",variable = option_var , value="Range")
calculate_button = tk.Button(root, text="Calculate", command=calculate)
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
label1.grid(row =0 , column =3, columnspan =2)
input_label.grid(row=1, column=1, columnspan=2)
entry.grid(row=2, column=1)
mean_radio.grid(row=4, column=1)
median_radio.grid(row=5, column=1)
g_mean_radio.grid(row =6, column = 1)
h_mean_radio.grid(row=7, column=1)
mode_radio.grid(row = 8 ,column =1)
label2.grid(row = 9, column = 3)
var_radio.grid(row=10,column=1)
std_dev_radio.grid(row=11, column=1)
coff_variance.grid(row =12, column =1)
mean_deviation.grid(row =13, column = 1)
range_radio.grid(row =14 , column =1)
calculate_button.grid(row=15, column=2)
result_label.grid(row=16, column=2)
root.mainloop()