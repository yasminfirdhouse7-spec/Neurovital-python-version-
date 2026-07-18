import time
import os

# ==============================
# GLOBAL VARIABLES
# ==============================

health_score = 100

username = ""
password = ""

water_glasses = 0
water_goal = 8

sleep_hours = 0

mood = ""

medicine_name = ""
medicine_time = ""

risk_level = ""

weight = 0.0
height = 0.0
bmi = 0.0

heart_rate = 0


# ==============================
# LOADING EFFECT
# ==============================

def loading_effect():
    print("\nLoading", end="")

    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)

    print("\n")


# ==============================
# CLEAR SCREEN
# ==============================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ==============================
# LOGIN SYSTEM
# ==============================

def login():
    global username, password

    print("=" * 40)
    print("         NEUROVITAL")
    print("=" * 40)

    username = input("\nCreate Username: ")
    password = input("Create Password: ")

    print("\nLogin Successful!")
    loading_effect()


# ==============================
# MAIN MENU
# ==============================

def display_menu():
    print("\n" + "=" * 40)
    print("         MAIN DASHBOARD")
    print("=" * 40)

    print("1. Water Tracker")
    print("2. Sleep Tracker")
    print("3. Mood Tracker")
    print("4. Medicine Reminder")
    print("5. Symptom Checker")
    print("6. Health Dashboard")
    print("7. AI Chatbot")
    print("8. AI Health Tips")
    print("9. Health Risk System")
    print("10. Daily Health Report")
    print("11. Save User History")
    print("12. Heart Rate Monitor")
    print("13. BMI Calculator")
    print("14. Emergency Alert System")
    print("15. Exit")

    choice = int(input("\nEnter your choice: "))

    return choice# ==============================
# WATER TRACKER
# ==============================

def water_tracker():
    global water_glasses, health_score

    print("\n===== WATER TRACKER =====")

    water_glasses = int(input("How many glasses of water did you drink today? "))

    print(f"Daily Goal: {water_goal} glasses")

    if water_glasses < water_goal:
        print(f"You need {water_goal - water_glasses} more glasses to reach your goal.")
        print("Reminder: Drink more water!")
        health_score -= 5
    else:
        print("Congratulations! Water goal achieved!")
        health_score += 5


# ==============================
# SLEEP TRACKER
# ==============================

def sleep_tracker():
    global sleep_hours, health_score

    print("\n===== SLEEP TRACKER =====")

    sleep_hours = int(input("How many hours did you sleep? "))

    if sleep_hours < 6:
        print("Notification: You need more sleep!")
        health_score -= 20
    else:
        print("Good sleep schedule!")


# ==============================
# MOOD TRACKER
# ==============================

def mood_tracker():
    global mood, health_score

    print("\n===== MOOD TRACKER =====")

    mood = input("Enter your mood (happy/sad/average): ").lower()

    if mood == "happy":
        print("Great! Keep smiling today.")
        health_score += 5

    elif mood == "sad":
        print("Take some rest and relax.")
        health_score -= 5

    elif mood == "average":
        print("Hope your day gets even better.")

    else:
        print("Mood recorded successfully.")


# ==============================
# MEDICINE REMINDER
# ==============================

def medicine_reminder():
    global medicine_name, medicine_time

    print("\n===== MEDICINE REMINDER =====")

    medicine_name = input("Enter medicine name: ")
    medicine_time = input("Enter medicine time: ")

    print("Medicine reminder saved successfully!")# ==============================
# SYMPTOM CHECKER
# ==============================

def symptom_checker():
    global health_score

    print("\n===== SYMPTOM CHECKER =====")

    fever = input("Do you have fever? (y/n): ").lower()
    headache = input("Do you have headache? (y/n): ").lower()
    cold = input("Do you have cold? (y/n): ").lower()
    tiredness = input("Do you feel tiredness? (y/n): ").lower()

    if fever == "y":
        health_score -= 15

    if headache == "y":
        health_score -= 10

    if cold == "y":
        health_score -= 10

    if tiredness == "y":
        health_score -= 15

    loading_effect()
    print("Symptoms analyzed successfully!")


# ==============================
# HEART RATE MONITOR
# ==============================

def heart_rate_monitor():
    global heart_rate, health_score

    print("\n===== HEART RATE MONITOR =====")

    heart_rate = int(input("Enter your heart rate (BPM): "))

    if heart_rate < 60:
        print("AI Analysis: Low heart rate detected!")
        print("Possible weakness or low blood pressure.")
        health_score -= 15

    elif heart_rate > 100:
        print("AI Analysis: High heart rate detected!")
        print("Possible stress, anxiety, or fever.")
        health_score -= 20

    else:
        print("AI Analysis: Heart rate is normal.")


# ==============================
# BMI CALCULATOR
# ==============================

def bmi_calculator():
    global weight, height, bmi, health_score

    print("\n===== BMI CALCULATOR =====")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    bmi = weight / (height * height)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("AI Analysis: Underweight")
        health_score -= 10

    elif 18.5 <= bmi <= 24.9:
        print("AI Analysis: Normal weight")

    elif 25 <= bmi <= 29.9:
        print("AI Analysis: Overweight")
        health_score -= 10

    else:
        print("AI Analysis: Obesity detected")
        health_score -= 20


# ==============================
# EMERGENCY ALERT SYSTEM
# ==============================

def emergency_alert_system():
    global health_score

    print("\n===== EMERGENCY ALERT SYSTEM =====")

    if health_score < 40:
        print("EMERGENCY ALERT ACTIVATED!")
        print("Critical health condition detected!")
        print("Sending emergency notification...")
        print("Contacting nearby healthcare support...")

    else:
        print("No emergency detected.")# ==============================
# HEALTH RISK SYSTEM
# ==============================

def health_risk_system():
    global risk_level

    print("\n===== HEALTH RISK SYSTEM =====")

    if health_score >= 80:
        risk_level = "LOW"

    elif health_score >= 50:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    print(f"Risk Level: {risk_level}")

    if risk_level == "HIGH":
        print("WARNING: Please consult a doctor immediately!")


# ==============================
# AI HEALTH TIPS
# ==============================

def ai_health_tips():
    print("\n===== AI HEALTH TIPS =====")

    if water_glasses < 5:
        print("- Drink more water daily.")

    if sleep_hours < 6:
        print("- Improve your sleep schedule.")

    if health_score < 50:
        print("- Take proper rest and monitor symptoms.")

    if health_score >= 80:
        print("- Great job! Maintain your healthy routine.")


# ==============================
# HEALTH DASHBOARD
# ==============================

def health_dashboard():
    print("\n===== HEALTH DASHBOARD =====")

    print(f"Username       : {username}")
    print(f"Water Intake   : {water_glasses} glasses")
    print(f"Mood           : {mood}")
    print(f"Sleep Hours    : {sleep_hours} hours")
    print(f"Heart Rate     : {heart_rate} BPM")
    print(f"BMI            : {bmi:.2f}")
    print(f"Medicine       : {medicine_name}")
    print(f"Medicine Time  : {medicine_time}")
    print(f"Health Score   : {health_score}/100")
    print(f"Risk Level     : {risk_level}")


# ==============================
# DAILY HEALTH REPORT
# ==============================

def daily_health_report():
    print("\n===== DAILY HEALTH REPORT =====")

    print(f"Health Score: {health_score}/100")

    if health_score >= 80:
        print("Overall Status: Healthy")

    elif health_score >= 50:
        print("Overall Status: Moderate")

    else:
        print("Overall Status: Unhealthy")


# ==============================
# SAVE USER HISTORY
# ==============================

def user_history():
    with open("health_history.txt", "a", encoding="utf-8") as file:

        file.write("\n===== USER HISTORY =====\n")
        file.write(f"Username: {username}\n")
        file.write(f"Water Intake: {water_glasses}\n")
        file.write(f"Mood: {mood}\n")
        file.write(f"Sleep Hours: {sleep_hours}\n")
        file.write(f"Heart Rate: {heart_rate}\n")
        file.write(f"BMI: {bmi:.2f}\n")
        file.write(f"Medicine: {medicine_name}\n")
        file.write(f"Medicine Time: {medicine_time}\n")
        file.write(f"Health Score: {health_score}\n")
        file.write(f"Risk Level: {risk_level}\n")

    print("\nUser history saved successfully!")# ==============================
# AI CHATBOT
# ==============================

def ai_chatbot():
    print("\n===== AI CHATBOT =====")
    print("Type 'exit' to stop chatting.\n")

    while True:
        question = input("Ask AI Chatbot: ").lower()

        if question == "exit":
            break

        elif "fever" in question:
            print("AI: Drink fluids and monitor your temperature.")

        elif "headache" in question:
            print("AI: Take proper rest and stay hydrated.")

        elif "cold" in question:
            print("AI: Drink warm fluids and rest.")

        elif "stress" in question:
            print("AI: Try meditation and proper sleep.")

        elif "sleep" in question:
            print("AI: Maintain 7-8 hours of sleep daily.")

        else:
            print("AI: Please consult a healthcare professional.")


# ==============================
# MAIN PROGRAM
# ==============================

login()

while True:

    choice = display_menu()

    if choice == 1:
        water_tracker()

    elif choice == 2:
        sleep_tracker()

    elif choice == 3:
        mood_tracker()

    elif choice == 4:
        medicine_reminder()

    elif choice == 5:
        symptom_checker()

    elif choice == 6:
        health_dashboard()

    elif choice == 7:
        ai_chatbot()

    elif choice == 8:
        ai_health_tips()

    elif choice == 9:
        health_risk_system()

    elif choice == 10:
        daily_health_report()

    elif choice == 11:
        user_history()

    elif choice == 12:
        heart_rate_monitor()

    elif choice == 13:
        bmi_calculator()

    elif choice == 14:
        emergency_alert_system()

    elif choice == 15:
        print("\nThank you for using NeuroVital!")
        break

    else:
        print("\nInvalid choice!")

    input("\nPress Enter to continue...")
    clear_screen()