from logger_setup import logger

class User:
    def __init__(self, repo):
        self.repo = repo

    def add_user(self, user_name, user_age):
        logger.info(f"Adding user ({user_name.title()})")
        if not user_name.strip():
            logger.warning("User name Can't be empty.")
            return False, "User name Can't be empty."
        if not user_age or user_age < 10 or user_age > 50:
            logger.warning("User age must be between in 10 to 50")
            return False, "User age must be between in 10 to 50"

        check_user = self.repo.get_user_by_name(user_name)
        if check_user:
            logger.warning("User already exists.")
            return False, "User already exists."
        self.repo.add_user(user_name, user_age)
        
        logger.info("User successfuly added.") 
        return True, "User successfuly added."
