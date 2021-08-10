import os
from instabot import Bot


def instagram_login(logger):
    logger.info('logging in instagram')

    ig_username = os.getenv('IG_USERNAME')
    ig_password = os.getenv('IG_PASSWORD')

    cookie_path = 'config/Fohoma_uuid_and_cookie.json'
    if os.path.exists(cookie_path):
        os.remove(cookie_path)

    bot = Bot()
    bot.login(username=ig_username, password=ig_password)

    return bot


def get_following(logger, bot, username):
    logger.info('getting following count')

    following = bot.get_user_following(username)

    return len(following)
