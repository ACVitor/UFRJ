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
    Give:   q - ratio (razão), attention 0 <= q < 1
            n - number of first terms of the PG'''
    return (1/(1-q)) - ((1*(q**n)-1)/(q-1))

#Test
# print(erro_pg_approx(0.5,5),erro_pg_approx(0.5,10),erro_pg_approx(0.5,20),erro_pg_approx(0.5,50),erro_pg_approx(0,10))


# Applied Calculations

# 8 - tip (gorjeta)
def tip_15(bill):
    '''Calculate the tip as a 15% of the bill.
    Give: bill -> bill value'''
    return bill*0.15

#Test
# print(tip_15(10.00),tip_15(50.00),tip_15(5.00),tip_15(0.00),tip_15(100.59))


# 9 - tip on legislation
def real_tip(bill,tip_percent):
    '''Calculate the tip based on legislation.
    Give:   bill -> bill value
            tip_percent (inform this in real format, like to 0.00, example: for 15% digit 0.15)'''
    return bill*tip_percent

#Test
# print(real_tip(10.00,0.15),real_tip(100,0.0),real_tip(5.00,0.50),real_tip(10,0.05))


# 10 - Bank Balance (Saldo)
def balance(initial_balance,juros,months):
    '''Calculate the current balance
    Give:   initial_balance
            juros (Is a month fees(juros), inform this in real format, like to 0.00)
            months'''
    return initial_balance*(1+juros*months)

#Test
# print(balance(15000,0.01,5))


# 11 - Boat and river current
def boat_hdist(boat_velocity,river_velocity,river_width):
    '''Calculate horizontal distance traveled by boat in function of the river current.
    Inform data in S.I.'''
    return river_width*(river_velocity/boat_velocity)

#Test
# print(boat_hdist(15,5,50))