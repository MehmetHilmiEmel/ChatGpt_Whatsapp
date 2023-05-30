import re
import json
import os
from datetime import datetime


folder_path = 'filtered'
files = os.listdir(folder_path)
message_objects = []

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

   
    messages_by_date = {}
    for line in lines:
        date_str = line.split(' ')[0]  # assume date is at beginning of line
        date = datetime.strptime(date_str, '%d.%m.%Y')
        if date not in messages_by_date:
            messages_by_date[date] = []
        messages_by_date[date].append(line.strip())  # strip off newline character at end of line
            
    for date, messages in messages_by_date.items():

        me_text = ""
        person_text = "" 
        for message in messages:

            if me_text=="" and person_text=="" and "Mehmet Hilmi Emel" in message.split(":")[1]:
                continue
            else:
                info = message.split(":")
                if "Mehmet Hilmi Emel" not in info[1]:
                    if me_text == "":
                        person_text += " " + info[2]
                    elif me_text!="" and person_text!="":
                        message_objects={
                            'prompt': f'{person_text}: ',
                            'completion': f'{me_text}'
                        }
                        with open('whatsapp_messages.json', 'a', encoding='utf-8') as jf:
                            json.dump(message_objects, jf, indent=4, ensure_ascii=False)
                            jf.write(",")

                            
                        person_text = ""
                        person_text += " " + info[2]
                        me_text = ""
                else:
                    me_text += " " + info[2]




# Read JSON file contents into a string variable
with open('whatsapp_messages.json', 'r') as f:
    json_string = f.read()

# Strip leading/trailing whitespace from the string
json_string = json_string.strip()

# Check if last character is a comma
if json_string[-1] == ',':
    # Remove the comma
    json_string = json_string[:-1]
    
json_string="["+json_string+"]"

# Convert the modified string back into a JSON object
json_object = json.loads(json_string)

# Write the JSON object back to the file
with open('Prepared.json', 'w') as f:
    json.dump(json_object, f, indent=4)