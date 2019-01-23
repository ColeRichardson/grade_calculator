''' My first try Went over complicated trying to imply classes
class Course:

    Finds the current weigthed course mark (CGPA coming soon)
    Current weghted course mark and CGPA calculatlor

    #Course(course code, # of assesments, weight of current assesment,
    Examples:
    Course(Eco200, 2, 0.15, 'y')
    Eco200.average
    -> edit from new section below;
    Y = full year course = 1.0 credit
    H = half year course = 0.5 credit
    all in decimal for easier math
'''
ans = ''
print('Welcome to (InsertNameHere) to calculate your current weighted average please enter your information below')
ans = str(input('have you already entered grades for this course ? (y/n)'))
#while ans == 'n' :
    course_code = str(input('what is the course code? ex. ECO200Y' ))
    no_of_ass = int(input('what is the number of current assessments ?' ))
    while n < no_of_ass:
        grade = float(input('what is your grade on assignment ' + str(n))) + '?'
        weight = float(input('what is the weight of assignement' str(n) + '?'))

    '''
    Examples:
    >>> 
    
    '''

def average(course):
#using the course code given by the user above, we can search our file for the corresponding line in a text file.
    accessdata(course)

def writedata(course_code, ):
    my_file = file.data

def accessdata(course_code): -> list[course code, number of assesments, ass1=tuple(grade, weight), assN=...]

