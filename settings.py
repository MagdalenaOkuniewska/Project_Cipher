from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.getenv('DEBUG', default=False)

print(DEBUG)