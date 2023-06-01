import re
import os

# Define regular expression pattern to match unwanted lines
unwanted_pattern = re.compile(r"^(.*)(Medya dahil edilmedi|Bu mesajı sildiniz|Bu mesaj silindi|Mesajlar ve aramalar uçtan uca şifrelidir|Bu kişiyi engellediniz)(.*)$", re.IGNORECASE)

# Define regular expression pattern to match emoji
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
# Open original file and new file

iban_pattern = re.compile(r"\b(?:TR|GR)\d{2}\s?(?:\d{4}\s?){5}\s?\d{2}\b")

# Create filtered folder if it does not exist
if not os.path.exists("filtered"):
    os.makedirs("filtered")

# Iterate over files in messages folder
for file_name in os.listdir("Whatsapp mesajları"):
    # Check if file is a text file
    if not file_name.endswith(".txt"):
        continue
    
    with open(os.path.join("Whatsapp mesajları", file_name), "r", encoding="utf-8") as original_file, open(os.path.join("filtered", file_name), "w", encoding="utf-8") as filtered_file:
    # Iterate over lines in original file
        for line in original_file:
            # If line matches unwanted pattern or contains ".vcf" extension, skip it
            if unwanted_pattern.match(line) or ".vcf" in line or url_pattern.search(line) or iban_pattern.search(line):
                continue

            
            # Remove emojis from line
            line = emoji_pattern.sub(r'', line)
            
            # If line is empty, skip it
            if line=="" or line==" ":
                continue
            
            
            # Otherwise, write line to filtered file
            if re.match(r'\d{2}.\d{2}.\d{4} \d{2}:\d{2} -', line):

                text=line.split(":")[2]

                # If line is empty, skip it
                if text =="" or text==" ":
                    continue
            
                filtered_file.write(line)
