#! python3

import random
   # The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 
   'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states=list(capitals.keys())

def isAnswer(option, answer):
    return option == answer

   # Generate 35 quiz files.
for file_num in range(35):
    # TODO: Create the quiz and answer key files.
    capital_quiz_file=open(f'capital_quiz_{file_num + 1}.txt', 'w')
    capital_quiz_answer_file=open(f'capital_quiz_{file_num + 1}_answer.txt', 'w')

    # TODO: Write out the header for the quiz.
    capital_quiz_file.write('Capital Quiz\n\nName:\n\n')

    # TODO: Shuffle the order of the states.
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for quiz_num in range(len(states)):
        state=states[quiz_num]
        
        answer=capitals[state]

        # wrong_answers=list(filter(lambda capital: capital != answer, capitals.values()))
        wrong_answers=list(capitals.values())
        del wrong_answers[wrong_answers.index(answer)]

        # three_wrong_answers=random.choices(wrong_answers, k=3)
        three_wrong_answers=random.sample(wrong_answers, k=3)

        # answers=[answer, *wrong_answers]
        answers = [answer] + three_wrong_answers
        random.shuffle(answers)

        capital_quiz_file.write(f"""
  {quiz_num + 1}. What is the capital of {state}?
      a. {answers[0]}
      b. {answers[1]}
      c. {answers[2]}
      d. {answers[3]}
        """)

        capital_quiz_answer_file.write(f'{quiz_num + 1}. {"abcd"[answers.index(answer)]}\n')

        capital_quiz_file.close()
        capital_quiz_answer_file.close()