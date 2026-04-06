questions = [
    ["Who is known as the father of Computer?", "Newton", "Einstein", "Charles Babbage", "Tesla", 3],
    ["Which planet is called the Red Planet?", "Mars", "Earth", "Jupiter", "Venus", 1],
    ["What is the national flower of Nepal?", "Rose", "Lali Gurans", "Lotus", "Sunflower", 2],
    ["Who invented the Telephone?", "Graham Bell", "Newton", "Edison", "Tesla", 1],
    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],

    ["HTML stands for?", "Hyper Trainer Marking Language", "Hyper Text Markup Language", "High Text Machine Language", "Hyper Tool Multi Language", 2],
    ["Which is the fastest land animal?", "Lion", "Cheetah", "Horse", "Tiger", 2],
    ["What is 5 × 12?", "60", "50", "72", "55", 1],
    ["Which device measures temperature?", "Barometer", "Thermometer", "Speedometer", "Hygrometer", 2],
    ["What is the capital city of Japan?", "Seoul", "Beijing", "Tokyo", "Bangkok", 3],

    ["Who discovered Gravity?", "Newton", "Einstein", "Galileo", "Tesla", 1],
    ["Which is the longest river in the world?", "Amazon", "Ganga", "Nile", "Koshi", 3],
    ["RAM is — ?", "Permanent Memory", "Temporary Memory", "Secondary Memory", "Magnetic Memory", 2],
    ["Which organ pumps blood?", "Heart", "Lungs", "Brain", "Kidney", 1],
    ["Where is Mount Everest located?", "China", "India", "Japan", "Nepal", 4],

    ["Which country invented Paper?", "Nepal", "USA", "China", "India", 3],
    ["What is H2O?", "Salt", "Water", "Sugar", "Gas", 2],
    ["Which ocean is the largest?", "Atlantic", "Pacific", "Indian", "Arctic", 2],
    ["Who wrote ‘Ramayana’?", "Valmiki", "Tulsidas", "Kalidas", "Vyasa", 1],
    ["Which is the smallest prime number?", "1", "2", "3", "5", 2],

    ["What is the boiling point of water?", "50°C", "100°C", "90°C", "120°C", 2],
    ["Which is the national animal of Nepal?", "Cow", "Tiger", "Rhino", "Leopard", 1],
    ["CPU stands for?", "Central Processing Unit", "Central Power Unit", "Control Processing Unit", "Central Program Unit", 1],
    ["Which instrument measures air pressure?", "Barometer", "Hygrometer", "Ammeter", "Altimeter", 1],
    ["Python is a — ?", "Microprocessor", "Snake", "Programming Language", "Operating System", 3],

    ["Which continent is the largest?", "Africa", "Asia", "Europe", "Australia", 2],
    ["Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["What does SMS stand for?", "Short Message Service", "Simple Mail System", "Send Message Service", "Signal Message System", 1],
    ["Which is the closest star to Earth?", "Sirius", "Alpha Centauri", "Sun", "Polaris", 3],
    ["Which organ is responsible for filtering blood?", "Liver", "Heart", "Kidney", "Lungs", 3]
]

levels = [
    1000, 2000, 3000, 5000, 10000,
    20000, 40000, 80000, 160000, 320000,
    640000, 1250000, 2500000, 5000000, 10000000,
    20000000, 30000000, 50000000, 75000000, 100000000,
    150000000, 200000000, 300000000, 500000000, 1000000000
]
money = 0

for i in range(len(levels)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"Q. {question[0]}")  # <-- prints the question text
    print(f"1. {question[1]} 2. {question[2]} ")
    print(f"3. {question[3]} 4. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))

    if reply == 0:
        money = levels[i-1]
        break

    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")
