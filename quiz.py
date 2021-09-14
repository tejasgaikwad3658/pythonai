import json

constant_keyword= "quiz"
constant_question_keyword= "question"
constant_answer_keyword ="answer"
constant_options_keyword ="options"

#open the json file
f= open("quiz.json",)

#loading the json file converting it to dictionary
data = json.load(f)

#list to identify quiz type sport/maths
quiz_geners_list=[]

#itterating through the json to find the genres
for i in data['quiz']: 
    quiz_geners_list.append(i)

#global score variable
score =0

#Terminal UI
print("\n!!!WElCOME TO THE QUIZ!!!")
print("\nEnter Your Gener of Quiz :\n1.Sport\n2.Maths\n3.Quit")
gener_input=int(input("\nEnter your choice : "))

if gener_input == 3:
    print("\nHope to see you soon!!!\n")
    exit()

print("\nYou have selected  --->", quiz_geners_list[gener_input-1])
selected_gener_name=quiz_geners_list[gener_input-1]

counter=1
options_array=[]

for i in data['quiz'][selected_gener_name]:
    question_set=[]
    question_set.append(i)
    question_count= len(question_set)

    print("\nQuestion -> ",data[constant_keyword][selected_gener_name][i][constant_question_keyword])
    answer_list=[]
    answer_list.append(data[constant_keyword][selected_gener_name][i][constant_answer_keyword])

    print("\nOptions are -> ")
    for i in data['quiz'][selected_gener_name][i][constant_options_keyword]:
        print( counter,")", i)
        options_array.append(i)
        counter=counter+1

answer = int(input("\nYour answer : "))

if (options_array[answer-1] == answer_list[0]) == True:
    print("\nCorrect Answer!!!\n")
    score =score+10
else:
    print("\nOppssiee Wrong Answer!!!\n") 

print("\nQuiz Score : ", score," Points\n")

#closing the json file
f.close()

