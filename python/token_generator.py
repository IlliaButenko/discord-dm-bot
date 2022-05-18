import requests
url = "https://discord.com/api/v9/invites/{}"
txt_file_name = "tokens.txt"
def list_tokens():
    tokens = []
    with open(txt_file_name) as file:
        account_list = file.readlines()
    for account in account_list:
        try:
            account = account.replace("\n","")
            token = account.split(":")[2]
            tokens.append(token)
        except:
            pass
    return tokens
def get_valid_tokens():
    valid_tokens = []
    tokens = list_tokens()
    with open('tokens.csv', 'w') as f:
        for token in tokens:
            f.write(token)
            f.write("\n")
    return valid_tokens

valid_tokens = get_valid_tokens()
print(valid_tokens)



