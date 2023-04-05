import json
import random
import argparse
from datetime import datetime

filename = 'Config.json'
current_datetime = datetime.now()

with open(filename, 'r') as file:
    config = json.load(file)


def current_rate():
    print(config['rate'])
    with open('Log_file', 'a') as logs:
        logs.write(f'Request {current_datetime}: current rate output - {config["rate"]}\n')
    return None


def wallet_balance():
    print(f"{config['balance_uah']} UAH\n{config['balance_usd']} USD")
    with open('Log_file', 'a') as logs:
        logs.write(f"Request {current_datetime}: current wallet balance - {config['balance_uah']} UAH;"
                   f" {config['balance_usd']} USD\n")
    return None


def buy_usd(amount):
    uah = amount * float(config['rate'])
    if uah > float(config['balance_uah']):
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {config['balance_uah']} "
              f"TO BUY MAXIMUM {round(config['balance_uah'] / config['rate'], 2)} USD")
    else:
        with open('Config.json', 'w') as file:
            config['balance_usd'] = round(float(config['balance_usd']) + amount, 2)
            config['balance_uah'] = round(float(config['balance_uah']) - uah, 2)
            json.dump(config, file)
    with open('Log_file', 'a') as logs:
        logs.write(f"Request {current_datetime}: buy {amount} USD\n")
    return None

# buy_usd(5)

def sell_usd(amount):
    uah = amount * float(config['rate'])
    if amount > float(config['balance_usd']):
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {config['balance_usd']} "
              f"TO BUY MAXIMUM {round(config['balance_usd'] / config['rate'], 2)} USD")
    else:
        with open('Config.json', 'w') as file:
            config['balance_usd'] = round(float(config['balance_usd']) - amount, 2)
            config['balance_uah'] = round(float(config['balance_uah']) + uah, 2)
            json.dump(config, file)
    with open('Log_file', 'a') as logs:
        logs.write(f"Request {current_datetime}: sell {amount} USD\n")
    return None

# sell_usd(4)


def buy_maximum_usd():
    if config['balance_uah'] == 0:
        print("There no money to spend")
    usd_max = float(config['balance_uah']) / float(config['rate'])
    with open('Log_file', 'a') as logs:
        logs.write(f"Request {current_datetime}: buy USD for {config['balance_uah']} UAH\n")
    with open('Config.json', 'w') as file:
        config['balance_usd'] = round(float(config['balance_usd']) + usd_max, 2)
        config['balance_uah'] = 0
        json.dump(config, file)
    return None

# buy_maximum_usd()


def sell_maximum_usd():
    if config['balance_usd'] == 0:
        print("There no money to spend")
    usd_max = float(config['balance_usd']) * float(config['rate'])
    with open('Log_file', 'a') as logs:
        logs.write(f"Request {current_datetime}: sell {config['balance_usd']} USD\n")
    with open('Config.json', 'w') as file:
        config['balance_usd'] = 0
        config['balance_uah'] = round(float(config['balance_uah']) + usd_max, 2)
        json.dump(config, file)
    return None

# sell_maximum_usd()

def new_rate():
    result = round(random.uniform(config['rate'] - config['delta'], config['rate'] + config['delta'] + 0.01), 2)
    with open('Config.json', 'w') as file:
        config['rate'] = result
        json.dump(config, file)
    with open('Log_file', 'a') as logs:
        logs.write(f"Request {current_datetime}: new currency rate - {config['rate']}\n")
    return None

# new_rate()

def restart():
    with open('default.txt', 'r') as res:
        _ = json.load(res)
    with open('Config.json', 'w') as res:
        json.dump(_, res)
    with open('Log_file', 'a') as logs:
        logs.write(f"Request: restart the program with the default values\n")
        print("System was restarted")
    return None

# restart()


def cleaner():
    with open('Log_file', 'w') as logs:
        logs.write('')
    print("Log file was cleaned")
    return None

# cleaner()


parser = argparse.ArgumentParser(description='Currency exchange.')

parser.add_argument("--rate", help="Display the current exchange rate", action='store_true')
parser.add_argument('--available', help="Display the current cash flow", action='store_true')
parser.add_argument('--buy', help="Buy xxx amount of USD", type=float, default=0)
parser.add_argument('--sell', help="Sell xxx amount of USD", type=float, default=0)
parser.add_argument('--buy_all', help="Buy all USD you can", action='store_true')
parser.add_argument('--sell_all', help="Sell all USD you have", action='store_true')
parser.add_argument("--next", help="Change the current exchange rate", action='store_true')
parser.add_argument('--restart', help="Start the program with the default values", action='store_true')
parser.add_argument('--system_clear', help="Clears the system log", action='store_true')


args = parser.parse_args()

if args.rate:
    current_rate()
elif args.next:
    new_rate()
elif args.available:
    wallet_balance()
elif args.buy:
    buy_usd(args.buy)
elif args.sell:
    sell_usd(args.sell)
elif args.buy_all:
    buy_maximum_usd()
elif args.sell_all:
    sell_maximum_usd()
elif args.restart:
    restart()
elif args.system_clear:
    cleaner()
