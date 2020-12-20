import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.exception('Exception occurred')
    logging.error('Or you can do like that too', exc_info=True)
