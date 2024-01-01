import requests
import csv
import time

# Your existing script logic here

# Run for a total of 10 minutes with updates every 1 minute
total_duration_minutes = 10
update_interval_seconds = 60
bot_token = os.environ.get("BOT_TOKEN")
chat_id= '-1002068146668 '
url = f'https://agile-cliffs-23967.herokuapp.com/ok'
#chat_id = response['result'][0]['message']['chat']['id']
#print(chat_id)
#print(response)
#print(message)

def monitor_req(url):
    response = requests.get(url).json()
    return response['resu']


def append_strings_to_csv(strings_to_check, csv_file_path):
    # Check if the array contains more than one element
    if len(strings_to_check) <= 1:
        print("Not enough strings to append. CSV file not updated.")
        return

    # Check each string and append to the CSV file until the one before the last
    with open(csv_file_path, mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")

        for string in strings_to_check[:-1]:
            if "|" in string:
                # Split the string into CSV fields using the pipe as the delimiter
                csv_fields = string.split("|")

                # Append the fields to the CSV file
                csv_writer.writerow(csv_fields)

    print(f"CSV file '{csv_file_path}' updated.")



csv_file_path = "output.csv"

def send_telegram(bot_token,chat_id,message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    if len(message) > 1:
        requests.get(url).json()


# Call the function
start_time = time.time()
while time.time() - start_time < total_duration_minutes * 60:
    # Your script logic here
    message = monitor_req(url)
    append_strings_to_csv(message, csv_file_path)
    send_telegram(bot_token,chat_id,message)
    time.sleep(update_interval_seconds)
