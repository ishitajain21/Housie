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



# The purple color is awful. 
# Make both buttons bigger. 
'''Make Text ID Bigger'''
# Make recent number previosu number table bigger. 
# After ALL_DONE keep playing for a new round. 


list_of_numbers_to_highlighte_at_the_end = []
list_of_nums = []
list_of_nums_to_highlight_rn = []
wons = {}
cricket_lst = {10:"Tendulkar Num", 7 : "Dhoni Num",  18:"Kohli Num", 45:"Rohit Sharma Num", 12: "Yuvraj Singh Num", 11:"Num of players in team", 5:"Max days test game goes",4 : "Score when ball bounces over boundary", 6:" Score when ball crosses boundary(no bounce)"}

def start():
    global list_of_numbers_to_highlighte_at_the_end
    global list_of_nums
    global list_of_nums_to_highlight_rn

    list_of_numbers_to_highlighte_at_the_end = []
    list_of_nums = []
    list_of_nums_to_highlight_rn = []

    for i in range(1, 91):
        list_of_nums.append(i)

    while len(list_of_nums) != 0:
        number_selected = random.choice(list_of_nums)
        list_of_nums.remove(number_selected)
        list_of_numbers_to_highlighte_at_the_end.append(number_selected)
    print(list_of_numbers_to_highlighte_at_the_end)


start()
app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('boar.html',list=list_of_nums_to_highlight_rn)


@app.route("/housie", methods=["POST"])
def Num1():
    print(list_of_numbers_to_highlighte_at_the_end)
    print(list_of_nums)
    print(list_of_nums_to_highlight_rn)

    if 'Search' in request.form :
        req = request.form['quantity']
        with open('test.json','r') as file:
            data=file.read()
        try:
            obj = json.loads(data)
            requi = "ticket" + str(req) 
            dict_mess = obj[requi]
            print(dict_mess)
            row1 = dict_mess[0]
            row1 = {int(k):int(v) for k,v in row1.items()}
            row2 = dict_mess[1]
            row2= {int(k):int(v) for k,v in row2.items()}
            row3 = dict_mess[2]
            row3 = {int(k):int(v) for k,v in row3.items()}
            print(row1)
            print("::;;::::::::::::::::::::::::::::")
            print(list_of_nums_to_highlight_rn)

            with open('tick_dicts.json') as f:
                datar = json.load(f)
            lnames = []
            for p in datar: 
                lnames.append(p)
            return render_template('something.html',list=list_of_nums_to_highlight_rn,row1=row1,row2=row2,row3=row3,lnames=lnames)
        except:
            return render_template('boar2.html', list=list_of_nums_to_highlight_rn, val="Invalid",wins=wons,num=len(list_of_nums_to_highlight_rn))  
    
    if 'TickPrice' and 'PrizeMon' and 'NumFulls' in request.form:
        with open('test.json','r') as f:
            data = json.load(f)
        
    elif 'Next' in request.form:
        try:
            list_of_nums_to_highlight_rn.append(list_of_numbers_to_highlighte_at_the_end[0])
            
            list_of_numbers_to_highlighte_at_the_end.pop(0)
            return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons,num=len(list_of_nums_to_highlight_rn),l2=cricket_lst)
        except:
            return render_template('boar.html', list=["ALL DONE!!!!"])
            list2 = list_of_nums_to_highlight_rn
            start()
    elif 'Back' in request.form:
        try:
            return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons,num=len(list_of_nums_to_highlight_rn)) 
        except:
            print("probl")
    elif 'Start' in request.form:
        return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons,num=len(list_of_nums_to_highlight_rn))
    elif 'Endgame' in request.form:
        dict_of_winer = {}
        with open('tick_dicts.json','r') as f:
            data = json.load(f)
        print(data)
        for name in data:
            lst = data[name]
            cost = len(lst[0]) * 2
            ## Cost
            lst.pop(0)
            mon = 0
            for i in lst:
                i = int(i)
                mon+= i 
            ## Mon

            net = mon - cost
            print(net)

            dict_of_winer.update({name:[cost,mon,net]})
        print(dict_of_winer)
            

        return render_template('end_game.html',dic = dict_of_winer)
        
    elif 'PrizeShwo' in request.form: 
        # with open('tick_dicts.json','r') as f: 
        #     data = json.load(f)
        # tick_no = len(data)
        # tick_price = request.form.get("TickPrice")
        # Fh = request.form.get("NumFulls")
        # mon_prize = request.form.get("PrizeMon")
        # x =0 
        # for i in range(Fh):
        #     x += i
        # step1 = (tick_no* tick_price) - x
        # num_prizes = step1 / mon_prize
        # print("NUGYTFRDESDTFYGUHIJOKPFGJNCFV BCVBJNCV BHJGYFTDREXFCGYUHJKM< NBVCFGDRTFY")
        # print(num_prizes)
        # # if is_instance(num_prizes, float) == True: 
        # # else: 
        #     # go thrugh the number that many times to finf it.   
        print("KKKKKKKKKNBVGFCGDSDFUHIJOKCFGVHBJU")  
        return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons,num=len(list_of_nums_to_highlight_rn))

    elif 'Won' in request.form:
        try:
            Mon = request.form.get("Money")
            last_Name  = request.form.get("LastName")
            print(last_Name)
            # with open("tick_dicts.json","r+") as f:
            #     data = json.load(f)
            #     # print(";;;;;;;;;;;;;;;;;;;;;;;;;;;; ")
            #     data[last_Name].append(Mon)
            #     json.dump(data,f)

            #     # obj = json.loads(data)
            #     # dict_mess = obj[last_Name]
            #     # print(dict_mess)
            #     # dict_mess.append(Mon)
            
            # return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons)
                
            with open('tick_dicts.json') as f:
                f.seek(0)
                data = json.load(f)
            data[last_Name].append(Mon)

            with open('tick_dicts.json','w') as f:
                json.dump(data,f)

            a = request.form.get("Fname")
            b = request.form.get("WonWhat")
            wons.update({b:a})
            with open('who_won.json', "w+") as f:
                json.dump(wons,f)
                
            return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons,num=len(list_of_nums_to_highlight_rn)) 
            
        # with open('test.json','r') as file:
        #     data=file.read()

        # obj = json.loads(data)
        except:
            return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="",wins=wons,num=len(list_of_nums_to_highlight_rn))


    return render_template('boar.html')

def Next_NUm():
    try:
        list_of_nums_to_highlight_rn.append(
        list_of_numbers_to_highlighte_at_the_end[0])
        list_of_numbers_to_highlighte_at_the_end.pop(0)
        return render_template('boar2.html', list=list_of_nums_to_highlight_rn,val="Please enter valid ticket number.",wins=wons,num=len(list_of_nums_to_highlight_rn))
    except:
        list2 = list_of_nums_to_highlight_rn
        start()

        return render_template('board.html', list=["ALL DONE!!"], list2=list2,maxi=maxi)
            # return render_template("board.html",Num1=Nu


