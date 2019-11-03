#this code is more about logging then anything else. using logging is better
#and more informative then print ln
# logging levels debug, info, warning, error, critical (debug at lowest, Critical hightest)
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s')
'logging.disable(logging.CRITICAL)
logging.debug('start of program')

def factorial(n):
    logging.debug('Start of function(%s)' %(n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total) )
    logging.debug('Return value is %s' % (total))
    return total

print (factorial(5))

logging.debug('end of program')
