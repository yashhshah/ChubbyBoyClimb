
#################################################################################
#GAME NAME: CHUBBY BOY CLIMB                                                    #
#GAME DEVELOPER/DESIGNER/EVERYTHING ELSE: YASH SHAH                             #
#GAME BASED OFF OF ME: FALSE                                                    #
#GAME MADE FOR: MR SCHATTMAN                                                    #
#IMAGES GOTTEN FROM: GOOGLE IMAGES THANK YOU GOOGLE                             #
#TIME YOU WASTED READING THIS: 10 SECONDS TO 1 HOUR DEPENDING ON READING SPEED  #                                                    
#################################################################################


#things to do:
#nothing left






#get the imports out of the way#
from tkinter import *
from random import *
from time import *
from math import *

#create the Canvas#
m=Tk()
s=Canvas(m,height=800,width=800,background="LightSkyBlue1")
homescreenclick=False
again=False


#define function for things needed during menu startup#
def setmenuvalues():
    global StartingImage,coin,grandma,snake,laser,chocolate
    StartingImage=PhotoImage(file="boystartpic.gif")
    coin=PhotoImage(file="coin3.gif")
    grandma=PhotoImage(file="madgrandma2.gif")
    snake=PhotoImage(file="snake2.gif")
    laser=PhotoImage(file="laserbase.gif")
    chocolate=PhotoImage(file="chocbar2.gif")
    

#function for the death screen#
def deathscreen():
    global again,button6,ff,qq,button7,deathtext
    deathtext=s.create_text(400,400,font="Arial 30 bold",fill="red",text="You died, better luck next time!")    
    button6 = Button(s, text = "PLAY AGAIN",font="Arial 30 bold",bg="orange",command =lambda:rungame())    
    button7 = Button(s, text = "HOME",font="Arial 30 bold",bg="orange",command =menuscreen)
    again=True
    ff=s.create_window(600, 750, window = button6,width=300)
    qq=s.create_window(100,750,window=button7,width=150)
    


#Set initial variables for the game#
def setinitialvalues():
    global ywalls2,ywall2s,gameend,ywall,ywall2,yLine,yLineend,yLine3,yLineend3,yLines,yLineends,yLine3s,yLineend3s,x,boyright,boyleft,keypress,manmovement,whichboy,jump,obStart,obStarty
    global obpic,cl,obStartLeft,whichdirection,obStartys,obstacles,n,q,pictures,chocolate,speed,gotoDistance,frames,obpics,grandma,rocketboy,rocketboyleft,coin
    global coincounter,originalspeed,yboy,laser,laser2,laserleft,laser3,laserstart,laserend,snake,x1w,y1ws,x2w,y2ws,win1,win2
    ywalls2=0
    ywall2s=800
    gameend=False
    ywall=0
    ywall2=800
    yLine=0
    yLineend=800
    yLine3=820
    yLineend3=820
    yLines=0
    yLineends=800
    yLine3s=820
    yLineend3s=820
    x=0
    boyright=0
    boyleft=0
    whichboy="right"
    manmovement=[PhotoImage(file="cr.gif"),PhotoImage(file="cl.gif")]
    again=False  
    keypress=False
    jump=0
    obStart=650
    obStartLeft=150
    obStarty=-400
    obpics=[]
    chocolate=PhotoImage(file="chocbar2.gif")
    grandma=PhotoImage(file="madgrandma2.gif")
    rocketboy=PhotoImage(file="rr.gif")
    rocketboyleft=PhotoImage(file="rl.gif")
    coin=PhotoImage(file="coin3.gif")
    laser=PhotoImage(file="laserbase.gif")
    laser2=PhotoImage(file="laser.gif")
    laserleft=PhotoImage(file="laserleft.gif")
    laser3=PhotoImage(file="laserbaseleft.gif")
    snake=PhotoImage(file="snake2.gif")
    obStartys=[]
    obstacles=[]
    cl=0.09
    n=200
    q=0
    getObStarty()  
    speed=30
    gotoDistance=True
    frames=0
    coincounter=0
    originalspeed=30
    yboy=650 
    whichdirection=[]
    whichobstacle()
    laserstart=[]
    laserend=[]
    x1w=330
    win1=[0,0,0]
    win2=[0,0,0]
    x2w=470    
    y1ws=[50,290,530]
    y2ws=[190,430,670]
    #===for loop for the 4 obstacles created on screen===#
    for i in range(4):
        obpic=choice([chocolate,grandma,coin,coin,laser,laser,laser,snake])
        laserstart.append(0)
        laserend.append(0)
        if whichdirection[i]=="left" and obpic==laser:
            obpic=laserleft
        if obpic==laser or obpic==laserleft:
            laserstartVal=randint(200,480)
            laserendVal=laserstartVal+randint(100,160)
            laserstart[i]=laserstartVal
            laserend[i]=(laserendVal)        
        obpics.append(obpic)
        
   

#create function for wall creation-Num1#
def wall1creation():
    global ywall,ywall2,yLine,yLineend,yLine3,yLineend3,vert,vert2   
    s.create_rectangle(500,ywall,800,ywall2,fill="firebrick3",outline="firebrick3")
    #create lines
    xLinestart=500
    yLinehori=20
    
    while xLinestart<=800:        
        if xLinestart<800:
            vert=s.create_line(xLinestart,yLine,xLinestart,yLineend,fill="yellow")
            vert2=s.create_line(xLinestart,yLine3,xLinestart,yLineend3,fill="yellow")
        else:
            vert=s.create_line(xLinestart,yLine,xLinestart,yLineend,fill="firebrick3")
            vert2=s.create_line(xLinestart,yLine3,xLinestart,yLineend3,fill="firebrick3")            
        xLinestart=xLinestart+20       
        
        while yLinehori<800:
            xLinehori=500
            xLinehoriend=800
            s.create_line(xLinehori,yLinehori,xLinehoriend,yLinehori,fill="yellow")
            yLinehori=yLinehori+20
    yLine=yLine+30
    yLineend=yLineend+30
    yLine3=yLine3+30
    yLineend3=yLineend3+30
    if yLine==30 or yLine3==30:
        if yLine==30:
            yLine3=-780
            yLineend3=20          
        else:
            yLine=-780
            yLineend=20
    s.pack()        
  
            

#create function for wall creation-Num2#
def wall2creation():
    global ywalls2,ywall2s,yLines,yLineends,yLine3s,yLineend3,yLineend3s,vert3,vert4,x1w,x2w,y1ws,y2ws,win1
     
    
    s.create_rectangle(0,ywalls2,300,ywall2s,fill="firebrick3",outline="firebrick3")
    #windows#
    for i in range(3):
        win1[i]=s.create_rectangle(x1w,y1ws[i],x2w,y2ws[i],fill="SteelBlue2",outline="DeepSkyBlue2",width=7)
        win2[i]=s.create_polygon(((x1w+x2w)/2),y2ws[i],(((x1w+x2w)/2)+5),y2ws[i]-10,x2w,y1ws[i],x2w,y2ws[i],fill="LightSKyBlue1")
        y1ws[i]=y1ws[i]+40
        y2ws[i]=y1ws[i]+140
        if y2ws[i]>820:
            y1ws[i]=-140
            y2ws[i]=y1ws[i]+140
            
        
           
   
    #create lines
    xLinestart2=0
    yLinehori2=20

    while xLinestart2<=300:
        if xLinestart2<300:
            vert3=s.create_line(xLinestart2,yLines,xLinestart2,yLineends,fill="yellow")
            vert4=s.create_line(xLinestart2,yLine3s,xLinestart2,yLineend3s,fill="yellow")
        else:
             vert3=s.create_line(xLinestart2,yLines,xLinestart2,yLineends,fill="firebrick3")
             vert4=s.create_line(xLinestart2,yLine3s,xLinestart2,yLineend3s,fill="firebrick3")
        xLinestart2=xLinestart2+20

        while yLinehori2<800:
            xLinehori2=0
            xLinehoriend2=300
            s.create_line(xLinehori2,yLinehori2,xLinehoriend2,yLinehori2,fill="yellow")
            yLinehori2=yLinehori2+20
    yLines=yLines+30
    yLineends=yLineends+30
    yLine3s=yLine3s+30
    yLineend3s=yLineend3s+30
    
    if yLines==30 or yLine3s==30:
        if yLines==30:
            yLine3s=-780
            yLineend3s=20          
        elif yLine3s==30:
            yLines=-780
            yLineends=20            
    s.pack()        
    

#create boy if hes on the left#
def boycreate():
    global x,boyright
    s.delete(boyleft)
    if gotoDistance==False:
        boyright=s.create_image(650,yboy,image=rocketboy)
    else:
        boyright=s.create_image(650,yboy,image=manmovement[x%len(manmovement)],anchor=N)       
    s.pack()   
    x=x+1


#create boy if hes on the right#
def boycreateleft():
    global x,boyleft
    s.delete(boyright)
    if gotoDistance==False:
        boyleft=s.create_image(150,yboy,image=rocketboyleft)
    else:
        boyleft=s.create_image(150,yboy,image=manmovement[x%len(manmovement)],anchor=N)   
    x=x+1
    s.pack()
    
    
#function for detecting key presses#
def keyPressDetector(event):
    global whichboy,keypress,yboy
    if event.keysym=="Left":       
        whichboy="left"        
    elif event.keysym=="Right":
        whichboy="right"    
    if event.keysym=="Up":
        yboy=yboy-30
    elif event.keysym=="Down" and yboy<=720:
        yboy=yboy+30
    


#draws which boy depending on key pressed#
def drawthecorrectboy():
    global whichboy,keypress
    if whichboy=="right":        
        s.delete(boyleft)
        boycreate()
    else:
        s.delete(boyright)       
        boycreateleft()
        

#draws the obstacles themselves#
def drawobstacle():
    global obStart,obStarty,obstacle,whichdirection,speed
    for xs in range(len(obStartys)):        
        if whichdirection[xs]=="right":
              if obpics[xs]==laser or obpics[xs]==laser2:
                  if laserstart[xs]<=obStartys[xs]<=laserend[xs]:
                      obpics[xs]=laser2                      
                  else:                     
                      obpics[xs]=laser
              if obStartys[xs]<=850:              
                obstacles[xs]=s.create_image(obStart,obStartys[xs],image=obpics[xs],anchor=S)
                obStartys[xs]=obStartys[xs]+speed            
              else:
                  if xs==0 and obStartys[3]<0:
                      obStartys[xs]=obStartys[3]-450
                  elif xs==1 and obStartys[0]<0:
                      obStartys[xs]=obStartys[0]-450
                  elif xs==2 and obStartys[1]<0:
                      obStartys[xs]=obStartys[1]-450
                  elif xs==3 and obStartys[2]<0:
                      obStartys[xs]=obStartys[2]-450                      
                  s.delete(obpics[xs])
                  whichdirection[xs]=choice(["left","right","left","left","right"])
                  obpics[xs]=choice([chocolate,grandma,coin,coin,coin,coin,grandma,snake,grandma,grandma,snake,laser,laser])
                  if whichdirection[xs]=="left" and obpics[xs]==laser:
                        obpics[xs]=laserleft
                  if obpics[xs]==laser or obpics[xs]==laserleft:
                    laserstartVal=randint(200,320)
                    laserendVal=laserstartVal+randint(100,250)
                    laserstart[xs]=laserstartVal
                    laserend[xs]=laserendVal         
                  
                  

        elif whichdirection[xs]=="left":
            if obpics[xs]==laser3 or obpics[xs]==laserleft:
                  if laserstart[xs]<=obStartys[xs]<=laserend[xs]:
                      obpics[xs]=laser3                    
                    
                  else:                     
                      obpics[xs]=laserleft
            if obStartys[xs]<=850:                
                obstacles[xs]=s.create_image(obStartLeft,obStartys[xs],image=obpics[xs],anchor=S)
                obStartys[xs]=obStartys[xs]+speed                
            else:              

                  if xs==0 and obStartys[3]<0:
                      obStartys[xs]=obStartys[3]-450
                  elif xs==1 and obStartys[0]<0:
                      obStartys[xs]=obStartys[0]-450
                  elif xs==2 and obStartys[1]<0:
                      obStartys[xs]=obStartys[1]-450
                  elif xs==3 and obStartys[2]<0:
                      obStartys[xs]=obStartys[2]-450
                  s.delete(obpics[xs])
                  whichdirection[xs]=choice(["left","right","right","right","left"])
                  obpics[xs]=choice([chocolate,grandma,coin,coin,coin,coin,grandma,grandma,snake,grandma,snake,laser,laser])
                  if whichdirection[xs]=="left" and obpics[xs]==laser:
                        obpics[xs]=laserleft
                  if obpics[xs]==laser or obpics[xs]==laserleft:
                    laserstartVal=randint(200,320)
                    laserendVal=laserstartVal+randint(100,250)
                    laserstart[xs]=laserstartVal
                    laserend[xs]=laserendVal                
    s.pack()   
    
    
#gets distance for the Obstacles#
def getDist( x1, y1, x2, y2 ):
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

#gets your score on screen#
def score():
    global x
    score=s.create_text(700,30,font="Arial 40 bold",text=coincounter)

#directions for the obstacles#
def whichobstacle():
    global direction,whichdirection,n,obstacles
    for m in range(4):
        direction=choice(["left","right","left","left","right"])
        whichdirection.append(direction) 
        obstacles.append(0)
        
   
#gets the random y values for the obstacles#       
def getObStarty():
    global n,obStarty,obStartys,q
    for i in range(4):
        obStarty=randint(q,n)
        obStarty=obStarty*-1        
        if i>=1:            
            while getDist(0,obStartys[i-1],0,obStarty)<450:         
                obStarty=randint(q,n)
        q=q+710
        n=n+900
        obStartys.append(obStarty)
    
    
   
#gets the distance between obstacles to see if the game ended#
def distofobstacle():
        global whichdirection,gameend,speed,gotoDistance,frames,textbu,coincounter,originalspeed
        #for the chocolate rocket#
        if gotoDistance==False:
            if frames<=12:
                speed=130            
                frames=frames+1
                for i in range(len(whichdirection)):
                    disttime1=85
                    disttime2=162
                    if whichboy==whichdirection[i]:                    
                        if whichboy=="right":               
                            dist=getDist(650,yboy,obStart,obStartys[i])                       
                        
                        else:
                            dist=getDist(150,yboy,obStartLeft,obStartys[i])

                        if obpics[i]==coin:                            
                            if obStartys[i]<650:                        
                                if dist<=disttime1:
                                    coincounter=coincounter+1
                                    if i==0 and obStartys[3]<0:
                                      obStartys[i]=obStartys[3]-500
                                    elif i==1 and obStartys[0]<0:
                                      obStartys[i]=obStartys[0]-500
                                    elif i==2 and obStartys[1]<0:
                                      obStartys[i]=obStartys[1]-500
                                    elif i==3 and obStartys[2]<0:
                                      obStartys[i]=obStartys[2]-500
                  
                                    s.delete(obpics[i])
                                    whichdirection[i]=choice(["left","right","left","left","right"])
                                    obpics[i]=choice([chocolate,grandma,coin,coin,coin,coin,grandma,grandma,laser,laser,snake])
                                    if whichdirection[i]=="left" and obpics[i]==laser:
                                        obpics[i]=laserleft
                                    if obpics[i]==laser or obpics[i]==laserleft:
                                        laserstartVal=randint(200,320)
                                        laserendVal=laserstartVal+randint(100,250)
                                        laserstart[i]=laserstartVal
                                        laserend[i]=laserendVal
                                    
                
                            else:                           
                        
                                if dist<=disttime2:
                                    coincounter=coincounter+1
                                    if i==0 and obStartys[3]<0:
                                      obStartys[i]=obStartys[3]-500
                                    elif i==1 and obStartys[0]<0:
                                      obStartys[i]=obStartys[0]-500
                                    elif i==2 and obStartys[1]<0:
                                      obStartys[i]=obStartys[1]-500
                                    elif i==3 and obStartys[2]<0:
                                      obStartys[i]=obStartys[2]-500
                  
                                    s.delete(obpics[i])
                                    whichdirection[i]=choice(["left","right","left","left","right"])
                                    obpics[i]=choice([chocolate,grandma,coin,coin,coin,coin,grandma,snake,laser,laser])
                                    if whichdirection[i]=="left" and obpics[i]==laser:
                                        
                                        obpics[i]=laserleft
                                    if obpics[i]==laser or obpics[i]==laserleft:
                                        laserstartVal=randint(200,320)
                                        laserendVal=laserstartVal+randint(100,250)
                                        laserstart[i]=laserstartVal
                                        laserend[i]=laserendVal



            else:
                frames=0
                speed=originalspeed
                
                gotoDistance=True
            
        else:        
            for i in range(len(whichdirection)):
                if obpics[i]==chocolate or obpics[i]==coin or obpics[i]==laser or obpics[i]==laserleft or obpics[i]==laser2 or obpics[i]==laser3 or obpics[i]==snake:
                    disttime1=0
                    disttime2=300
                elif obpics[i]==grandma:
                    disttime1=0
                    disttime2=450
                if whichboy==whichdirection[i]:                    
                    if whichboy=="right":               
                        dist=getDist(650,yboy,obStart,obStartys[i])                       
                    else:                        
                        dist=getDist(150,yboy,obStartLeft,obStartys[i])                   
                    
                    if obStartys[i]<=yboy:#different distances based on if the obstacle is above or below the character#                           
                       
                        if dist<=disttime1:
                            if obpics[i]==chocolate:
                                gotoDistance=False
                            elif obpics[i]==coin:
                                    coincounter=coincounter+1
                                    if i==0 and obStartys[3]<0:
                                      obStartys[i]=obStartys[3]-500
                                    elif i==1 and obStartys[0]<0:
                                      obStartys[i]=obStartys[0]-500
                                    elif i==2 and obStartys[1]<0:
                                      obStartys[i]=obStartys[1]-500
                                    elif i==3 and obStartys[2]<0:
                                      obStartys[i]=obStartys[2]-500
                      
                                    s.delete(obpics[i])
                                    whichdirection[i]=choice(["left","right","left","left","right"])
                                    obpics[i]=choice([chocolate,grandma,coin,coin,coin,coin,grandma,snake])
                                    if whichdirection[i]=="left" and obpics[i]==laser:
                                        obpics[i]=laserleft
                                    if obpics[i]==laser or obpics[i]==laserleft:
                                        laserstartVal=randint(200,320)
                                        laserendVal=laserstartVal+randint(100,250)
                                        laserstart[i]=laserstartVal
                                        laserend[i]=laserendVal
                                   
                                
                                

                            else:
                                if obpics[i]==laser3 or obpics[i]==laser2:
                                    if laserstart[i]-200<=yboy<=laserend[i]:
                                         gameend=True
                                         
                                         
                                else:
                                    if obpics[i]==grandma or obpics[i]==snake or obpics[i]==laserleft or obpics[i]==laser:
                                         gameend=True
                                         
                                        

                                
                                
                                

                    else:#if the obstacle has a greater y value than the character#        
                            
                        
                            if dist<=disttime2:
                                 if obpics[i]==chocolate:
                                    gotoDistance=False
                                 elif obpics[i]==coin:
                                    coincounter=coincounter+1
                                    if i==0 and obStartys[3]<0:
                                      obStartys[i]=obStartys[3]-450
                                    elif i==1 and obStartys[0]<0:
                                      obStartys[i]=obStartys[0]-450
                                    elif i==2 and obStartys[1]<0:
                                      obStartys[i]=obStartys[1]-450
                                    elif i==3 and obStartys[2]<0:
                                      obStartys[i]=obStartys[2]-450              
                                    s.delete(obpics[i])
                                    whichdirection[i]=choice(["left","right","left","left","right"])
                                    obpics[i]=choice([chocolate,grandma,coin,coin,coin,coin,grandma,grandma])
                                    if whichdirection[i]=="left" and obpics[i]==laser:
                                        obpics[i]=laserleft
                                    if obpics[i]==laser or obpics[i]==laserleft:
                                        laserstartVal=randint(200,320)
                                        laserendVal=laserstartVal+randint(100,250)
                                        laserstart[i]=laserstartVal
                                        laserend[i]=laserendVal
                                   
                                    
                                   
                                 else:                            
                                    if obpics[i]==laser3 or obpics[i]==laser2:
                                        if laserstart[i]-200<=yboy<=laserend[i]:
                                            gameend=True
                                            
                                           
                                    else:
                                        if obpics[i]==grandma or obpics[i]==snake or obpics[i]==laserleft or obpics[i]==laser:
                                            gameend=True
                                            
                                            
                                    
                                    

                                    

                else:
                   if obpics[i]==laser3 or obpics[i]==laser2:
                                    if laserstart[i]-200<=yboy<=laserend[i]:
                                        gameend=True
                                        
                                        
                                    else:
                                       if obpics[i]==grandma:
                                        gameend=True
                                        
                                        
    
    

#==================================The run game ====================================#
def rungame():
    global gameend,cl,n,speed,button,l,originalspeed
    s.delete(ALL)
    if again==True:
        button6.destroy()
        button7.destroy()
    setinitialvalues()    
    s.delete(button,l,button2,x,image,hometext)
    button2.destroy()
    while gameend==False:       
        wall1creation()
        wall2creation()
        score()        
        drawthecorrectboy()       
        drawobstacle()        
        distofobstacle()               
        sleep(cl)
        s.update()        
        s.delete(vert,vert2,vert3,vert4,score)
        for l in range(len(obstacles)):
            s.delete(obstacles[l])
        if coincounter%3==0 and coincounter>0:
           speed=speed+5          
           originalspeed=speed           
           if cl<=0:
               cl=0
        for d in range(len(win1)):
            s.delete(win1[d],win2[d])        
        s.pack()
    else:
        sleep(1.5)
        s.delete(ALL)
        deathscreen()


#the main menu screen that appears on startup#
def menuscreen():
    global button,l,textb,x,button2,a,image,hometext,homescreenclick,line1,button0  
    if homescreenclick==True:
        button3.destroy()
        button4.destroy()
        s.delete(instructionstitle,line1,line2,line3,line4,coin,pic1,pic2,pic3,pic4,line2c)
    if again==True:
        button6.destroy()
        button7.destroy()
        s.delete(deathtext)        
    setmenuvalues()
    image = s.create_image(400,300,image=StartingImage)
    hometext=s.create_text(400,50,font="Arial 35 bold",text="CHUBBY BOY CLIMB")    
    button2=Button(s,text="HELP",font="Arial 30 bold",bg="yellow",command=instructions)
    button = Button(s, text = "PLAY",font="Arial 30 bold",bg="red",command =rungame)
    button0 = Button(s, text = "QUIT",font="Arial 30 bold",bg="red",command=lambda:m.destroy())

    #Use 'screen.create_window() to place the widget on the screen    
    l=s.create_window(400, 560, window = button,width=800)
    x=s.create_window(400,660,window=button2,width=800)
    b=s.create_window(400,760,window=button0,width=800)
    s.update()

#instruction pg 2#
def obstaclepage():
    global button4,q,line1,line2,line2c,line3,instructionstitle,pic1,pic2,pic3,pic4
    s.delete(ALL)
    button4 = Button(s, text = "HOME",font="Arial 30 bold",bg="orange",command =menuscreen)
    q=s.create_window(100,750,window=button4,width=150)
    instructionstitle=s.create_text(400,100,font="Arial 25 bold",text="WELCOME TO CHUBBY BOY CLIMB!")    
    line1=s.create_text(10,180,font="ComicSans 15 ",text="MAD GRANDMAS and SNAKES-Chubby boy is scared to 'death' of them. Stay away!",anchor=NW)
    line2=s.create_text(10,260,font="ComicSans 15 ",text="LASERS: Lasers will turn on at random times. Their beams are hard to see, watch out!",anchor=NW)
    line2c=s.create_text(10,340,font="ComicSans 15 ",text="When you die it might seem you didnt hit the lasers, but you did!",anchor=NW)
    line3=s.create_text(10,430,font="ComicSans 15 ",text="CHOCOLATES: These are your friends, get them for invunerability for a certain time.",anchor=NW)
    pic1=s.create_image(70,600,image=grandma)
    pic2=s.create_image(250,600,image=laser)
    pic3=s.create_image(500,600,image=chocolate)
    
    pic4=s.create_image(700,600,image=snake)

#instruction pg 1#    
def instructions():
    global x,button2,button,l,hometext,button3,f,homescreenclick,instructionstitle,line1,line2,line3,button4,f,coinpic,coin,line4,pic1,pic2,pic3,pic4,line2c
    s.delete(button,l,button2,x,hometext,image)
    button2.destroy()
    button0.destroy()    
    instructionstitle=s.create_text(400,100,font="Arial 25 bold",text="WELCOME TO CHUBBY BOY CLIMB!")
    line1=s.create_text(10,250,font="ComicSans 15 ",text="- Use the arrow keys to control Chubby Boy",anchor=NW)
    line2=s.create_text(10,350,font="ComicSans 15 ",text="- Help him climb walls and collect coins.",anchor=NW)
    line3=s.create_text(10,450,font="ComicSans 15",text="Collecting coins might make random enemies/coins/chocolates appear! Stay aware!",anchor=NW)
    coinpic=s.create_image(400,350,image=coin)
    line4=s.create_text(10,550,font="ComicSans 15 ",text="- Watch out for different obstacles, each one is explained on the next page:",anchor=NW)
    button3 = Button(s, text = "NEXT",font="Arial 30 bold",bg="orange",command =obstaclepage)
    button4 = Button(s, text = "HOME",font="Arial 30 bold",bg="orange",command =menuscreen)
    f=s.create_window(700, 750, window = button3,width=150)
    q=s.create_window(100,750,window=button4,width=150)
    homescreenclick=True
    pic1=0
    pic2=0
    pic3=0
    pic4=0
    line2c=0
                         
    

                  
   
    

      

    
    

#calls to begin the game#       
m.after(0, menuscreen)
s.bind( "<Key>", keyPressDetector)

s.pack()
s.focus_set()
m.mainloop()
