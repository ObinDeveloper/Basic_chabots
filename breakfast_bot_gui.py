import tkinter as tk
from tkinter import messagebox

# Emojis for fun interactions
emoji_yes = "😊"
emoji_no = "🙁"
emoji_welcome = "👋"
emoji_bot = "🤖"
emoji_food = "🍽️"

# Global variables to track orders and order count
total_orders = 0
order_list = []


# Function for Yes/No response
def yes_no_response(answer):
    if answer == "yes":
        response = f"{emoji_bot} You said YES! {emoji_yes} Let's take another order."
        display_response(response)
        enable_order_buttons(True)
    else:
        response = f"{emoji_bot} You said NO! {emoji_no} Goodbye!"
        display_response(response)
        disable_all_buttons()


# Function to process order input and display response
def process_order():
    global total_orders
    order = order_entry.get().lower()

    if order == "waffles" or order == "pancakes":
        order_list.append(order)
        total_orders += 1

        response = f"{emoji_bot} {order.capitalize()} it is! {emoji_food} Your order is coming right up!"
        response += f"\n{emoji_bot} Orders so far: {', '.join(order_list)}."
        response += f"\nTotal number of orders: {total_orders}"
    else:
        response = f"{emoji_bot} Sorry, we only have waffles and pancakes today!"

    display_response(response)
    order_entry.delete(0, tk.END)  # Clear the input field
    ask_order_again()


# Function to ask if user wants to order again
def ask_order_again():
    message = f"{emoji_bot} Would you like to place another order? Please select Yes or No."
    display_response(message)
    enable_yes_no_buttons()


# Function to display the bot's response in the message box
def display_response(message):
    message_display.config(state=tk.NORMAL)  # Enable the textbox for editing
    message_display.delete(1.0, tk.END)  # Clear previous message
    message_display.insert(tk.END, message)  # Insert new message
    message_display.config(state=tk.DISABLED)  # Disable the textbox after updating


# Disable buttons when needed
def disable_all_buttons():
    yes_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)
    order_button.config(state=tk.DISABLED)


# Enable order buttons
def enable_order_buttons(enable=True):
    order_button.config(state=tk.NORMAL if enable else tk.DISABLED)


# Enable Yes/No buttons
def enable_yes_no_buttons():
    yes_button.config(state=tk.NORMAL)
    no_button.config(state=tk.NORMAL)


# Bot introduction
def start_bot():
    display_response(f"{emoji_welcome} Hello! I am Bob, the Breakfast Bot.\n"
                     f"{emoji_bot} Today we have waffles and pancakes available.\n"
                     "Please type your choice below.")


# Set up the main GUI window
root = tk.Tk()
root.title("Breakfast Bot")
root.geometry("500x400")

# Message display area
message_display = tk.Text(root, height=10, width=50, state=tk.DISABLED, wrap=tk.WORD)
message_display.pack(pady=10)

# Input field for the order
order_label = tk.Label(root, text="Enter your order (waffles/pancakes):")
order_label.pack()

order_entry = tk.Entry(root, width=40)
order_entry.pack(pady=5)

# Submit order button
order_button = tk.Button(root, text="Submit Order", command=process_order)
order_button.pack()

# Yes/No Buttons
yes_button = tk.Button(root, text="Yes", state=tk.DISABLED, command=lambda: yes_no_response("yes"))
yes_button.pack(side=tk.LEFT, padx=50, pady=20)

no_button = tk.Button(root, text="No", state=tk.DISABLED, command=lambda: yes_no_response("no"))
no_button.pack(side=tk.RIGHT, padx=50, pady=20)

# Start the bot when the program runs
start_bot()

# Start the tkinter event loop
root.mainloop()
