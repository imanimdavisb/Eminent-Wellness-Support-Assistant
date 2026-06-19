print("=== Eminent Wellness Support Assistant ===")

print("\nDISCLAIMER:")
print("This tool does not replace a therapist or emergency support.")
print("If you are experiencing an emergency, call 911 or 988.\n")

name = input("Name: ")
contact = input("Phone or Email: ")

reason = input(
    "\nBriefly describe why you are seeking support today:\n"
)

stress_level = input(
    "\nStress Level (Low, Moderate, High): "
)

print("\nSupport Categories")
print("1. Grief Counseling")
print("2. Anxiety / Stress")
print("3. Family Support")
print("4. Community Resources")

choice = input("\nSelect 1-4: ")

if choice == "1":
    category = "Grief Counseling"
    next_step = "Schedule a grief counseling consultation."
elif choice == "2":
    category = "Anxiety / Stress"
    next_step = "Schedule a wellness assessment."
elif choice == "3":
    category = "Family Support"
    next_step = "Connect with a family support specialist."
elif choice == "4":
    category = "Community Resources"
    next_step = "Receive a list of local community resources."
else:
    category = "General Support"
    next_step = "Staff review required."

print("\n" + "="*40)
print("CLIENT INTAKE SUMMARY")
print("="*40)

print(f"Name: {name}")
print(f"Contact: {contact}")
print(f"Reason: {reason}")
print(f"Stress Level: {stress_level}")

print(f"\nResource Category: {category}")
print(f"Suggested Next Step: {next_step}")

print("\nSummary for Staff:")
print(
    f"{name} is seeking support related to "
    f"{category.lower()}. "
    f"Reported stress level: {stress_level}."
)

print("\nThank you for completing the intake.")
