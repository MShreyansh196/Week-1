"""
Your First Interactive Python Program
-------------------------------------
Author:  <Shreyansh Medatati>
Date:    <June 17, 2025>

What to do:
   1. Replace <Your Name> and <Today's Date>.
   2. Follow the prompts in the terminal.
   3. Customize the questions or add more input/output.
"""

# ---- 1. Main logic -------------------------------------------------
def main() -> None:
    """
    This function asks the user for their name and responds.
    """
    # Ask the user for their name
name = input ("what is your name?")


    # Respond with a greeting
greeting = input ("Hello " + str(name) + ", how are you doing?")
   
    # Optional challenge: Ask for age and respond
age = input ( "What is your age?")
age_num = int(age)
until_25 = 1000-age_num
print("You have " + str(until_25) + " years until you are 1000 years old.")
# ---- 2. “Guard” to run main() when executed directly ---------------
if __name__ == "__main__":
    main()

"""
How to run: 
1) Open Terminal (Ctrl + Shift + `)
2) type: python week1_1.py
3) Program should run! Let us know if it doesn't

"""