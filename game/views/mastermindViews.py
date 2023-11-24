import tkinter as tk
from tkinter import ttk

class MasterMindView:
    def __init__(self,availableColors):
        root = tk.Tk()
        self.master = root
        self.master.title("Mastermind Game")
        self.master.configure(bg="black")
        self.availableColors = availableColors

        title_label = ttk.Label(self.master,foreground="white", background="black",text="Mastermind Game", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Create the game board
        self.displayBoard(0,9,5)

        verify_button = ttk.Button(self.master, text="Verify", command=self.setUserInput)
        verify_button.grid(row=2, column=0, columnspan=4, pady=10)

    def displayBoard(self,turn,max_turns,width,guess=None):
        # Create a frame to hold the game board
        board_frame = ttk.Frame(self.master, padding="10")
        board_frame.grid(row=1, column=0, padx=10, pady=10)
        self.peg_buttons = []
        # Create the code pegs
        for row in range(max_turns):
            row_buttons = []
            for col in range(width):
                peg_button = tk.Button(board_frame, width=5, command=lambda t=turn, r=row, c=col: self.peg_clicked(r, c,t))
                peg_button.grid(row=row, column=col, padx=5, pady=5)
                row_buttons.append(peg_button)
            self.peg_buttons.append(row_buttons)
        
        # Create labels for correctness feedback
        self.feedback_labels = []
        for row in range(max_turns):
            feedback_label = ttk.Label(board_frame, text="", foreground="white", background="black")
            feedback_label.grid(row=row, column=width, padx=5, pady=5)
            self.feedback_labels.append(feedback_label)

    def peg_clicked(self, row, col,turn):
        if row == turn:
            # Cycle through available colors
            try:
                current_color_index = self.availableColors.index(self.peg_buttons[row][col]["bg"])
            except:
                current_color_index = 0

            next_color_index = (current_color_index + 1) % len(self.availableColors)
            new_color = self.availableColors[next_color_index]

            # Update the color of the clicked peg
            self.peg_buttons[row][col].configure(bg=new_color,activebackground=new_color)
    
    def setUserInput(self):
        inputs = []
        for button in self.peg_buttons[0]:
            inputs.append(button["bg"])
        self.user_input = inputs

    def getUserInput(self):
        while self.user_input == None:
            pass
        values = self.user_input
        self.user_input = None
        return values


availableColors = ["red", "blue", "green", "yellow", "purple", "orange"]
M = MasterMindView(availableColors)
M.master.mainloop()