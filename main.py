from pyscript import display, document

def intrams_qualifications(event):
    document.getElementById("output").innerHTML = ""

    grade_input = document.getElementById("grade").value
    section = document.getElementById("section").value

    registration = document.querySelector('input[name="reg"]:checked')
    medical = document.querySelector('input[name="med"]:checked')

    if grade_input == "" or not grade_input.isdigit():
        display("Please enter a valid grade level.", target="output")
        return

    grade = int(grade_input)

    if registration is None or medical is None or section == "":
        display("Make sure all fields are answered.", target="output")
        return

    if registration.value != "yes":
        display("You must complete the online registration first.", target="output")
        return

    if medical.value != "cleared":
        display("Medical clearance is required to participate.", target="output")
        return

    if grade < 7 or grade > 10:
        display("This activity is only for Grades 7 to 10.", target="output")
        return

    if grade == 7 and section == "Ruby":
        display("Grade 7 Ruby belongs to the Green Hornets!", target="output")
    elif grade == 7 and section == "Sapphire":
        display("Grade 7 Sapphire belongs to the Yellow Tigers!", target="output")
    elif grade == 7 and section == "Emerald":
        display("Grade 7 Emerald belongs to the Blue Bears!", target="output")
    elif grade == 7 and section == "Topaz":
        display("Grade 7 Topaz belongs to the Red Bulldogs!", target="output")

    elif grade == 8 and section == "Ruby":
        display("Grade 8 Ruby belongs to the Yellow Tigers!", target="output")
    elif grade == 8 and section == "Sapphire":
        display("Grade 8 Sapphire belongs to the Green Hornets!", target="output")
    elif grade == 8 and section == "Emerald":
        display("Grade 8 Emerald belongs to the Red Bulldogs!", target="output")
    elif grade == 8 and section == "Topaz":
        display("Grade 8 Topaz belongs to the Blue Bears!", target="output")


    elif grade == 9 and section == "Ruby":
        display("Grade 9 Ruby belongs to the Blue Bears!", target="output")
    elif grade == 9 and section == "Sapphire":
        display("Grade 9 Sapphire belongs to the Red Bulldogs!", target="output")
    elif grade == 9 and section == "Emerald":
        display("Grade 9 Emerald belongs to the Green Hornets!", target="output")
    elif grade == 9 and section == "Topaz":
        display("Grade 9 Topaz belongs to the Yellow Tigers!", target="output")

    elif grade == 10 and section == "Ruby":
        display("WOW! Grade 10 Ruby is part of the Blue Bears", target="output")
    elif grade == 10 and section == "Sapphire":
        display("WOW! Grade 10 Sapphire is part of the Green Hornets", target="output")
    elif grade == 10 and section == "Emerald":
        display("WOW! Grade 10 Emerald is part of the Yellow Tigers", target="output")
    elif grade == 10 and section == "Topaz":
        display("WOW! Grade 10 Topaz is part of the Red Bulldogs", target="output")

    else:
        display("Something went wrong. Please check your inputs.", target="output")
