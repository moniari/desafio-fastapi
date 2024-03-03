import logging
from datetime import datetime

def generate_log(error: bool, method: str, params: str, message: str):
    time_stamp = datetime.now().timestamp()

    logging.basicConfig(
        filename=f"logs/log-{time_stamp}.log",
        level= error if logging.INFO else logging.ERROR,
        format="%(asctime)s %(message)s"
    )

    logging.info("LOG START")
    error if logging.info("Operation failed") else logging.info("Operation completed successfully")
    logging.info(f"Method {method}")
    logging.info(f"Params used {params}")
    logging.info(f"Message {message}")
    logging.info("LOG FINISHED")
