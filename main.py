from pyscript import document
import random

def get_team(event):

    regis_checked = document.querySelector('input[name="regis"]:checked')
    medcert_checked = document.querySelector('input[name="medcert"]:checked')

    if not regis_checked or not medcert_checked or regis_checked.value == "No" or medcert_checked.value == "No":
        document.getElementById("team_name").innerText = "Please complete registration and medical certificate to join a team."
        document.getElementById("team_img").src = ""
        return
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    if not grade or not section:
        document.getElementById("team_name").innerText = "Please select both a grade and a section to sign up."
        document.getElementById("team_img").src = ""
        return

    if grade in ["g7", "g8", "g9", "g10"]:
        teams = ["Red Bulldogs!", "Green Hornets!", "Blue Bears!", "Yellow Tigers!"]
        name = random.choice(teams)  
        img = name.split()[0].lower() + ".jpg"
    else:
        name, img = "Special Case!", ""

    document.getElementById("team_name").innerText = name
    document.getElementById("team_img").src = img
