from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from markupsafe import escape
import random
import json
app = Flask(__name__)

# The actual ticket more to the right. 
# The words "Ticket Number Bigger"
# Redo of number.. 
# name should be centered 
# Ask if rewrite or append to previous. 
# 


ticket_no = 0 
dict_of_ticks = {}
dict_of_wins = {}

def start_over():
    ticket_no = 0 
    dict_of_ticks = {}
    dict_of_wins = {}
    ticket_no -= 1
    make_ticket()
    sort_tick()
    


def problem_changing():
    global possible_things_to_remove
    for n in problem_index:
        col_num = n
        if col_num == 1:
            condition(row1,1,9,col_num)
            list_of_tallies[0] += 1
        elif col_num == 2:
            condition(row1,10,19,col_num)
            list_of_tallies[1] += 1
        elif col_num == 3:
            condition(row1,20,29,col_num)
            list_of_tallies[2] += 1
        elif col_num == 4:
            condition(row1,30,39,col_num)
            list_of_tallies[3] += 1
        elif col_num == 5:
            condition(row1,40,49,col_num)
            list_of_tallies[4] += 1
        elif col_num == 6:
            condition(row1,50,59,col_num)
            list_of_tallies[5] += 1
        elif col_num == 7:
            condition(row1,60,69,col_num)
            list_of_tallies[6] += 1
        elif col_num == 8:
            condition(row1,70,79,col_num)
            list_of_tallies[7] += 1
        elif col_num == 9:
            condition(row1,80,90,col_num)
            list_of_tallies[8] += 1
        # try:
        
        
        try:
            row1.pop(possible_things_to_remove[0])
            del possible_things_to_remove[0]
        except:
            print("Going once")
            print(row1)
            print(possible_things_to_remove)
            print(problem_index)
            row1.pop(possible_things_to_remove[1])
            del possible_things_to_remove[1]
        
        # except:
        #     start_over()
def condition(row,min,max,col_num):
    val = 0
    while val in row.values() or val in list_of_values:
        val = random.randint(min,max)
    row[col_num] = val
    list_of_values.append(val)

def make_ticket():
    
    global ticket_no
    global list_of_values
    global possible_things_to_remove
    global row1
    global row2
    global row3
    global list_of_tallies
    global problem_index
    global lista

    ticket_no += 1 

    row1 = {0:0}
    row2 = {0:0}
    row3 = {0:0}

    list_of_values = []

    tally_of_1 = 0 
    tally_of_2 = 0 
    tally_of_3 = 0 
    tally_of_4 = 0 
    tally_of_5 = 0 
    tally_of_6 = 0 
    tally_of_7 = 0 
    tally_of_8 = 0 
    tally_of_9 = 0 

    list_of_tallies = [tally_of_1,tally_of_2,tally_of_3,tally_of_4,tally_of_5,tally_of_6,tally_of_7,tally_of_8,tally_of_9]

    for i in range(1,6):
        col_num = 0
        if col_num in row1:
            while col_num in row1:
                col_num = random.randint(1,9)
        if col_num == 1:
            condition(row1,1,9,col_num)
            list_of_tallies[0] += 1 
        elif col_num == 2:
            condition(row1,10,19,col_num)
            list_of_tallies[1] += 1
        elif col_num == 3:
            condition(row1,20,29,col_num)
            list_of_tallies[2] += 1 
        elif col_num == 4:
            condition(row1,30,39,col_num)
            list_of_tallies[3] += 1 
        elif col_num == 5:
            condition(row1,40,49,col_num)
            list_of_tallies[4] += 1 
        elif col_num == 6:
            condition(row1,50,59,col_num)
            list_of_tallies[5] += 1 
        elif col_num == 7:
            condition(row1,60,69,col_num)
            list_of_tallies[6] += 1 
        elif col_num == 8:
            condition(row1,70,79,col_num)
            list_of_tallies[7] += 1 
        elif col_num == 9:
            condition(row1,80,90,col_num)
            list_of_tallies[8] += 1 
    for i in range(1,6):
        col_num = 0
        if col_num in row2:
            while col_num in row2:
                col_num = random.randint(1,9)
        if col_num == 1:
            condition(row2,1,9,col_num)
            list_of_tallies[0] += 1
        elif col_num == 2:
            condition(row2,10,19,col_num)
            list_of_tallies[1] += 1
        elif col_num == 3:
            condition(row2,20,29,col_num)
            list_of_tallies[2] += 1
        elif col_num == 4:
            condition(row2,30,39,col_num)
            list_of_tallies[3] += 1
        elif col_num == 5:
            condition(row2,40,49,col_num)
            list_of_tallies[4] += 1
        elif col_num == 6:
            condition(row2,50,59,col_num)
            list_of_tallies[5] += 1
        elif col_num == 7:
            condition(row2,60,69,col_num)
            list_of_tallies[6] += 1
        elif col_num == 8:
            condition(row2,70,79,col_num)
            list_of_tallies[7] += 1
        elif col_num == 9:
            condition(row2,80,90,col_num)
            list_of_tallies[8] += 1
    for i in range(1,6):
        col_num = 0
        if col_num in row3:
            while col_num in row3:
                col_num = random.randint(1,9)
        if col_num == 1:
            condition(row3,1,9,col_num)
            list_of_tallies[0] += 1
        elif col_num == 2:
            condition(row3,10,19,col_num)
            list_of_tallies[1] += 1
        elif col_num == 3:
            condition(row3,20,29,col_num)
            list_of_tallies[2] += 1
        elif col_num == 4:
            condition(row3,30,39,col_num)
            list_of_tallies[3] += 1
        elif col_num == 5:
            condition(row3,40,49,col_num)
            list_of_tallies[4] += 1
        elif col_num == 6:
            condition(row3,50,59,col_num)
            list_of_tallies[5] += 1
        elif col_num == 7:
            condition(row3,60,69,col_num)
            list_of_tallies[6] += 1
        elif col_num == 8:
            condition(row3,70,79,col_num)
            list_of_tallies[7] += 1
        elif col_num == 9:
            condition(row3,80,89,col_num)
            list_of_tallies[8] += 1
    problem_index = []
    possible_things_to_remove = []

    for index,val in enumerate(list_of_tallies):
        
        if val == 0:
            problem_index.append(index+1)
        if val == 3:
            possible_things_to_remove.append(index+1)

    if len(possible_things_to_remove) < len(problem_index):
        print("::::::::::FIELDED")
        for index,val in enumerate(list_of_tallies):
            if val == 2 and index in row1.keys():
                possible_things_to_remove.append(index+1)
    if problem_index:
        problem_changing()    

    del row1[next(iter(row1))]
    del row2[next(iter(row2))]
    del row3[next(iter(row3))]

    lista = ["a","b","c"]

    

def sort_tick():
    global row1
    global row2
    global row3

    col1 = [[],[]]
    col2 = [[],[]]
    col3 = [[],[]]
    col4 = [[],[]]
    col5 = [[],[]]
    col6 = [[],[]]
    col7 = [[],[]]
    col8 = [[],[]]
    col9 = [[],[]]

    dictcol1 = {}
    dictcol2 = {}
    dictcol3 = {}
    dictcol4 = {}
    dictcol5 = {}
    dictcol6 = {}
    dictcol7 = {}
    dictcol8 = {}
    dictcol9 = {}

    row1a =  {}
    row2a = {}
    row3a = {}

    for i in row1:
        if i == 1:
            col1[0].append(1)
            col1[1].append(row1[i])
        if i == 2:
            col2[0].append(1)
            col2[1].append(row1[i])
        if i == 3:
            col3[0].append(1)
            col3[1].append(row1[i])
        if i == 4:
            col4[0].append(1)
            col4[1].append(row1[i])
        if i == 5:
            col5[0].append(1)
            col5[1].append(row1[i])
        if i == 6:
            col6[0].append(1)
            col6[1].append(row1[i])
        if i == 7:
            col7[0].append(1)
            col7[1].append(row1[i])
        if i == 8:
            col8[0].append(1)
            col8[1].append(row1[i])
        if i == 9:
            col9[0].append(1)
            col9[1].append(row1[i])
    for i in row2:
        if i == 1:
            col1[0].append(2)
            col1[1].append(row2[i])
        if i == 2:
            col2[0].append(2)
            col2[1].append(row2[i])
        if i == 3:
            col3[0].append(2)
            col3[1].append(row2[i])
        if i == 4:
            col4[0].append(2)
            col4[1].append(row2[i])
        if i == 5:
            col5[0].append(2)
            col5[1].append(row2[i])
        if i == 6:
            col6[0].append(2)
            col6[1].append(row2[i])
        if i == 7:
            col7[0].append(2)
            col7[1].append(row2[i])
        if i == 8:
            col8[0].append(2)
            col8[1].append(row2[i])
        if i == 9:
            col9[0].append(2)
            col9[1].append(row2[i])
    for i in row3:
        if i == 1:
            col1[0].append(3)
            col1[1].append(row3[i])
        if i == 2:
            col2[0].append(3)
            col2[1].append(row3[i])
        if i == 3:
            col3[0].append(3)
            col3[1].append(row3[i])
        if i == 4:
            col4[0].append(3)
            col4[1].append(row3[i])
        if i == 5:
            col5[0].append(3)
            col5[1].append(row3[i])
        if i == 6:
            col6[0].append(3)
            col6[1].append(row3[i])
        if i == 7:
            col7[0].append(3)
            col7[1].append(row3[i])
        if i == 8:
            col8[0].append(3)
            col8[1].append(row3[i])
        if i == 9:
            col9[0].append(3)
            col9[1].append(row3[i])
    col1[1].sort()
    for one,two in zip(col1[0],col1[1]):
        dictcol1.update({one:two})
    col2[1].sort()
    for one,two in zip(col2[0],col2[1]):
        dictcol2.update({one:two})
    col3[1].sort()
    for one,two in zip(col3[0],col3[1]):
        dictcol3.update({one:two})
    col4[1].sort()
    for one,two in zip(col4[0],col4[1]):
        dictcol4.update({one:two})
    col5[1].sort()
    for one,two in zip(col5[0],col5[1]):
        dictcol5.update({one:two})
    col6[1].sort()
    for one,two in zip(col6[0],col6[1]):
        dictcol6.update({one:two})
    col7[1].sort()
    for one,two in zip(col7[0],col7[1]):
        dictcol7.update({one:two})
    col8[1].sort()
    for one,two in zip(col8[0],col8[1]):
        dictcol8.update({one:two})
    col9[1].sort()
    for one,two in zip(col9[0],col9[1]):
        dictcol9.update({one:two})

    if 1 in dictcol1:
        row1a.update({1:dictcol1[1]})
    if 2 in dictcol1:
        row2a.update({1:dictcol1[2]})
    if 3 in dictcol1:
        row3a.update({1:dictcol1[3]})

    if 1 in dictcol2:
        row1a.update({2:dictcol2[1]})
    if 2 in dictcol2:
        row2a.update({2:dictcol2[2]})
    if 3 in dictcol2:
        row3a.update({2:dictcol2[3]})

    if 1 in dictcol3:
        row1a.update({3:dictcol3[1]})
    if 2 in dictcol3:
        row2a.update({3:dictcol3[2]})
    if 3 in dictcol3:
        row3a.update({3:dictcol3[3]})

    if 1 in dictcol4:
        row1a.update({4:dictcol4[1]})
    if 2 in dictcol4:
        row2a.update({4:dictcol4[2]})
    if 3 in dictcol4:
        row3a.update({4:dictcol4[3]})

    if 1 in dictcol5:
        row1a.update({5:dictcol5[1]})
    if 2 in dictcol5:
        row2a.update({5:dictcol5[2]})
    if 3 in dictcol5:
        row3a.update({5:dictcol5[3]})

    if 1 in dictcol6:
        row1a.update({6:dictcol6[1]})
    if 2 in dictcol6:
        row2a.update({6:dictcol6[2]})
    if 3 in dictcol6:
        row3a.update({6:dictcol6[3]})

    if 1 in dictcol7:
        row1a.update({7:dictcol7[1]})
    if 2 in dictcol7:
        row2a.update({7:dictcol7[2]})
    if 3 in dictcol7:
        row3a.update({7:dictcol7[3]})

    if 1 in dictcol8:
        row1a.update({8:dictcol8[1]})
    if 2 in dictcol8:
        row2a.update({8:dictcol8[2]})
    if 3 in dictcol8:
        row3a.update({8:dictcol8[3]})

    if 1 in dictcol9:
        row1a.update({9:dictcol9[1]})
    if 2 in dictcol9:
        row2a.update({9:dictcol9[2]})
    if 3 in dictcol9:
        row3a.update({9:dictcol9[3]})

    row1 = row1a
    row2 = row2a
    row3 = row3a

    print(row1)
    print(row2)
    print(row3)

@app.route('/')
def main():
    return redirect(url_for("index"))

@app.route('/index',methods=["POST","GET"])
def index():
    make_ticket()
    sort_tick()
    with open("test.json","w+") as f:
        l = [row1,row2,row3]
        t = "ticket" + str(ticket_no)
        dict_of_ticks.update({str(t):l})
        json.dump(dict_of_ticks,f)
    if request.method == "GET":
        return render_template("ticka.html",lista = lista,row1 = row1,row2 = row2,row3 = row3,ticket_no=ticket_no)
    else: 
        last_name = request.form.get("Nameis")
        if last_name == 'Last Name':
            print("On Noes!")
        elif last_name in dict_of_wins:
            tot_list = dict_of_wins[last_name]
            tot_list[0].append(ticket_no)
        else: 
            dict_of_wins.update({last_name:[[ticket_no]]})
        with open("tick_dicts.json","w+") as f:
            json.dump(dict_of_wins,f)
        return render_template('ticka.html',lista = lista,row1 = row1,row2 = row2,row3 = row3,ticket_no=ticket_no)
