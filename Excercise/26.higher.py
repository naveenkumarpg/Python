import random

data = [
    {"What is the population of Australia.?": "25687041"},
    {"What is the height of Mount Everest in meters.?": "8848"},
    {"What is the current year.?": "2024"},
    {"How many countries are there in the world.?": "195"},
    {"What is the speed of light in km/s.?": "299792"},
    {"How many bones are in the human body.?": "206"},
    {"What is the boiling point of water in degrees Celsius.?": "100"},
    {"How many elements are in the periodic table.?": "118"},
    {"How many minutes are there in a day.?": "1440"},
    {"What is the atomic number of Carbon.?": "6"},
    {"How many planets are in the Solar System.?": "8"},
    {"What is the distance from the Earth to the Moon in kilometers.?": "384400"},
    {"What is the capital city of Japan's population.?": "13929286"},
    {"How many zeros are in a trillion.?": "12"},
    {"What is the diameter of Earth in kilometers.?": "12742"},
    {"How many weeks are there in a year.?": "52"},
    {"What is the age of the oldest person ever recorded.?": "122"},
    {"How many stars are on the flag of the United States.?": "50"},
    {"How many chromosomes do humans have.?": "46"},
    {"How many Great Lakes are there.?": "5"},
    {"What is the world record for the 100m sprint in seconds.?": "9.58"},
    {"How many milliliters are in a liter.?": "1000"},
    {"What is the height of the Eiffel Tower in meters.?": "324"},
    {"How many hours are in a week.?": "168"},
    {"What is the freezing point of water in Fahrenheit.?": "32"},
    {"How many continents are there on Earth.?": "7"},
    {"How many letters are in the English alphabet.?": "26"},
    {"What is the average life expectancy in years globally.?": "72"},
    {"How many meters are in a kilometer.?": "1000"},
    {"How many degrees are in a circle.?": "360"},
    {"What is the highest score in a single game of basketball by one player in the NBA.?": "100"},
    {"How many legs does a spider have.?": "8"},
    {"How many players are there in a soccer team on the field.?": "11"},
    {"How many countries are in the European Union.?": "27"},
    {"What is the lifespan of a domestic cat in years.?": "15"},
    {"How many moons does Mars have.?": "2"},
    {"What is the speed of sound in air at sea level in m/s.?": "343"},
    {"How many teeth does an adult human have.?": "32"},
    {"What is the atomic number of Oxygen.?": "8"},
    {"How many Oscars did the movie Titanic win.?": "11"},
    {"What is the normal human body temperature in degrees Celsius.?": "37"},
    {"How many sides does a hexagon have.?": "6"},
    {"What is the capital of France's population.?": "2161000"},
    {"How many hours are there in a day.?": "24"},
    {"What is the circumference of Earth in kilometers.?": "40075"},
    {"How many miles is a marathon.?": "26.2"},
    {"What is the maximum number of points in a game of Pac-Man.?": "3333360"},
    {"How many dots are there on two dice.?": "42"},
    {"How many valves does the human heart have.?": "4"},
    {"What is the number of amendments to the US Constitution.?": "27"},
    {"How many syllables are in the word 'supercalifragilisticexpialidocious'.?": "14"},
    {"How many hearts does an octopus have.?": "3"},
    {"What is the highest number used in a Sudoku puzzle.?": "9"},
    {"How many states are there in Australia.?": "6"},
    {"What is the average number of taste buds on a human tongue.?": "10000"},
    {"How many paintings did Vincent van Gogh sell during his lifetime.?": "1"},
    {"What is the highest possible score in a game of bowling.?": "300"},
    {"How many centimeters are there in an inch.?": "2.54"},
    {"How many players are there in a rugby team on the field.?": "15"},
    {"What is the total number of James Bond films as of 2023.?": "27"},
    {"How many wings does a bee have.?": "4"},
    {"How many seconds are in an hour.?": "3600"},
    {"What is the population of New York City.?": "8419600"},
    {"How many letters are there in the Greek alphabet.?": "24"},
    {"What is the world population.?": "8000000000"},
    {"How many prime numbers are there between 1 and 100.?": "25"},
    {"How many US presidents have there been.?": "46"},
    {"How many millimeters are there in a meter.?": "1000"},
    {"How many centimeters are there in a meter.?": "100"},
    {"How many bytes are in a kilobyte.?": "1024"},
    {"How many strings does a standard guitar have.?": "6"},
    {"What is the maximum number of players in a game of Texas Hold'em poker.?": "10"},
    {"How many bones are there in a giraffe's neck.?": "7"},
    {"What is the distance from the Earth to the Sun in kilometers.?": "149600000"},
    {"How many stripes are on the flag of the United States.?": "13"},
    {"What is the number of moons orbiting Jupiter.?": "79"},
    {"How many Harry Potter books are there.?": "7"},
    {"What is the world record for the men's marathon in hours.?": "2.01"},
    {"How many players are there in a basketball team on the court.?": "5"},
    {"How many kilometers are in a mile.?": "1.609"},
    {"How many World Wars have there been.?": "2"},
    {"How many legs does a crab have.?": "10"},
    {"What is the population of Canada.?": "38008005"},
    {"How many squares are there on a chessboard.?": "64"},
    {"How many edges does a cube have.?": "12"},
    {"What is the atomic number of Hydrogen.?": "1"},
    {"How many kilometers are in a nautical mile.?": "1.852"},
    {"How many provinces are there in Canada.?": "10"},
    {"How many sides does a pentagon have.?": "5"},
    {"What is the population of India.?": "1417000000"},
    {"How many days are there in February in a leap year.?": "29"},
    {"How many teams are there in the NFL.?": "32"},
    {"How many bones are in a shark's body.?": "0"},
    {"How many hours of video are uploaded to YouTube every minute.?": "500"},
    {"What is the atomic number of Gold.?": "79"},
    {"How many sides does a triangle have.?": "3"},
    {"What is the distance between the Earth and Mars in kilometers.?": "225000000"}
]

score = 0
continue_game = True

print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print("~ ~ ~ ~ ~ ~ Welcome to Higher or Lower game ~ ~ ~ ~ ~ ~")
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')

question_one_data = random.choice(data)
question_one = 'Question One'
question_one_answer = 0

for key in question_one_data:
    question_one = key
    question_one_answer = int(question_one_data[key])

while continue_game == True:
    question_two_data = random.choice(data)
    question_two = 'Question Two'
    question_two_answer = 0
    for key in question_two_data:
        question_two = key
        question_two_answer = int(question_two_data[key])

    print('----------------------------------------------------------------')
    print(f'Question 1 : {question_one}')
    print(f'Answer     : {question_one_answer}')
    print("VS")
    print(f'Question 2 : {question_two}')
    print('----------------------------------------------------------------')

    print("What is your answer 'Higher' or 'Lower .?'")
    answer = input("Answer : ")

    print(f"Answer is : {question_two_answer}")

    if(answer.lower() == 'higher'):
        if(question_two_answer > question_one_answer) :
            score = score + 1 
            print(f'Congratulations..! You Won, and score is : {score}')
            question_one = question_two
            question_one_answer = question_two_answer
        else :
            print(f'Ohhhh, you tried, your score is {score}')
            continue_game = False
    else :
        if(question_two_answer < question_one_answer) :
            score = score + 1 
            print(f'Congratulations..! You Won, and score is : {score}')
            question_one = question_two
            question_one_answer = question_two_answer
        else :
            print(f'Ohhhh, you tried, your score is {score}')
            continue_game = False
    
    