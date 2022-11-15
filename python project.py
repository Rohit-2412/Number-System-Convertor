from tkinter import *
from tkinter import messagebox
from conversion import *


"""python GUI project to convert a number to another number system"""
class NumberSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Number System")
        self.root.geometry("875x700+225+50")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        # Create a frame
        main_frame = Frame(self.root, bg="white")
        main_frame.place(x=0, y=0, width=870, height=400)

        # Create a label
        input_label = Label(main_frame, text="Enter a number", font=(
            "times new roman", 20, "bold"), bg="white")
        input_label.place(x=10, y=10)

        # Create a entry
        self.entry = Entry(main_frame, font=(
            "times new roman", 15), bg="lightgreen")
        self.entry.place(x=10, y=50, width=300, height=30)

        # display 4 radio buttons to choose between binary, octal, decimal and hexadecimal
        self.number_type = IntVar()
        bin_radio = Radiobutton(main_frame, text="Binary", variable=self.number_type, value=1, font=(
            "times new roman", 15, "bold"), bg="white")
        bin_radio.place(x=10, y=100)

        oct_radio = Radiobutton(main_frame, text="Octal", variable=self.number_type, value=2, font=(
            "times new roman", 15, "bold"), bg="white")
        oct_radio.place(x=10, y=135)

        dec_radio = Radiobutton(main_frame, text="Decimal", variable=self.number_type, value=3, font=(
            "times new roman", 15, "bold"), bg="white")
        dec_radio.place(x=10, y=170)

        hex_radio = Radiobutton(main_frame, text="Hexadecimal", variable=self.number_type, value=4, font=(
            "times new roman", 15, "bold"), bg="white")
        hex_radio.place(x=10, y=205)

        # display label for 'Number to be converted in'
        converted_to_label = Label(main_frame, text="Number to be converted in", font=(
            "times new roman", 20, "bold"), bg="white")
        converted_to_label.place(x=450, y=40)

        # display 4 radio buttons to choose between binary, octal, decimal and hexadecimal
        self.convert_to = IntVar()
        bin_radio = Radiobutton(main_frame, text="Binary", variable=self.convert_to, value=1, font=(
            "times new roman", 15, "bold"), bg="white")
        bin_radio.place(x=450, y=100)

        oct_radio = Radiobutton(main_frame, text="Octal", variable=self.convert_to, value=2, font=(
            "times new roman", 15, "bold"), bg="white")
        oct_radio.place(x=450, y=135)

        dec_radio = Radiobutton(main_frame, text="Decimal", variable=self.convert_to, value=3, font=(
            "times new roman", 15, "bold"), bg="white")
        dec_radio.place(x=450, y=170)

        hex_radio = Radiobutton(main_frame, text="Hexadecimal", variable=self.convert_to, value=4, font=(
            "times new roman", 15, "bold"), bg="white")
        hex_radio.place(x=450, y=205)

        # display 3 button- convert, explain, clear and exit

        # convert button
        convert_button = Button(main_frame, text="Convert", font=(
            "times new roman", 15), bg="lightgreen", command=self.convert)
        convert_button.place(x=10, y=275, width=150, height=30)

        # explain button
        explain_button = Button(main_frame, text="Explain", font=(
            "times new roman", 15), bg="lightgreen", command=self.explain)
        explain_button.place(x=235, y=275, width=150, height=30)

        # clear button
        clear_button = Button(main_frame, text="Clear", font=(
            "times new roman", 15), bg="lightgreen", command=self.clear)
        clear_button.place(x=460, y=275, width=150, height=30)

        # exit button
        exit_button = Button(main_frame, text="Exit", font=(
            "times new roman", 15), bg="lightgreen", command=self.exit)
        exit_button.place(x=685, y=275, width=150, height=30)

        # --- result frame ---
        # display 4 label as binary, octal, decimal and hexadecimal and one textbox corresponding to each label to show the result
        result_frame = Frame(self.root, bg="tomato")
        result_frame.place(x=0, y=400, width=875, height=300)

        # display label for 'Result'
        result_label = Label(result_frame, text="Result", font=(
            "times new roman", 20, "bold"), bg="tomato")
        result_label.place(x=10, y=10)

        # display label for 'Binary'
        binary_label = Label(result_frame, text="Binary", font=(
            "Abel", 15), bg="tomato")
        binary_label.place(x=12, y=50)

        # display label for 'Binary' Result corresponding to binary_label
        self.binary_result = Label(result_frame, text="", font=(
            "Abel", 15), bg="white", width=15)
        self.binary_result.place(x=150, y=50)

        # display label for 'Octal'
        octal_label = Label(result_frame, text="Octal", font=(
            "Abel", 15), bg="tomato")
        octal_label.place(x=12, y=100)

        # display label for 'Octal' Result corresponding to octal_label
        self.octal_result = Label(result_frame, text="", font=(
            "Abel", 15), bg="white", width=15)
        self.octal_result.place(x=150, y=100)

        # display label for 'Decimal'
        decimal_label = Label(result_frame, text="Decimal", font=(
            "Abel", 15), bg="tomato")
        decimal_label.place(x=12, y=150)

        # display label for 'Decimal' Result corresponding to decimal_label
        self.decimal_result = Label(result_frame, text="", font=(
            "Abel", 15), bg="white", width=15)
        self.decimal_result.place(x=150, y=150)

        # display label for 'Hexadecimal'
        hexadecimal_label = Label(result_frame, text="Hexadecimal", font=(
            "Abel", 15), bg="tomato")
        hexadecimal_label.place(x=12, y=200)

        # display label for 'Hexadecimal' Result corresponding to hexadecimal_label
        self.hexadecimal_result = Label(result_frame, text="", font=(
            "Abel", 15), bg="white", width=15)
        self.hexadecimal_result.place(x=150, y=200)

        # display a text box showing  `Click on 'Explain' button to know how to convert number from one base to another`
        self.explain_text = Label(result_frame, text="Click on 'Explain' button to know how to convert number from one base to another", font=(
            "Abel", 15), bg="white", width=40, height=8, wraplength=400, justify=CENTER)
        self.explain_text.place(x=400, y=50)

    def convert(self):
        # get the number from the entry
        number = self.entry.get()

        # get the number type from the radio button
        number_type = self.number_type.get()

        # get the number to be converted in from the radio button
        convert_to = self.convert_to.get()

        # check if the number is empty
        if number == "":
            messagebox.showerror("Error", "Please enter a number")
            return

        # check if the number type is not selected
        if number_type == 0:
            messagebox.showerror("Error", "Please select the number type")
            return

        # check if the number to be converted in is not selected
        if convert_to == 0:
            messagebox.showerror(
                "Error", "Please select the number to be converted in")
            return

        # check if the number type and number to be converted in is same
        if number_type == convert_to:
            messagebox.showerror(
                "Error", "Please select different number type and number to be converted in")
            return

        # check if the number is binary
        if number_type == 1:
            # check if the number is valid binary number
            if not self.is_valid_binary(number):
                messagebox.showerror(
                    "Error", "Please enter a valid binary number")
                return

            # convert the number to octal
            if convert_to == 2:
                self.octal_result.config(text=self.binary_to_octal_res(number))
                self.decimal_result.config(text="")
                self.hexadecimal_result.config(text="")
                self.binary_result.config(text=number)
            # convert the number to decimal
            elif convert_to == 3:
                self.decimal_result.config(
                    text=self.binary_to_decimal_res(number))
                self.octal_result.config(text="")
                self.hexadecimal_result.config(text="")
                self.binary_result.config(text=number)
            # convert the number to hexadecimal
            elif convert_to == 4:
                self.hexadecimal_result.config(
                    text=self.binary_to_hexadecimal_res(number))
                self.octal_result.config(text="")
                self.decimal_result.config(text="")
                self.binary_result.config(text=number)

        # check if the number is octal
        elif number_type == 2:
            # check if the number is valid octal number
            if not self.is_valid_octal(number):
                messagebox.showerror(
                    "Error", "Please enter a valid octal number")
                return

            # convert the number to binary
            if convert_to == 1:
                self.binary_result.config(
                    text=self.octal_to_binary_res(number))
                self.octal_result.config(text=number)
                self.decimal_result.config(text="")
                self.hexadecimal_result.config(text="")
            # convert the number to decimal
            elif convert_to == 3:
                self.decimal_result.config(
                    text=self.octal_to_decimal_res(number))
                self.octal_result.config(text=number)
                self.binary_result.config(text="")
                self.hexadecimal_result.config(text="")
            # convert the number to hexadecimal
            elif convert_to == 4:
                self.hexadecimal_result.config(
                    text=self.octal_to_hexadecimal_res(number))
                self.octal_result.config(text=number)
                self.binary_result.config(text="")
                self.decimal_result.config(text="")

        # check if the number is decimal
        elif number_type == 3:
            # check if the number is valid decimal number
            if not self.is_valid_decimal(number):
                messagebox.showerror(
                    "Error", "Please enter a valid decimal number")
                return

            # convert the number to binary
            if convert_to == 1:
                self.binary_result.config(
                    text=self.decimal_to_binary_res(number))
                self.decimal_result.config(text=number)
                self.octal_result.config(text="")
                self.hexadecimal_result.config(text="")
            # convert the number to octal
            elif convert_to == 2:
                self.octal_result.config(
                    text=self.decimal_to_octal_res(number))
                self.decimal_result.config(text=number)
                self.binary_result.config(text="")
                self.hexadecimal_result.config(text="")
            # convert the number to hexadecimal
            elif convert_to == 4:
                self.hexadecimal_result.config(
                    text=self.decimal_to_hexadecimal_res(number))
                self.decimal_result.config(text=number)
                self.binary_result.config(text="")
                self.octal_result.config(text="")

        # check if the number is hexadecimal
        elif number_type == 4:
            # check if the number is valid hexadecimal number
            if not self.is_valid_hexadecimal(number):
                messagebox.showerror(
                    "Error", "Please enter a valid hexadecimal number")
                return

            # convert the number to binary
            if convert_to == 1:
                self.binary_result.config(
                    text=self.hexadecimal_to_binary_res(number))
                self.octal_result.config(
                    text="")
                self.decimal_result.config(
                    text="")
                self.hexadecimal_result.config(
                    text="")
            # convert the number to octal
            elif convert_to == 2:
                self.binary_result.config(
                    text="")
                self.octal_result.config(
                    text=self.hexadecimal_to_octal_res(number))
                self.decimal_result.config(
                    text="")
                self.hexadecimal_result.config(
                    text="")
            # convert the number to decimal
            elif convert_to == 3:
                self.decimal_result.config(
                    text=self.hexadecimal_to_decimal_res(number))
                self.binary_result.config(
                    text="")
                self.octal_result.config(
                    text="")
                self.hexadecimal_result.config(
                    text="")

    def is_valid_binary(self, number):
        # check if the number is valid binary number
        for digit in number:
            if digit not in "01":
                return False
        return True

    def is_valid_octal(self, number):
        # check if the number is valid octal number
        for digit in number:
            if digit not in "01234567":
                return False
        return True

    def is_valid_decimal(self, number):
        # check if the number is valid decimal number
        for digit in number:
            if digit not in "0123456789":
                return False
        return True

    def is_valid_hexadecimal(self, number):
        # check if the number is valid hexadecimal number
        for digit in number:
            if digit not in "0123456789ABCDEF":
                return False
        return True

    def binary_to_octal_res(self, number):
        # convert the binary number to octal number
        return oct(int(number, 2))[2:]

    def binary_to_decimal_res(self, number):
        # convert the binary number to decimal number
        return str(int(number, 2))

    def binary_to_hexadecimal_res(self, number):
        # convert the binary number to hexadecimal number
        return hex(int(number, 2))[2:].upper()

    def octal_to_binary_res(self, number):
        # convert the octal number to binary number
        return bin(int(number, 8))[2:]

    def octal_to_decimal_res(self, number):
        # convert the octal number to decimal number
        return str(int(number, 8))

    def octal_to_hexadecimal_res(self, number):
        # convert the octal number to hexadecimal number
        return hex(int(number, 8))[2:].upper()

    def decimal_to_binary_res(self, number):
        # convert the decimal number to binary number
        return bin(int(number))[2:]

    def decimal_to_octal_res(self, number):
        # convert the decimal number to octal number
        return oct(int(number))[2:]

    def hexadecimal_to_binary_res(self, number):
        # convert the hexadecimal number to binary number
        return bin(int(number, 16))[2:]

    def hexadecimal_to_octal_res(self, number):
        # convert the hexadecimal number to octal number
        return oct(int(number, 16))[2:]

    def hexadecimal_to_decimal_res(self, number):
        # convert the hexadecimal number to decimal number
        return str(int(number, 16))

    def explain(self):
        # getting number type
        number_type = self.number_type.get()

        # getting convert to
        convert_to = self.convert_to.get()
        if self.entry.get() == "":
            messagebox.showerror("Error", "Please enter a number")
            return

        if number_type == 0 or convert_to == 0:
            messagebox.showerror("Error", "Please select the options")
            return

        # create a new window
        self.explain_window = Tk()
        self.explain_window.title("Explanation")
        self.explain_window.geometry("500x700+500+75")
        self.explain_window.resizable(False, False)

        names = ["Binary", "Octal", "Decimal", "Hexadecimal"]

        # create a label to explain the program font color should be green
        self.explain_label = Label(
            self.explain_window, text="Explanation", font=("Arial", 20, 'bold'), fg="sky blue")
        self.explain_label.pack(pady=10)

        # create a Label to show the base number system and target number system
        self.base_label = Label(
            self.explain_window, text=f"Base Number System: {names[number_type-1]}", font=("Arial", 15), fg='red')
        self.base_label.pack(pady=10)

        self.target_label = Label(
            self.explain_window, text=f"Target Number System: {names[convert_to-1]}", font=("Arial", 15), fg='chocolate')
        self.target_label.pack(pady=5)

        # create a label to show the steps to convert
        self.steps_label = Label(
            self.explain_window, text="", font=("Arial", 15))
        self.steps_label.pack(pady=5)
        # create a label to show the explanation
        self.exp_label = Label(
            self.explain_window, text="", font=("Arial", 15, 'bold'))
        self.exp_label.pack(pady=5)

        if number_type == 1:
            if convert_to == 2:
                e = convertBinToOct(self.entry.get())
                self.steps_label.config(
                    text="Steps: Convert each 3 digits to octal number")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 3:
                e = convertBinToDec(self.entry.get())
                self.steps_label.config(
                    text="Steps: Multiply each digit with 2^i and add them")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 4:
                e = convertBinToHex(self.entry.get())
                self.steps_label.config(
                    text="Steps: Convert each 4 digits to hexadecimal number")
                self.exp_label.config(
                    text=f"{e}")

        elif number_type == 2:
            if convert_to == 1:
                e = convertOctToBin(self.entry.get())
                self.steps_label.config(
                    text="Steps: Convert each digit to 3 digits binary number")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 3:
                e = convertOctToDec(self.entry.get())
                self.steps_label.config(
                    text="Steps: Multiply each digit with 8^i and add them")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 4:
                e = convertOctToHex(self.entry.get())
                self.steps_label.config(
                    text="Steps: Convert the given octal number to binary number and then convert it to hexadecimal number")
                self.exp_label.config(
                    text=f"{e}")

        elif number_type == 3:
            if convert_to == 1:
                e = convertDecToBin(self.entry.get())
                self.steps_label.config(
                    text="Steps: Divide the number by 2 and get the remainder")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 2:
                e = convertDecToOct(self.entry.get())
                self.steps_label.config(
                    text="Steps: Divide the number by 8 and get the remainder")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 4:
                e = convertDecToHex(self.entry.get())
                self.steps_label.config(
                    text="Steps: Divide the number by 16 and get the remainder")
                self.exp_label.config(
                    text=f"{e}")

        elif number_type == 4:
            if convert_to == 1:
                e = convertHexToBin(self.entry.get())
                self.steps_label.config(
                    text="Steps: Convert each digit to 4 digits binary number")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 2:
                e = convertHexToOct(self.entry.get())
                self.steps_label.config(
                    text="Steps: Convert the given hexadecimal number to binary number and then convert it to octal number")
                self.exp_label.config(
                    text=f"{e}")
            elif convert_to == 3:
                e = convertHexToDec(self.entry.get())
                self.steps_label.config(
                    text="Steps: Multiply each digit with 16^i and add them")
                self.exp_label.config(
                    text=f"{e}")

    def clear(self):
        self.binary_result.config(text="")
        self.octal_result.config(text="")
        self.decimal_result.config(text="")
        self.hexadecimal_result.config(text="")
        self.entry.delete(0, END)
        self.number_type.set(0)
        self.convert_to.set(0)

    def exit(self):
        self.root.destroy()


# main fuction
if __name__ == '__main__':
    root = Tk()
    obj = NumberSystem(root)
    root.mainloop()
