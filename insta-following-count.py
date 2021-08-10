import os

import utils
import instagram_utils
import email_utils

from dotenv import load_dotenv
load_dotenv()


# get logger
logger = utils.get_logger()
logger.info('insta-following-count started')

ig_username = os.getenv('IG_USERNAME')
ig_bot = instagram_utils.instagram_login(logger)

desired_following = int(os.getenv('DESIRED_FOLLOWING'))
actual_following = instagram_utils.get_following(logger, ig_bot, ig_username)

ifc_email_sent = os.getenv('IFC_EMAIL_SENT') == '1'
lang = os.getenv('LAN')

logger.info(f'desired following: {desired_following} | actual following: {actual_following}')

if desired_following != actual_following and not ifc_email_sent:
    email_utils.send_email(logger, desired_following, actual_following, lang)
else:
    os.environ['IFC_EMAIL_SENT'] = '0'

utils.write_env_file(logger)
