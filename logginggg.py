import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='log.txt',format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')

def fact(n):
    total=1
    logging.debug('Start of factorial')
    for i in range(1,n+1):
        total *=i
        logging.debug('i is' +'  ' + str(i) + '   ' +'total is' +'   '+ str(total))
    logging.debug('End of factorial')
    return total


print(fact(5))
logging.debug('End of program')

#################Logging Modes #################

#logging.debug() --------------     lowest level,usually for small details,we care for this while diagnosing issues
#logging.info(msg) --------------    for getting general info in the program,used to check if things are working fine at that point of time
#logging.warning(msg) --------------  Used to indicate a potential issue that doesnt prevent program from working but might do so in future
#logging.critical(msg) --------------
#logging.basicConfig()--------------
        