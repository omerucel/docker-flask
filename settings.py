import os
from dotenv import load_dotenv
load_dotenv()

TEMPLATES_AUTO_RELOAD = os.getenv('TEMPLATES_AUTO_RELOAD') == 'True'