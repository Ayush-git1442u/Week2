
from logging_config import logger


def login(username: str, password: str) -> bool:

    logger.info("Login process started")

    try:
        if not username or not password:
            logger.warning("Username or password is missing")
            return False

        if username == "ayush" and password == "1234":
            logger.info("User %s logged in successfully", username)
            return True

        logger.warning("Invalid login attempt for %s", username)
        return False

    except Exception:
        logger.exception("Unexpected error during login")
        return False


if __name__ == "__main__":
    login("ayush", "1234")
    login("rahul", "wrong")
    login("", "")
