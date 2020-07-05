#!/usr/bin/env python3

# A module for drawing a chart with the turtle
# import required modules
import turtle
import math
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

def read_file():
    """ 
    Manage file and title of the output window.
    
    Retrieve file path and read content of the file line-by-line. Set user-defined title for the output window and initialize turtle method.

    No arguments and return value.
    """

    # input file path into a variable
    file_path = input("Which file to visualize? Note: The file exist in data folder. Please enter filename without the path (Example: 'huskies2016.txt'): ")
    
    # input title for the bar chart
    chart_title = input("What should the chart be named? (Example: 'Chart 1'): ")
    
    # open and read data from the file
    f = open('data/' + file_path, mode='r')
    data = f.readlines()

    # function to draw the chart
    turtleinit(data, chart_title)


def count_observations(data):
    """
    Count the number of observations from input file.
    
    Initialize counter variable to 0 and increment for each line that is parsed from the input file. 
    Divide the counter variable by 3 to get the number of observations.

    Parameters:
    arg1(list): Input the list of all the lines read from the input file

    Returns:
    int: The count for the number of observations in the input file
    """

    count = 0

    # count the number of lines in the input file
    for line in data:
        count += 1

    # convert and return number of lines into number of observations
    return(int(count / 3))

def get_max_value(data, feature):
    """
    Determine the maxmimum value of first feature across observations.
    
    Initialize max variable to a small value and compare it with the data of first feature for different 
    set of observations while storing the result of the comparison into max variable
    

    Parameters:
    arg1(list): Input the list of all the lines read from the input file
    arg2(string): Input the list of features

    Returns:
    int: The maxmium value of the first feature across observations
    """

    # store the integer value of the required feature
    feature_index = int(feature[-1])
    
    # declare a variable to store maximum value of the first feature across the observations
    max = -100000

    # compare and retrieve the maximum value of the first feature across the observations
    for index, line in enumerate(data):
        if feature_index == 1 and index % 3 == 1:
            if int(line) > max:
                max = int(line)

    # return maximum value of the first feature
    return(max)

def draw_x_axis(pointer):
    """
    Draw x axis on the output window    

    Parameters:
    arg1(object): Turtle object

    Returns:
    No return value
    """

    # draw x axis
    pointer.forward(WINDOW_WIDTH - 120)

def draw_y_axis(pointer):
    """
    Draw y axis on the output window    

    Parameters:
    arg1(object): Turtle object

    Returns:
    No return value
    """

    pointer.home()

    # draw y axis
    pointer.left(90)
    pointer.forward(WINDOW_HEIGHT)

def draw_y_tick_mark(pointer, data):
    """
    Draw y axis ticks on the output window   

    Parameters:
    arg1(object): Turtle object
    arg2(list): Input the list of all the lines read from the input file

    Returns:
    No return value
    """

    pointer.home()
    pointer.left(90)

    # retrieve maximum value of first feature
    max_value = get_max_value(data, 'feature 1')
    
    # calculate the number of ticks on y axis
    y_max = math.ceil(max_value / 7)

    # plot ticks and numbers
    for y in range(y_max):
        pointer.forward(45)
        pointer.left(90)
        pointer.forward(5)
        pointer.penup()
        pointer.forward(40)
        pointer.pendown()
        pointer.write((y + 1) * 7, font = ("Arial", 7, "normal"))
        pointer.penup()
        pointer.left(180)
        pointer.forward(40)
        pointer.pendown()
        pointer.forward(5)
        pointer.left(90)

def draw_x_axis_label(pointer, data):
    """
    Draw x axis labels on the output window   

    Parameters:
    arg1(object): Turtle object
    arg2(list): Input the list of all the lines read from the input file

    Returns:
    No return value
    """

    pointer.home()

    # retrieve number of observations in input file
    data_count = count_observations(data)

    # print labels on x axis using input file
    for i in range(data_count):

        # retrieve labels from input file
        label_value = data[3 * i]

        # move point to the specific location to print labels
        pointer.forward(math.floor((WINDOW_WIDTH - 100) / data_count))
        pointer.right(90)
        pointer.penup()
        pointer.forward(40)
        pointer.pendown()

        # print labels on x axis
        pointer.write(label_value, font = ("Arial", 7, "normal"))
        pointer.penup()
        pointer.left(180)
        pointer.forward(40)
        pointer.right(90)
        pointer.pendown()
        
def choose_color():
    """
    Randomly generate colors

    Generate random RGB values in the range 0 to 255 that is used to color the bars of the bar chart   

    Parameters:
    No parameters

    Returns:
    tuple: returns a tuple with a set of three randomly generated number
    """

    # randomly create RGB values to create bar colors for each observation
    return(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
def draw_bars(pointer, data):
    """
    Draw the bars of the bar chart on the output window   

    Parameters:
    arg1(object): Turtle object
    arg2(list): Input the list of all the lines read from the input file

    Returns:
    No return value
    """

    pointer.home()

    # count number of observations from the input file
    num_of_obs = count_observations(data)
    step = 1

    # plot bar chart
    for i in range(num_of_obs):
        # retrieve random RGB values for chart bars
        color = choose_color()

        # draw bars in the bar plot for each feature value
        draw_rectangle(pointer, i * math.floor((WINDOW_WIDTH - 100) / num_of_obs) + 40, 0, 40, int(data[step]), color)
        step = step + 3
        
def draw_rectangle(pointer, px, py, width, height, pen_color):
    """
    Draw the rectangles on the output window   

    Parameters:
    arg1(object): Turtle object
    arg2(int): x coordinate of the rectangular position
    arg3(int): y coordinate of the rectangular position
    arg4(int): height of the rectangle
    arg5(int): width of the rectangle
    arg6(tuple): RGB values

    Returns:
    No return value
    """

    pointer.penup()
    pointer.home()

    # set position of bar
    pointer.setpos(px, py)
    pointer.pendown()

    # set the color of the pen
    pointer.color(pen_color)
    pointer.begin_fill()

    # draw a rectangle with the specified width and height
    for i in range(2):
        pointer.forward(width)
        pointer.left(90)
        pointer.forward(height * 7)
        pointer.left(90)

    pointer.end_fill()

def turtleinit(data, chart_title):
    """
    Create the screen and function call to develop the bar chart of the input data

    Parameters:
    arg1(object): Turtle object
    arg2(string): Title of the bar chart output window

    Returns:
    No return value
    """

    # initialize the output window
    window = turtle.Screen()

    # set the title of bar plot
    window.title(chart_title)

    # set the width and height of output window
    turtle.setup(width = WINDOW_WIDTH, height = WINDOW_HEIGHT, startx = 0, starty = 0)

    # set the default position of the turtle pointer to be the bottom left of the output window
    turtle.setworldcoordinates(-100, -100, WINDOW_WIDTH, WINDOW_HEIGHT)

    # set the color modes and speed of the turtle pointer
    turtle.colormode(255)
    turtle.speed(9)

    # create and initialize turtle object
    pointer = turtle.Turtle()

    # Function call to print bar plot on output window
    draw_x_axis(pointer)
    draw_y_axis(pointer)
    draw_y_tick_mark(pointer, data)
    draw_x_axis_label(pointer, data)
    draw_bars(pointer, data)
    window.mainloop()

def main():
    read_file()

if __name__ == "__main__":
    # execute only if run as a script
    main()