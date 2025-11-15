import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import redis
from validate_email import validate_email

# Load environment variables from a .env file
load_dotenv()

# Validate and load sensitive configuration from environment variables
class SecureConfig:
    def __init__(self):
        self.redis_host = self.get_env_var('REDIS_HOST', 'Redis host URL must be set.')
        self.redis_port = self.get_env_var('REDIS_PORT', 'Redis port must be set.')
        self.database_url = self.get_env_var('DATABASE_URL', 'Database URL must be set.')
        self.geoip_service = self.get_env_var('GEOIP_SERVICE', 'GeoIP service must be set.')
        self.encryption_key = self.get_env_var('ENCRYPTION_KEY', 'Encryption key must be set.')
        self.security_level = self.get_env_var('SECURITY_LEVEL', 'Security level must be set.')
        self.rate_limit = self.get_env_var('RATE_LIMIT', 'Rate limit must be set.')

        self.validate_settings()

    def get_env_var(self, var_name, error_message):
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(error_message)
        return value

    def validate_settings(self):
        if not validate_email(os.getenv('ADMIN_EMAIL', '')):
            raise ValueError('Invalid admin email address.')

        # Additional validation checks can be added as needed.
    
    def get_redis_client(self):
        return redis.Redis(host=self.redis_host, port=self.redis_port)

# Instantiate the SecureConfig class
config = SecureConfig()