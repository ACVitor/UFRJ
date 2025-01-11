# Geometric Calculations

# 1 - Retangule Area
def r_area(l1,l2):
    '''This function calculate and return a retangule area'''
    return l1*l2

#Tests
# print(r_area(5,7), r_area(15,2), r_area(15,2), r_area(500,700),r_area(5,0))


# 2 - Superficial Cube area
def cube_area(c):
    '''This function calculates and return a superficial area of a cube with edge c'''
    return r_area(c,c) * 6

#Tests
# print(cube_area(2), cube_area(0), cube_area(-2))


# 3 - Ring area
def ring_area(r1,r2):
    '''Calculates area of a ring with the radius given by the user.
    r1 for the biggest radius and r2 for the smallest'''
    return 3.14*r1**2 - 3.14*r2**2

#Tests
# print(ring_area(2,1), ring_area(15,5), ring_area(100,0))


# Algebric calculations

# 4 - Average for 2 numbers (Media)
def average_2_numbers(n1,n2):
    '''Calculates average between two numbrs given by the user.'''
    return (n1+n2)/2

#Test
# print(average_2_numbers(-5,7), average_2_numbers(2,-2), average_2_numbers(5,5), average_2_numbers(3,4), average_2_numbers(3.0,4.0))

# 5 - ordinate of the 2 degree function
def y_function2(a,b,c,x):
    '''Calculate ordinate value of the 2 degree function'''
    return a*x**2 + b*x + c

#Test
# print(y_function2(1,1,1,1),y_function2(0,1,1,1),y_function2(0,0,1,1),y_function2(-1,1.5,-1,1),)


# 6 - Weighted Average for 2 numbers (Media ponderada)
def w_average(n1,p1,n2,p2):
    '''Calculate weighted average for 2 numbers
    Give:   n1 - number 1
            p1 - weight for number 1
            n2 - number 2
            p2 - weight for number 2
    Please, respect this order.'''
    return (n1*p1 + n2*p2)/(p1+p2)

#Test
# print(w_average(4.5,1,9.5,3),w_average(2,4,5,2),w_average(0,2,10,0),)


# 7 - erro of approximation PG
def erro_pg_approx(q,n):
    '''Calculate error of approximation between infinity and normal geometric progression
    Given:  q - ratio (razão), attention 0 <= q < 1
            n - number of first terms of the PG'''
    return (1/(1-q)) - ((1*(q**n)-1)/(q-1))

#Test
# print(erro_pg_approx(0.5,5),erro_pg_approx(0.5,10),erro_pg_approx(0.5,20),erro_pg_approx(0.5,50),erro_pg_approx(0,10))