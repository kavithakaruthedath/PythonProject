date = input("Enter today's date : ")
mood = input("How do you rate your mood today from 1 to 10? ")
thought = input("Thought of the day : ")

with open("files/{date}.txt", "w") as file:
    file.write(mood)
    file.write(thought)

