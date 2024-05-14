import re

class PhoneValidator:
    def __init__(self):
        # Regular expression pattern for matching valid email addresses
        self.phone_pattern = re.compile(r'^(\(61\)|61)0\d{9}$')

    def validate_phone(self, phone):
        # Validate the given email address against the pattern
        return bool(self.phone_pattern.match(phone))

# Example usage:
validator = PhoneValidator()

class EmailValidator:
    def __init__(self):
        # Regular expression pattern for matching valid email addresses
        self.phone_pattern = re.compile(r'^[a-zA-Z]+(\.[a-zA-Z0-9]+)*@[a-zA-Z]+\.[a-zA-Z]+$')

    def validate_email(self, phone):
        # Validate the given email address against the pattern
        return bool(self.phone_pattern.match(phone))

# Example usage:
validator_phone = PhoneValidator()
validator_email = EmailValidator()


output = ""
email_details = {}

# Read email file and match email entries with property entries
# This part can be replaced with lib CSV to JSON
with open('sample_properties_email_phone.csv', mode="r", encoding="utf-8-sig") as emails:
    email_header = emails.readline().strip().split(',')
    index_propid_email = email_header.index('prop_id')
    index_email_email = email_header.index('email')
    index_phone_email = email_header.index('phone')
    for email in emails:
        email_detail = email.strip().split(',')
        email_id = email_detail[index_propid_email]
        email_email = email_detail[index_email_email]
        email_phone = email_detail[index_phone_email]
        email_details[email_id] = [email_email,email_phone]


with open('sample_properties.csv', mode="r", encoding="utf-8-sig") as props:
    prop_header = props.readline().strip().split(',')
    index_propid_prop = prop_header.index('prop_id')
    index_address_prop = prop_header.index('full_address')

    for prop in props:
        prop_detail = prop.strip().split(',')
        prop_prop_id = prop_detail[index_propid_prop]
        prop_address = prop_detail[index_address_prop]
        if prop_prop_id in email_details:
            if validator_email.validate_email(email_details[prop_prop_id][index_email_email]):
                output += f"{prop.strip()},{email_details[prop_prop_id][index_email_email]}\n"
            else:
                output += f"{prop.strip()},\n"            

# Add header
str_header = f"{prop_header[index_propid_prop]},{prop_header[index_address_prop]},email"
if len(output):
    output = str_header + "\n" + output.strip()
else:
    output = str_header
# return output
print(output.strip())