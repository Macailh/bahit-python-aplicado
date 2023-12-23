# Logging levels
# INFO, DEBUG, WARNING, ERROR, CRITICAL

# basicConfig class
# class used to initialize a record and set the level
from logging import basicConfig, INFO
basicConfig(
    filename="system_log_generation/programa.log",
    filemode="a",
    level=INFO,
    format="[%(asctime)s] [%(levelname)s] [pid %(process)d] MYAPP MyErrorLevel Alert: %(message)s"
)

# functions
# info(), debug(), warning(), error(), critical()

import logging

logging.info("Este es un mensaje de registro de nivel INFO")
logging.warning("Este es un mensaje de registro de nivel WARNING")
