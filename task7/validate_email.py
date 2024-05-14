import re

class EmailValidator:
    def __init__(self):
        # Regular expression pattern for matching valid email addresses
        self.email_pattern = re.compile(r'^\D*@+\D+\.[a-zA-Z]*$')

    def validate_email(self, email):
        # Validate the given email address against the pattern
        return bool(self.email_pattern.match(email))

# Example usage:
validator = EmailValidator()

# Test cases
emails = ["AlbertB@gmail.com", "Albert.C@123.com", "hello.world@student.monash.edu",
          "Albert.D@qq.com", "Albert.D@163.com"]

for email in emails:
    if validator.validate_email(email):
        print(f"{email} is a valid email address.")