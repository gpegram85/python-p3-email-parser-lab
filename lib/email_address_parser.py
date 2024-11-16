# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        split_emails = re.split(r"[,\s]+", self.text)
        valid_email_pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        valid_emails = []

        for email in split_emails:
            if re.match(valid_email_pattern, email):
                valid_emails.append(email)

        result = sorted(valid_emails)
        return result