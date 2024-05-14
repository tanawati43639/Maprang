import re

class RegexHandler:

    def __init__(self) -> None:
        self.email_pattern = re.compile(r'^\D*@+\D+\.[a-zA-Z]*$')
        self.phone_pattern = re.compile(r'^(\(61\)|61)0\d{9}$')

    def validate_email(self, str2check: str) -> bool:
        return bool(self.email_pattern.match(str2check))
    
    def validate_phone(self, str2check: str) -> bool:
        return bool(self.phone_pattern.match(str2check))

def prop_email_matcher(prop_fpath: str, email_fpath: str) -> str:
    with open(prop_fpath, 'r', encoding='utf-8-sig') as props_file:
        props_lines = [line.rstrip('\n') for line in props_file]
        props_lines_spt = props_lines[0].split(',')
        index_props_prop_id = props_lines_spt.index('prop_id')
        index_props_full_address = props_lines_spt.index('full_address')
    with open(email_fpath, 'r', encoding='utf-8-sig') as phone_email_file:
        phone_email_lines = [line.rstrip('\n') for line in phone_email_file]
        index_phone_email_prop_id = phone_email_lines[0].split(',').index('prop_id')
        index_phone_email_email = phone_email_lines[0].split(',').index('email')

    props_valide_email = []
    # Create Header depend on index in file
    # Add Header Row in first. When the data is empty, it still show header
    props_valide_email.append(props_lines_spt[index_props_prop_id] + ',' + props_lines_spt[index_props_full_address] + ',' + 'email')
    for props_line in props_lines[1:]:
        for phone_email_line in phone_email_lines[1:]:
            if props_line.split(',')[index_props_prop_id].strip() == phone_email_line.split(',')[index_phone_email_prop_id].strip():
                email = phone_email_line.split(',')[index_phone_email_email]
                if RegexHandler().validate_email(email):
                    props_valide_email.append(props_line + ',' + email)
                else:
                    props_valide_email.append(props_line + ',')

    return '\n'.join(props_valide_email)

def prop_phone_matcher(prop_fpath: str, phone_fpath: str) -> str:
    with open(prop_fpath, 'r', encoding='utf-8-sig') as props_file:
        props_lines = [line.rstrip('\n') for line in props_file]
        props_lines_spt = props_lines[0].split(',')
        index_props_prop_id = props_lines_spt.index('prop_id')
        index_props_full_address = props_lines_spt.index('full_address')
    with open(phone_fpath, 'r', encoding='utf-8-sig') as phone_email_file:
        phone_email_lines = [line.rstrip('\n') for line in phone_email_file]
        index_phone_email_prop_id = phone_email_lines[0].split(',').index('prop_id')
        index_phone_email_phone = phone_email_lines[0].split(',').index('phone')

    props_valide_phone = []
    props_valide_phone.append(props_lines_spt[index_props_prop_id] + ',' + props_lines_spt[index_props_full_address] + ',' + 'phone')
    for props_line in props_lines[1:]:
        for phone_email_line in phone_email_lines[1:]:
            if props_line.split(',')[index_props_prop_id].strip() == phone_email_line.split(',')[index_phone_email_prop_id].strip():
                phone = phone_email_line.split(',')[index_phone_email_phone]
                if RegexHandler().validate_phone(phone):
                    props_valide_phone.append(props_line + ',' + phone)
                else:
                    props_valide_phone.append(props_line + ',')

    return '\n'.join(props_valide_phone)

def merge_prop_email_phone(prop_fpath: str, email_phone_fpath: str) -> str:
    with open(prop_fpath, 'r', encoding='utf-8-sig') as props_file:
        props_lines = [line.rstrip('\n') for line in props_file]
        props_lines_spt = props_lines[0].split(',')
        index_props_prop_id = props_lines_spt.index('prop_id')
        index_props_full_address = props_lines_spt.index('full_address')
    with open(email_phone_fpath, 'r', encoding='utf-8-sig') as phone_email_file:
        phone_email_lines = [line.rstrip('\n') for line in phone_email_file]
        index_phone_email_prop_id = phone_email_lines[0].split(',').index('prop_id')
        index_phone_email_email = phone_email_lines[0].split(',').index('email')
        index_phone_email_phone = phone_email_lines[0].split(',').index('phone')

    props_valide_email_phone = []
    props_valide_email_phone.append(props_lines_spt[index_props_prop_id] + ',' + props_lines_spt[index_props_full_address] + ',' + 'email' + ',' + 'phone')
    for props_line in props_lines[1:]:
        for phone_email_line in phone_email_lines[1:]:
            if props_line.split(',')[index_props_prop_id].strip() == phone_email_line.split(',')[index_phone_email_prop_id].strip():
                email = phone_email_line.split(',')[index_phone_email_email]
                phone = phone_email_line.split(',')[index_phone_email_phone]
                if RegexHandler().validate_email(email) or RegexHandler().validate_phone(phone):
                    if RegexHandler().validate_email(email):
                        temp_text = props_line + ',' + email
                    if not RegexHandler().validate_email(email):
                        temp_text = props_line + ','
                    if RegexHandler().validate_phone(phone):
                        temp_text = temp_text + ',' + phone
                    if not RegexHandler().validate_phone(phone):
                        temp_text = temp_text + ','
                    props_valide_email_phone.append(temp_text)
                    temp_text = ''

    return '\n'.join(props_valide_email_phone)
    
if __name__ == "__main__":
    print("Task 1 results: ")
    print(prop_email_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 2 results: ")
    print(prop_phone_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 3 results: ")
    print(merge_prop_email_phone("sample_properties.csv", "sample_properties_email_phone.csv"))

