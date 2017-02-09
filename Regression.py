# Programming Regression Analysis
# Programmer: Anna Marlena
# March 22, 2015

# This program performs a regression analysis on a provided set of data. It graphs the scatterplot
# points and determines a regression line. It then draws lines from the plotted points to
# the regression line. 

# import the math and graphics modules
import math
from graphics import *

# open and read the data file
fileHandle = open('Regression.dat','r')
fileLines = fileHandle.readlines()

# program greeting
def greeting():
    print("Welcome to Marlena's regression analysis. This program will ")
    print('open the provided data file, plot the points within the file,')
    print('& graph a regression line as determined by a mathematical')
    print('regression analysis. It will then connect the plotted points')
    print('to the regression line.')

# main function which does the calculations
def regression():
    # create empty X and Y lists
    X = []
    Y = []

    # divide the data into the x and y lists
    for n in range(0,len(fileLines)):
        itemList = fileLines[n].split(',')
        X.append(float(itemList[0]))
        Y.append(float(itemList[1]))
    sumX = sum(X)
    sumY = sum(Y)

    # find the average values for X and Y in the lists
    avX = sumX / float(len(X))
    avY = sumY / float(len(Y))

    print('\nThe average value of X is: ',avX)
    print('\nThe average value of Y is: ',avY)

    # define numerator and denominator variables to hold the values of summed
    # up numerator and denominator.
    numerator = 0
    denominator = 0
    
    for n in range(0,len(X)):
        numer = ((X[n] - avX) * (Y[n] - avY))
        denom = ((X[n] - avX)**2)
        numerator += numer
        denominator += denom

    slope = numerator / denominator
    print('\nThe slope is: ',numerator,'/',denominator)
    print('\nOr as a decimal value, the slope is: ',slope)

    # find b, the intercept point of the regression line on the Y axis
    b = avY - (slope * avX)
    print('\nThe value of b is: ',b)

    # create lists for the standard deviations of the x and y values
    Ox = []
    Oy = []

    # calculate the standard deviations and append them to their lists
    for n in range(0,len(X)):
        countX = ((float(X[n] -  avX))**2 / len(X))
        Ox.append(countX)
        sumOx = sum(Ox)
        xdev = math.sqrt(sumOx)

    for n in range(0,len(Y)):
        countY = ((float(Y[n] -  avY))**2 / len(Y))
        Oy.append(countY)
        sumOy = sum(Oy)
        ydev = math.sqrt(sumOy)
        
        
    # do the calculation to find the coefficient of determination, R**2
    # first set the variables & empty lists, then proceed with the calculation
    calc = []

    for n in range(0,len(X)):
        calc1 = ((X[n] - avX) * (Y[n] - avY)) / (xdev * ydev)
        calc.append(calc1)

    calcSum = sum(calc)

    Rsq = ((1 / len(X)) * calcSum)**2
    print('\nThe value of R squared is:\n',Rsq)

    # now determine the first and last Y points by using the equation
    # Y = mX + b
    Y1 = (slope * 0) + b
    Y2 = (slope * 10) + b
   
    # open a window graph
    win = GraphWin("Regression Model", 550, 550, autoflush=True)

    # set window coordinates
    win.setCoords(-.33,-1,11,36)
    win.setBackground('black')

    # create a set of boundaries
    xp1 = Point(0,0)
    xp2 = Point(10.5,0)
    xaxis = Line(xp1,xp2)
    xaxis.setArrow('last')
    yp1 = Point(0,0)
    yp2 = Point(0,35)
    yaxis = Line(yp1,yp2)
    yaxis.setArrow('last')
    xaxis.setOutline('blue')
    yaxis.setOutline('blue')
    xaxis.setWidth(.2)
    yaxis.setWidth(.2)
    xaxis.draw(win)
    yaxis.draw(win)
        
    # mark points on the x and y axis for comprehension of scale
    origin = Text(Point(0,0), '0')
    origin.setOutline('white')
    origin.draw(win)
    xaxis1 = Text(Point(2,0), '2')
    xaxis1.setOutline('white')
    xaxis1.draw(win)
    xaxis2 = Text(Point(4,0), '4')
    xaxis2.setOutline('white')
    xaxis2.draw(win)
    xaxis3 = Text(Point(6,0), '6')
    xaxis3.setOutline('white')
    xaxis3.draw(win)
    xaxis4 = Text(Point(8,0), '8')
    xaxis4.setOutline('white')
    xaxis4.draw(win)
    xaxis5 = Text(Point(10,0), '10')
    xaxis5.setOutline('white')
    xaxis5.draw(win)
    yaxis1 = Text(Point(0,10),'10')
    yaxis1.setOutline('white')
    yaxis1.draw(win)
    yaxis2 = Text(Point(0,20),'20')
    yaxis2.setOutline('white')
    yaxis2.draw(win)
    yaxis3 = Text(Point(0,30),'30')
    yaxis3.setOutline('white')
    yaxis3.draw(win)

    # graph the scatterplot points
    for a in range(0,len(X)):
        p = Point(X[a],Y[a]) 
        c = Circle(p,0.2)
        c.setFill('green')
        c.draw(win)
        
    # graph the regression line using X values of 0 and 10, and Y values
    # as determined by the calculations above using slope, X values,
    # and Y-intercept points
    p1 = Point(0, Y1)
    p2 = Point(10,Y2)
    line = Line(p1,p2)
    line.setArrow('last')
    line.setWidth(.3)
    line.setOutline('yellow')
    line.draw(win)

    # create a list of points at the regression line
    regresspoints = []
    # run through a calculation to create this list
    for n in range(0,len(X)):
        P = ((slope * X[n]) + b)
        regresspoints.append(P)
        

    # draw lines from the scatterplot points to the regression line
    for n in range(len(X)):
        point1 = Point(X[n],Y[n]) # original plot point
        point2 = Point(X[n],(regresspoints[n]))  # point on the regression line
        tinyLine = Line(point1,point2)  # connect the points, and voila: little lines
        tinyLine.setWidth(.01)
        tinyLine.setOutline('purple')
        tinyLine.draw(win)  

    win.getMouse()
    win.close()

# call the program greeting and the regression function
greeting()

regression()


