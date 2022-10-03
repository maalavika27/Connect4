import turtle
import time
import pickle
import winsound
import mysql.connector as sql

#Screen setting
t=turtle.Turtle()

def buttonsound():
	winsound.PlaySound('Buttonlightsound.wav',winsound.SND_ASYNC)

def errormsg():
    turtle.setpos(-600,10)
    turtle.color('red')
    turtle.ht()
    turtle.speed(0)
    turtle.write('CHECK YOUR INPUT!', align="left", font=("Calibri", 20))
    winsound.PlaySound('Buttonsound.wav',winsound.SND_ASYNC)
    time.sleep(2)
    turtle.undo()
        

def inputval(l,m,val):  #l,m are messages and val are values accepted
	while True:
		var=turtle.textinput(l,m)
		if var in val:
			return var
		else:
			errormsg()

screen=turtle.Screen()
screen.setup(width=1350,height=700,startx=0,starty=0)
screen.title('Connect 4')

winsound.PlaySound('Song (mp3cut.net).wav',winsound.SND_ASYNC)

ts=t.getscreen()
ts.bgcolor('black')

t.ht()
t.color('red')
t.speed(10)
t.pensize(5)

#Showing Connect 4
t.pu()
t.setpos(-250,200)
t.pd()
t.lt(180)
t.fd(10)
t.circle(50,90)
t.fd(30)
t.circle(50,90)
t.fd(10)

t.pu()
t.setpos(-225,150)
t.rt(90)
t.pd()
t.fd(30)
t.circle(50,180)
t.fd(30)
t.circle(50,180)

t.pu()
t.setpos(-100,70)
t.rt(180)
t.pd()
t.fd(130)
t.rt(150)
t.fd(150)
t.lt(150)
t.fd(130)

t.pu()
t.setpos(-25,70)
t.pd()
t.fd(130)
t.rt(150)
t.fd(150)
t.lt(150)
t.fd(130)

t.pu()
t.setpos(90,200)
t.lt(90)
t.pd()
t.fd(30)
t.lt(90)
t.fd(130)
t.lt(90)
t.fd(30)
t.pu()
t.setpos(60,115)
t.pd()
t.fd(30)

t.pu()
t.setpos(160,200)
t.rt(180)
t.pd()
t.fd(10)
t.circle(50,90)
t.fd(30)
t.circle(50,90)
t.fd(10)

t.pu()
t.setpos(250,200)
t.pd()
t.rt(180)
t.fd(60)
t.pu()
t.setpos(220,200)
t.pd()
t.lt(90)
t.fd(130)

t.color('blue')
t.pu()
t.setpos(0,65)
t.rt(30)
t.pd()
t.fd(86)
t.lt(120)
t.fd(86)
t.pu()
t.setpos(0,65)
t.rt(90)
t.pd()
t.fd(130)
t.pu()
t.lt(90)

time.sleep(2)
t.clear()

while True:
	
	
	while True:
		t.setpos(0,10)
		t.color('yellow')

		#Asking login
		t.write('''        			MULTIPLAYER
		
		Please enter the Player names in the box. One name in one box. 
		
		NOTE: If you already have played, your score gets added to your account provided you enter
		the same name. Or else, a new name is created for you.''', align="center", font=("Calibri", 20))

		name1= turtle.textinput('PLAYER 1','Enter Name').upper()#To reduce chances of duplication, all input characters are made in upper case 
		buttonsound()
		name2= turtle.textinput('PLAYER 2','Enter Name').upper()
		buttonsound()
		t.clear()

		t.setpos(0,-70)
		t.color('red')

		t.write('''		RULES :

		1. There are 8 columns in the grid. Each numbered 0 to 7 from the left.
		2. To put a coin in a column, enter the column number.
		3. Player 1 plays first and player 2 plays second.
		4. If you get 4 in a row, diagonally, vertically or horizontally, then you win!
		5. If you want to quit the current game at any time, enter 'q' in the column box. 

		SO ARE YOU READY TO PLAY? :)

		To continue, press ENTER''', align='center', font=('Calibri',20))

		x=turtle.textinput('To continue','Press enter')
		buttonsound()

		while True:
			valuesallowed=['0','1','2','3','4','5','6','7','q']
			t.clear()

			t.lt(90)   

			
			t.rt(90)
			t.color('blue')
			t.setpos(-300,-300)

			#Drawing grid
			x=-300
			t.speed(0)
			for i in range(10):
				t.pd()
				t.fd(600)
				t.pu()
				t.setpos(-300,x)
				x+=75
			t.pu()
			t.lt(90)

			x=-300
			for i in range(10):
				t.pd()
				t.fd(600)
				t.pu()
				t.setpos(x,-300)
				x+=75

			y=305
			x=-262
			for i in range(0,8):
				t.pu()
				t.setpos(x,y)
				t.pd()
				t.color('red')
				t.write(i,align='center',font=('Calibri',20))     #Writing numbers on top of grid
				x+=75

			#Creating the coordinate points in the grid
			t.pu()
			pd={}
			#rows numbered down to up 0 to 7 (column,row)
			p=[(i,j) for i in range(8) for j in range(8)]

			coord=[-262,-185,-110,-35,35,110,185,262]

			#Making dictionary pd with match of each box as none
			for i in p:
				pd[i]='none'

			ctr=1
			while 1:
				if ctr%2==0:
					color='red'
					name=name2
				else:
					color='green'
					name=name1

				m=inputval('Column no',name,tuple(valuesallowed))		#Asking what column for each member; datatype=string
				buttonsound()

				if m=='q':
					break
				
				c=int(m)	#c is the column no to be entered in integer

				rlist=[]	
				n=len(p)
				for i in range(0,n):
					if p[i][0]==c:		#If column=c,
						rlist+=[p[i][1]]
						break	#create list of all rows in p with column=c; if last iteration a (c,r) is called,
						#then that wont be in p (coz next line (c,r) is deleted and thus wont be added. so min of this list gives bottom most row 
				else:
					valuesallowed.remove(str(c))
					errormsg()
					continue

				r=min(rlist)
				t.setpos(coord[c],coord[r])
				t.dot(50,color)

				p.remove((c,r))		#that (c,r) deleted

				pd[(c,r)]=name		#in dictionary, this point is marked with name of player
				t.setpos(350,100)

				randomct=0

				if 'none' not in pd.values():		#if all the boxes are filled (to check)
					t.setpos(430,40)
					t.write('IT IS A TIE!',align='center',font=('Calibri',20))
					randomct+=1
					winner='tie'
					time.sleep(3)
					break


				for i in range(0,8):		#Finding winner if 4 in a row combination true by checking if the different ones dont have value none
					for j in range(0,8):

						if (i,j+1) in pd and (i,j+2) in pd and (i,j+3) in pd and \
						(i,j) in pd and \
						pd[(i,j+1)]==pd[(i,j+2)]==pd[(i,j+3)]==pd[(i,j)]!='none':

							winner=str(pd[(i,j)])
							t.write(winner,align='center',font=('Calibri',20))
							t.setpos(430,40)
							t.write('''      	has won!
	Congratulations!''',align='center',font=('Calibri',20))
							randomct+=1
							time.sleep(3)
							break

						elif (i+1,j) in pd and (i+2,j) in pd and \
						(i+3,j) in pd and (i,j) in pd and\
						pd[(i+1,j)]==pd[(i+2,j)]==pd[(i+3,j)]==pd[(i,j)]!='none':

							winner=str(pd[(i,j)])
							t.write(winner,align='center',font=('Calibri',20))
							t.setpos(430,40)
							t.write('''    	   	has won!
	Congratulations!''',align='center',font=('Calibri',20))
							randomct+=1
							time.sleep(3)
							break

						elif (i+1,j+1) in pd and (i+2,j+2) in pd and \
						(i+3,j+3) in pd and (i,j) in pd and\
						pd[(i+1,j+1)]==pd[(i+2,j+2)]==pd[(i+3,j+3)]==pd[(i,j)]!='none':

							winner=str(pd[(i,j)])
							t.write(winner,align='center',font=('Calibri',20))
							t.setpos(430,40)
							t.write('''      	has won!
	Congratulations!''',align='center',font=('Calibri',20))
							randomct+=1
							time.sleep(3)
							break

						elif (i,j) in pd and (i+1,j-1) in pd and \
						(i+2,j-2) in pd and (i+3,j-3) in pd and\
						pd[(i,j)]==pd[(i+1,j-1)]==pd[(i+2,j-2)]==pd[(i+3,j-3)]!='none':

							winner=str(pd[(i,j)])
							t.write(winner,align='center',font=('Calibri',20))
							t.setpos(430,40)
							t.write('''       	has won!
	Congratulations!''',align='center',font=('Calibri',20))
							randomct+=1
							time.sleep(3)
							break
						
						else:
							continue

					if randomct==1:
						break
				if randomct==1:
					break
				ctr+=1

			if m!='q':  #only if they havent planned to quit the game, that is entering q in column hasnt been done
				if winner!='tie':
					mycon=sql.connect(host='localhost',passwd='mysql',user='root',database='class12')
					cursor=mycon.cursor()

					cursor.execute("select name from connect4;")
					namestuple=cursor.fetchall()
					namesplayed=[]
					for i in namestuple:
						s=''
						for j in i:
							s+=j
						namesplayed+=[s.upper()]
					for i in name1,name2:
						if i in namesplayed:
							cursor.execute("update connect4 set totalgames=totalgames+1 where name='"+i+"';")
						else:
							cursor.execute("insert into connect4 values('"+i+"',1,0,0);")

					if name1==winner:
						cursor.execute("update connect4 set won=won+1 where name='"+name1+"';")
					else:
						cursor.execute("update connect4 set won=won+1 where name='"+name2+"';")

					cursor.execute("select totalgames,won from connect4 where name='"+name1+"';")
					data=cursor.fetchone()
					rname1=data[1]/data[0]
					cursor.execute("select totalgames,won from connect4 where name='"+name2+"';")
					data=cursor.fetchone()
					rname2=data[1]/data[0]

					cursor.execute("update connect4 set ratio="+str(rname1)+" where name='"+name1+"';")
					cursor.execute("update connect4 set ratio="+str(rname2)+" where name='"+name2+"';")
					mycon.commit()
					mycon.close()


					f=open(r'C:\Users\csmaa\Desktop\CS Project\multiconnect4.dat','rb') #assuming it has already been created
					players={}
					try:
						while True:
							players.update(pickle.load(f))
					except:
						f.close()
					for i in players:
						if name1 in i and name2 in i:
							score=list(players[i])

							del players[i]

							if i[0]==winner:
								score[0]+=1
							elif i[1]==winner:
								score[1]+=1

							players[i]=tuple(score)
							break

					else: #In case dict is empty or if name not found
						if name1==winner:
							players[(name1,name2)]=(1,0)
						elif name2==winner:
							players[(name1,name2)]=(0,1)
					#each time w is done so only one pickle done everytime
					g=open(r'C:\Users\csmaa\Desktop\CS Project\multiconnect4.dat','wb')
					pickle.dump(players,g)
					g.close()

				t.clear()
				t.setpos(0,0)
				t.color('pink')
				f=open(r'C:\Users\csmaa\Desktop\CS Project\multiconnect4.dat','rb') #assuming it has already been created
				players={}
				try:
					while True:
						players.update(pickle.load(f))
				except:
					f.close()

				for i in players:
					if name1 in i and name2 in i:
						if i[0]==name1:
							name1score=players[i][0]
							name2score=players[i][1]
						elif i[1]==name1:
							name1score=players[i][1]
							name2score=players[i][0]
					#case of no entry cannot be present since addwinner() has already been done before this
				#Output of SCORE BOARD
				output='''SCORE BOARD\n
Total games: 	'''+str(name1score+name2score)+'''
Won by '''+name1+''':	'''+str(name1score)+'''
Won by '''+name2+''':	'''+str(name2score)
				t.write(output,align="center", font=("Calibri", 25))
				time.sleep(5)
				
			mycon=sql.connect(host='localhost',passwd='mysql',user='root',database='class12')
			cursor=mycon.cursor()
			cursor.execute("select * from connect4 order by ratio desc,totalgames desc")
			alldata=cursor.fetchall()
			mycon.close()

			p1=str(alldata[0][0])
			p2=str(alldata[1][0])
			p3=str(alldata[2][0])
			r1=str(alldata[0][2])+'/'+str(alldata[0][1])
			r2=str(alldata[1][2])+'/'+str(alldata[1][1])
			r3=str(alldata[2][2])+'/'+str(alldata[2][1])

			t.clear()
			t.setpos(0,10)
			t.color('Orange')
			t.write('''LEADERBOARD\n
Name - Win Ratio\n
1 - '''+p1+'''  ('''+r1+''')
2 - '''+p2+'''  ('''+r2+''')
3 - '''+p3+'''  ('''+r3+''')''',align="center", font=("Calibri",20))
			time.sleep(7)

			t.clear()
			t.setpos(0,10)
			t.color('red')
			t.write('''Type in the Textbox\n
1. Play again with the same person
2. Play with a different person
3. Quit''', align="center", font=("Calibri", 20))

			userchoice=inputval('Your Choice','1,2 or 3?',('1','2','3'))
			buttonsound()

			t.clear()
			t.rt(90) #to make grid back to normal alignment
			if userchoice=='2':
				break
			elif userchoice=='3':
				break
		if userchoice=='3':
			break
	if userchoice=='3':
		break
turtle.bye()