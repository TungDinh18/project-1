print('Hello!')
name = input('What is your name? ')
print('Hello, ' + name + '!')
print('How are you feeling today?')
print('1. Good')
print('2. Bad')
print('3. OK')
feeling = int(input('Please choose one option number: '))
if feeling > 3:
  print('Please choose a valid option.')
if feeling == 1:
  print('Glad to hear that!')
if feeling == 2:
  print('Sorry to hear that.')
if feeling == 3:
  print('OK is fine.')

def algorithm():
  print('What else would you like to talk about?')
  print('1. Weather')
  print('2. Food')
  print('3. Hobbies')
  print('4. Maths')
  print('5. Science')
  print('6. History')
  print('7. Geography')
  print('8. Music')
  print('9. Art')
  print('10. Sports')
  topic = int(input('Please choose one option number: '))
  if topic > 10:
    print('Please choose a valid option.')
  print('I think that is a great topic!')
  if topic == 1:
    print('What is the weather like today?')
    print('1. Sunny')
    print('2. Rainy')
    print('3. Cloudy')
    print('4. Snowy')
    print('5. Windy')
    print('6. Foggy')
    weather = input('Please pick using one of the numbers: ')
    if weather == '1':
      print('That is a great day to go outside!')
    if weather == '2':
      print('You should stay inside and read a book.')
    if weather == '3':
      print('It is a bit cloudy today.')
    if weather == '4':
      print('It is snowing outside, go build a snowman!')
    if weather == '5':
      print('It is windy outside, be careful!')
    if weather == '6':
      print('It is foggy outside, can you see?')
  if topic == 2:
    print('What is your favourite food?')
    food = input('Please type your favourite food: ')
    print(food + ' is a good choice')
  if topic == 3:
    print('What is your favourite hobby?')
    hobby = input('Please type your favourite hobby: ')
    print(hobby + ' is a good hobby')
  if topic == 4:
    print('What is your favourite maths topic?')
    maths = input('Please type your favourite maths topic: ')
    print(maths + ' is a good maths topic')
  if topic == 5:
    print('What is your favourite science topic?')
    science = input('Please type your favourite science topic: ')
    print(science + ' is a good science topic')
  if topic == 6:
    print('What is your favourite history topic?')
    history = input('Please type your favourite history topic: ')
    print(history + ' is a good history topic')
  if topic == 7:
    print('What is your favourite geography topic?')
    geography = input('Please type your favourite geography topic: ')
    print(geography + ' is a good geography topic')
  if topic == 8:
    print('What is your favourite music piece?')
    music = input('Please type your favourite music piece: ')
    print(music + ' sounds good, nice choice')
  if topic == 9:
    print('What is your favourite art piece?')
    art = input('Please type your favourite art piece: ')
    print(art + ' is a good art piece, can you draw it?')
  if topic == 10:
    print('What is your favourite sport?')
    sport = input('Please type your favourite sport: ')
    print(sport + ' is a good sport, do you play it?')
  print('Would you like to talk about something else?')
  print('1. Yes')
  print('2. No')
  choice = int(input('Please choose one option number: '))
  if choice == 1:
    algorithm()
  if choice == 2:
    print('Goodbye, ' + name + '!')
    exit()
algorithm()
