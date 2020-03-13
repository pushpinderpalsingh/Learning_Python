from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv("Password")
print(password)