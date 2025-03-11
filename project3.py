

def namer (name):
    return ("Hello %s" % name )




def elecunit (units):

    if units <= 50: 
        bill = units * 0.50
        surcharge = bill * 0.20
        final_bill = bill + bill * 0.20
        print ("Total electricity bill = Rs. %s" % final_bill)
    
    elif units <= 150:
        bill = 50 * 0.50 + 100 * 0.75
        surcharge = bill * 0.20
        final_bill = bill + bill * 0.20
        print ("Total electricity bill = Rs. %s" % final_bill)
    
    elif units <= 250:
        bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20
        surcharge = bill * 0.20
        final_bill = bill + bill * 0.20
        print ("Total electricity bill = Rs. %s" % final_bill)

    else:
        surcharge = bill * 0.20
        final_bill = bill + bill * 0.20
        bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
        print ("Total electricity bill = Rs. %s" % final_bill)

elecunit (200)




def salarycalc (salary):

     if salary <= 10000:
         print ("HRA = 20%, DA = 80%")

     elif salary <= 20000:
         print ("HRA = 25%, DA = 90%")

     else:
         print ("HRA = 30%, DA = 95%")

salarycalc (30000)



