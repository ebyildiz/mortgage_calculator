# mortgage calculator 
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Elif's Mortgage Calculator")
root.geometry("500x600")

def payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get():
        # 1) Converting Entry Boxes to Numbers
        years = int(term_entry.get())
        months = years * 12
        rate = float(interest_entry.get())
        loan = int(amount_entry.get())
        # 2) Start Calculating
        # Monthly Interest Rate
        monthly_rate = rate / 100 / 12
        # 3) Get payment
        payment = loan*(monthly_rate*(1 + monthly_rate)**(months)) / \
((1 + monthly_rate)**(months) - 1)
        # 4) Add optional entries
        if propertytax_entry.get():
            prop_tax = float(propertytax_entry.get())
            payment = payment + prop_tax / 12
        if homeowners_insurance_entry.get():
            homeowners = float(homeowners_insurance_entry.get())
            payment = payment + homeowners / 12
        if pmi_rate_entry.get():
            pmi = float(pmi_rate_entry.get())
            payment = payment + pmi / 12
        if hoa_entry.get():
            hoa = float(hoa_entry.get())
            payment = payment + hoa  / 12
        # 5) Output Payment to the Screen
        payment_label.config(text=f"Monthly Payment: ${round(payment, 2)}")
    else:
        payment_label.config(text="Don't Forget to Enter the Required Values!")

label_frame = LabelFrame(root, text='Mortgage Calculator')
label_frame.pack(pady=30)

my_frame = Frame(label_frame)
my_frame.pack(pady=20)

# Define labels and entry boxes

amount_label = Label(my_frame, text= 'Loan Amount')
amount_entry = Entry(my_frame, font=('Helvetica', 10))

interest_label = Label(my_frame, text= 'Interest Rate \
(ex:3 for 3%)')
interest_entry = Entry(my_frame, font=('Helvetica', 10))

term_label = Label(my_frame, text= 'Loan Term (years)')
term_entry = Entry(my_frame, font=('Helvetica', 10))

propertytax_label = Label(my_frame, text= 'Annual Property Tax Amount \
(Optional)')
propertytax_entry = Entry(my_frame, font=('Helvetica', 10))

homeowners_insurance_label = Label(my_frame, text= 'Annual Homeowner Insurance \
Cost (Optional)')
homeowners_insurance_entry = Entry(my_frame, font=('Helvetica', 10))

pmi_rate_label = Label(my_frame, text= 'Annual PMI Cost (Optional)')
pmi_rate_entry = Entry(my_frame, font=('Helvetica', 10))

hoa_label = Label(my_frame, text= 'Monthly HOA Fees (Optional)')
hoa_entry = Entry(my_frame, font=('Helvetica', 10))

# Put labels and entry boxes on the screen

amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20)

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

propertytax_label.grid(row=4, column=0)
propertytax_entry.grid(row=4, column=1, pady=20)

homeowners_insurance_label.grid(row=5, column=0)
homeowners_insurance_entry.grid(row=5, column=1)

pmi_rate_label.grid(row=6, column=0)
pmi_rate_entry.grid(row=6, column=1, pady=20)

hoa_label.grid(row=7, column=0)
hoa_entry.grid(row=7, column=1, pady=20)

# Button
my_button = Button(label_frame, text="Calculate Payment", command=payment)
my_button.pack(pady=20)

# Output Label
payment_label  = Label(root, text="", font=("Helvetica", 10))
payment_label.pack(pady=20)

 # THE ENDDDD !!!!! <3333
root.mainloop()