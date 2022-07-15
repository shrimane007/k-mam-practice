#tracking file and program after run
# in searching for bug
# python logger-

# import logging
# logging.basicConfig(filename="log1.log",format='%(asctime)s %(message)s')
# logger=logging.getlogger()
# logger.setlevel(logging.DEBUG)

# str='www.google.com'
# logger.debug(str) 

import logging
logging.basicConfig(filename="log1.log",level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s',filemode='w')
                    
                    
# # logger=logging.getlogfile()
# # logger.setlevel(logging.DEBUG)

str='i am shri'
logging.warning(str)
logging.critical("ITS NG")

 
# try:
#     print(10/0)
# except Exception as e:
#     logging.exception(e)









































































