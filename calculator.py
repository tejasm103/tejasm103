import tkinter as tk
from tkinter import messagebox

class RealCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#171616")  # Dark sleek aesthetic
        self.root.resizable(False, False)

        # Store the current mathematical expression
        self.expression = ""

        # Setup Display Screen
        self.display_var = tk.StringVar(value="0")
        self.create_display()

        # Setup Buttons Layout
        self.create_buttons()

        # Bind physical keyboard keys for real-world usability
        self.bind_keys()

    def create_display(self):
        """Creates the digital display screen at the top."""
        display_frame = tk.Frame(self.root, width=350, height=100, bg="#171616")
        display_frame.pack(expand=True, fill="both")

        # Label widget mirrors real LCD/LED screens
        self.screen = tk.Label(
            display_frame, 
            textvariable=self.display_var, 
            anchor="e", 
            font=("Arial", 36, "bold"), 
            bg="#171616", 
            fg="#ffffff", 
            padx=20, 
            pady=20
        )
        self.screen.pack(expand=True, fill="both")

    def create_buttons(self):
        """Creates the grid layout for calculator keys."""
        button_frame = tk.Frame(self.root, bg="#171616")
        button_frame.pack(expand=True, fill="both")

        # Configured layout mimicking standard hardware calculators
        button_layout = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        # Explicit color thematic mapping
        colors = {
            "number": {"bg": "#333333", "fg": "#ffffff", "active_bg": "#555555"},
            "operator": {"bg": "#ff9f0a", "fg": "#ffffff", "active_bg": "#cc7f08"},
            "utility": {"bg": "#a5a5a5", "fg": "#000000", "active_bg": "#d8d8d8"}
        }

        for row_idx, row in enumerate(button_layout):
            for col_idx, text in enumerate(row):
                # Determine button styling category
                if text in ['C', '(', ')']:
                    theme = colors["utility"]
                elif text in ['/', '*', '-', '+', '=']:
                    theme = colors["operator"]
                else:
                    theme = colors["number"]

                # Handle the layout span for the zero '0' button to keep layout symmetrical
                colspan = 2 if text == '0' else 1
                
                btn = tk.Button(
                    button_frame, 
                    text=text, 
                    font=("Arial", 18, "bold"),
                    bg=theme["bg"], 
                    fg=theme["fg"], 
                    activebackground=theme["active_bg"],
                    activeforeground=theme["fg"],
                    bd=0, 
                    relief="flat",
                    command=lambda t=text: self.on_button_click(t)
                )
                
                # Dynamic grid alignment
                btn.grid(
                    row=row_idx, 
                    column=col_idx if text != '=' or button_layout[row_idx][0] != '0' else col_idx + 1, 
                    columnspan=colspan, 
                    sticky="nsew", 
                    padx=2, 
                    pady=2
                )
                
            button_frame.rowconfigure(row_idx, weight=1)
            
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        """Central logical router processing user inputs."""
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif char == '=':
            self.evaluate_expression()
        else:
            # Replace initial zero unless adding a decimal point
            if self.expression == "" and char not in ['.', '+', '-', '*', '/', '(', ')']:
                self.expression = str(char)
            else:
                self.expression += str(char)
            self.display_var.set(self.expression)

    def evaluate_expression(self):
        """Safely calculates the string math equation."""
        try:
            # Explicit replacements to format friendly characters into mathematical script
            sanitized_expr = self.expression.replace('×', '*').replace('÷', '/')
            
            # Restrict global/local dictionary evaluation to prevent security injection risks
            result = eval(sanitized_expr, {"__builtins__": None}, {})
            
            # Format integer conversions cleanly
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            # Truncate overly long floats to avoid breaking the display screen grid limits
            elif isinstance(result, float):
                result = round(result, 8)

            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            self.display_var.set("Error: Div by 0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def bind_keys(self):
        """Maps physical computer keystrokes to calculator methods."""
        self.root.bind("<Key>", self.parse_keyboard)

    def parse_keyboard(self, event):
        """Directs keyboard events to match graphical interface actions."""
        char = event.char
        if char in '0123456789+-*/().':
            self.on_button_click(char)
        elif event.keysym in ['Return', 'KP_Enter']:
            self.on_button_click('=')
        elif event.keysym in ['BackSpace']:
            # Emulate real calculator single-character deletion
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif event.keysym == 'Escape':
            self.on_button_click('C')

if __name__ == "__main__":
    window = tk.Tk()
    app = RealCalculator(window)
    window.mainloop()
