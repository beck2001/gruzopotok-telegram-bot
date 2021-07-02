import logging

# formatting logging for debugging of application
logging.basicConfig(format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s",
                    level=logging.INFO)
