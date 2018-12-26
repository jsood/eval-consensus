import logging
import logging.handlers
import os

# create logger
logger = logging.getLogger('raftlogfile.csv')
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

filename = "raftlogfile.csv"
should_roll_over = os.path.isfile(filename)
handler = logging.handlers.RotatingFileHandler(filename, mode='w')
if should_roll_over:  # log already exists, roll over!
    handler.doRollover()

#file handler
fh = logging.FileHandler(filename)
#fh = logging.handlers.RotatingFileHandler(filename)
#if should_roll_over:  # log already exists, roll over!
#fh.doRollover()

# create formatter. TODO: might not even need a formatter
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(message)s')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
#logger.addHandler(ch)
logger.addHandler(fh)

if __name__=="__main__":
	# 'application' code
	logger.debug('debug message')
	logger.info('info message')
	logger.warn('warn message')
	logger.error('error message')
	logger.critical('critical message')
