import tkinter as tk
from tkinter import ttk, messagebox

# Extended static exchange rates
exchange_rates = {
    "USD": {"INR": 83.0, "EUR": 0.92, "GBP": 0.79, "JPY": 157, "AUD": 1.52, "CAD": 1.36},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0095, "JPY": 1.9, "AUD": 0.018, "CAD": 0.016},
    "EUR": {"USD": 1.08, "INR": 90.0, "GBP": 0.86, "JPY": 170, "AUD": 1.65, "CAD": 1.47},
    "GBP": {"USD": 1.26, "INR": 105, "EUR": 1.16, "JPY": 198, "AUD": 1.92, "CAD": 1.71},
    "JPY": {"USD": 0.0064, "INR": 0.53, "EUR": 0.0059, "GBP": 0.005, "AUD": 0.0097, "CAD": 0.0086},
    "AUD": {"USD": 0.66, "INR": 55, "EUR": 0.61, "GBP": 0.52, "JPY": 103, "CAD": 0.90},
    "CAD": {"USD": 0.74, "INR": 61, "EUR": 0.68, "GBP": 0.58, "JPY": 116, "AUD": 1.11}
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if from_curr == to_curr:
            result_label.config(text=f"Converted Amount: {amount:.2f} {to_curr}")
            return

        converted = amount * exchange_rates[from_curr][to_curr]
        result_label.config(text=f"Converted Amount: {converted:.2f} {to_curr}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount")
    except KeyError:
        messagebox.showerror("Error", "Conversion not available")

# Main window
root = tk.Tk()
root.title("Currency Converter - RISE 3.0")
root.geometry("420x320")
root.resizable(False, False)

# Title
tk.Label(root, text="Currency Converter App",
         font=("Arial", 16, "bold")).pack(pady=10)

# Amount
tk.Label(root, text="Enter Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Currency list
currency_list = list(exchange_rates.keys())

# From currency
tk.Label(root, text="From Currency").pack()
from_currency = ttk.Combobox(root, values=currency_list, state="readonly")
from_currency.pack(pady=5)
from_currency.set("USD")

# To currency
tk.Label(root, text="To Currency").pack()
to_currency = ttk.Combobox(root, values=currency_list, state="readonly")
to_currency.pack(pady=5)
to_currency.set("INR")

# Convert button
tk.Button(root, text="Convert", command=convert_currency,
          bg="green", fg="white", width=15).pack(pady=10)

# Result
result_label = tk.Label(root, text="Converted Amount:",
                        font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
