import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV = os.getenv("ENV", "qa")

env_path = ROOT_DIR / "config" / f"{ENV}.env"

load_dotenv(dotenv_path=env_path)

class Config:
    BASE_URL = os.getenv("BASE_URL")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chromium")
    FIXED_OTP = os.getenv("FIXED_OTP")

    if not BASE_URL:
        raise ValueError(f"BASE_URL is missing. Env file not loaded from: {env_path}")
