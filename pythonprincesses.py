print('Welcome Patient to the South Georgia Medical Center',end='')
print(' Research Study')
print()
print('GENERAL QUESTIONS:')
name = input('Please enter your full name here:\n')
age = input('What is your age?\n')
print()
print("Your name is",name,"and your are",age,"years old")
print()

correct_statement = int(input('Is this correct? Please enter 1 for Yes and 0 for No:\n'))



if correct_statement == 1:
    print("Great! Let's continue!")
elif correct_statement == 0:
    print('Please reenter your information')
    name = input('What is your name?\n')
    age = input('What is your age?\n')
    print("Your name is",name,"and your are",age,"years old")
 
else:
    print("Reenter information please")
    name = input('What is your name?\n')
    age = input('What is your age?\n')
    print("Your name is",name,"and your are",age,"years old")
print()
patient_feeling = int(input('How are you feeling today? (Please enter 1 for good and 0 for bad):\n'))
if patient_feeling == 1:
    print('Great!')
elif patient_feeling == 0:
    print('Please explain your concern to your doctor,')

print()
patient_problem = input("Ok, please describe your symptoms:\n")
print()
print('Great, thank you for letting us know that "',patient_problem,'". Your doctor', end='')
print(' will address your concern in your appointment')
print()
print()
print('Now we will begin our survey portion:\n')
print()
medication_tak = int(input('Are you taking any prescribed medication? Such as Opioids, Depressants, Stimulants, etc.,( 1 for Yes and 0 for No): \n'))
if medication_tak == 1:
    medication = input("What medication's are you taking?")
elif medication_tak == 0:
    print("Thank you for letting us know. Let's continue.")
else:
    print('Invalid input')
    print('Your doctor will address your medication.')

print()
print('PAIN REPORT:\n')
print()
pain_exper = int(input('Are you experiencing any pain?  ( 1 for Yes and 0 for No): \n'))
if pain_exper == 1:
    print('NOTICE: For the next set of questions please refer to the pain scale below:')
    print()
    print('1 - pain is barely noticeable')
    print('5 - pain is very distracting and may stop them from being able to do',end='')
    print('typical activities')
    print('10 - pain is bad enough to prevent moving on your own')
    pain_rate = input('Rate your pain on a scale of 1-10:')
    print() 
    print('Where is the pain located?')
    print('1- head\n2- Torso\n3- Below Pelvis\n4- Internal\n5- Elsewhere')
    pain_location = input('Your answer:')
    print()
    pain_triggering = input('What do you think is triggering the pain?')
    print()
    pain_impact = input('How has this impacted your quality of life?')
    pain_length = input('How long have you been experiencing this pain?')
if pain_exper == 0:
    print('PLEASE CONTINUE TO THE NEXT SECTION')
else:
    ('Please address any concerns in the following appointments.')
print()
print('DROWSINESS REPORT')
print('Have you been experiencing any form of drowsiness in the past 7 days?')
print('1- Yes')
print('0- No')
drowsiness_level = input('Your Answer:\n')
print()
print('MENTAL HEALTH REPORT:')
print()
print('NOTICE: Please refer to below to answer questions 1-10.')
print()
print('0- Never\n1- Rarely\n2- sometimes\n3- Mostly\n4- Always')
Lack_energy = int(input('In the last 7 days have you felt a lack of energy?\n'))
if Lack_energy >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
focus_question = int(input('In the last 7 days have you had trouble focusing?\n'))
if focus_question >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
depressed_question = int(input('In the las 7 days have you felt sad or depressed?\n'))
if depressed_question  >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
future = int(input('In the last 7 days have you felt hopeless about the future?\n'))
if  future >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
lonely = int(input('In the last 7 days have you felt extreme loneliness?\n'))
if  lonely >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')

appetite = int(input('In the last 7 days have you had little to no appetite?\n'))
if  appetite >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
distracted = int(input('In the last 7 days have you felt easily distracted?\n'))
if  distracted >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
halluncinations = int(input("In the last 30 days have you experienced physical symspton such as Halluncinations that aren't there\n"))
if  halluncinations >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
sleep= int(input("In the last 30 days have you experinced any symptoms of insomnia such as lack of sleep, daily exhuastion, and fatigue?\n"))
if sleep  >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
memory = int(input('In the past 30 days have you had trouble retaining memory?\n'))
if  memory >= 3:
    explain = input('Please explain:\n')
else:
    print('Continue to next question.')
print()
print('Thank you for your time',name,'. Your information will be recorded and will be review by a doctor to dicuss further treatment plans.')
 








