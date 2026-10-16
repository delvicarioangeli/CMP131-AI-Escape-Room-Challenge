# ================================================================
# CMP 131 - AI ESCAPE ROOM CHALLENGE
# ================================================================
# Team members: Ayden S, Mikhial  A, Matthew C, Angelina D 
# Date: 10/16/2026
# Group project
# STORY:
# C.O.D.E., the classroom AI, accidentally locked the virtual lab.
# Complete the three levels to help the player escape.
#
# DIRECTIONS:
# Write your Python code below each numbered TODO.
# Use only concepts covered in class:
# print, input, variables, int, if/elif/else, and while loops.
# ================================================================


# ------------------------- INTRODUCTION --------------------------

# TODO 1:
# This introduction is provided. Run it and study the output.
player_name = input("Enter your name, brave programmer: ")

print("\nWelcome,", player_name + "!")
print("C.O.D.E., the classroom AI, locked the virtual lab.")
print("Complete three levels to escape!")


# ------------------- LEVEL 1: ACCESS CODE ------------------------

print("\nLEVEL 1: ACCESS CODE")
print("Enter the correct code to unlock the door.")

# These starting variables are provided.
correct_code = 131
door_status = "locked"
attempts = 0

# Continue to asked for the correct code until the door is unlocked. 
while door_status == "locked":
    code = int(input("Enter the access code: "))
    attempts += 1
    if code == correct_code:
        door_status = "unlocked"
    else:
        print("Incorrect code. Please try again.")
     # Display result after the loop ends 
    print("The door is unlocked!")
    print("You used", attempts, "attempts to unlock the door.")

# ---------------- LEVEL 2: COOLING SYSTEM ------------------------

# TODO 6:
print("\nLEVEL 2: COOLING SYSTEM")
print("A safe temperature is from 50 through 99.")

# The first temperature input is provided.
temperature = int(input("Enter the system temperature: "))

# TODO 7:
# Create a while loop that repeats when the temperature is unsafe.
while(temperature<50 or temperature>99):
    print("Too cold or overheating, Enter a new temperature ")
if(temperature<50):
    print("Too cold")
elif(temperature>99):
    print("OVERHEATING")
else:
    print("Safe to move on.")
temperature = int(input("Enter the system temperature: "))

# A temperature is unsafe when it is below 50 OR 100 or higher.
# Inside the loop:
#   1. If the temperature is below 50, display "Too cold."
#   2. Otherwise, display "Overheating."
#   3. Ask the player to enter a new temperature.

# TODO 8:
# After the loop ends, display that the temperature is safe.


# --------------- LEVEL 3: SECURITY DECISION ---------------------

#
print("\nLEVEL 3: SECURITY DECISION")
print("Choose: scan, shutdown, or share")

# The first security choice is provided.
choice = input("Enter your choice: ").lower()

while choice not in("scan", "shutdown", "share"):
    print("Oops! That is not a valid choice. Please Try Again.")
    choice = input("Enter scan, shutdown, or share: ").lower()
# TODO 10:
# Create a while loop that repeats when the choice is not valid.
# Inside the loop:
#   1. Display a friendly invalid-choice message.
#   2. Ask the player to enter scan, shutdown, or share again.
if choice == "scan":
    print("Starting a deep system scan for security threats. . .")
elif choice == "shutdown":
    print("Initiating emergency shutdown. Disconnecting. . .")
elif choice == "share":
    print("Preparing to share data. . . REMINDER: Never Share Your Passwords or Private Information with AI!")
# TODO 11:
# After the loop ends, use if/elif/else to display a different
# message for scan, shutdown, and share.
# The share message must remind the player not to share passwords
# or private information with AI.


# ----------------------- FINAL ESCAPE ----------------------------

# TODO 12:
# The final success message is provided.
print("\nCongratulations,", player_name + "!")
print("You escaped from C.O.D.E.'s virtual laboratory!")

# Add one friendly or funny final message written by your team.

print("You did it! now you gotta pay us for playing this game. jk, but seriously, you should pay us. ")
