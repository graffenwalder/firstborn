import matplotlib.pyplot as plt
import requests
import datetime

'''
Dear Hackers, government agencies and other criminals
You are probarbly in the midst of planning an invasion,
to rob me of my Bitcoins
However i've used Satoshi's BTC address in this script
I'm sorry for any inconvenience caused
'''

btc_address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'

#ToDoList:
#Started with 371 lines
#cmctop is a complete mess, check if vars are neccesary in for loop.  maybe start over
#try and make stampcheck functions


#Done:
#make 2 empty lines function lol
#finbook put vars out of for loop - deleted them
#Maybe combine the stamp_price() and stamp_eur_price() and ask for userinput (not to many markets on bitstamp)
#same can be done for the stampbook and stampprice functions
#Check stamp_history() and stamp_hist_eur(), vars in for loop might be unnecesary
#Give some extra info to stamp_price() and stamp_eur_price(), like volume daily change etc...
#maybe make a sub menu for bitfinex and bitstamp, although combining functions would reduce the number of options already
#Do i want to clear screen after running a function or, do i want to be able see? ---- NO
#make menu for fin_info() options
#have to make a while loop with valid tickers or a try/except error catch for fin_info() user input
#Do the same for fin_eur() and all bitstamp functions
#stampmenu()

# I like to start and end my printouts with 2 empty lines, so this function saves some lines
def empty_lines(x=2):
	lines = '\n' * x
	print(lines)

# Calls CoinMarketCap's API and gives global crypto statisttics
def cmcglobal():
	r = requests.get('https://api.coinmarketcap.com/v2/global/?convert=EUR')
	data = r.json()["data"]
	ts = data["last_updated"]

	empty_lines()
	print("CoinMarketCap Global Data:")
	empty_lines()
	print(f'	Active Crypto\'s:	{data["active_cryptocurrencies"]}')
	print(f'	Active Markets: 	{data["active_markets"]}')
	print(f'	Bitcoin Dominance: 	{data["bitcoin_percentage_of_market_cap"]}%')
	print("")
	print("	USD:")
	print(f'	Total MarketCap: 	$ {data["quotes"]["USD"]["total_market_cap"]/1000000000} billion')
	print(f'	Total Volume 24h: 	$ {data["quotes"]["USD"]["total_volume_24h"]/1000000000} billion')
	print("")
	print("	EUR:")
	print(f'	Total MarketCap: 	€ {data["quotes"]["EUR"]["total_market_cap"]/1000000000} billion')
	print(f'	Total Volume 24h: 	€ {data["quotes"]["EUR"]["total_volume_24h"]/1000000000} billion')
	print("")
	print(f"Last update: {datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')}")
	print("")

# Calls for CMC API for top25, could throw in userinput to change the number of crypto's in the list.
# Have to clean up the else if statement, real mess now
def cmctop():
	r = requests.get('https://api.coinmarketcap.com/v2/ticker/?limit=25&structure=array')
	x = 0
	data2 = r.json()["data"]
	ts = data2[0]["last_updated"]

	empty_lines()
	print("CoinMarketCap Top25:")
	empty_lines()

	print("rank/name		price		change	volume				market cap")
	for items in data2:
		data = r.json()["data"][x]
		rank = data["rank"]
		name = data["name"]
		price = data["quotes"]["USD"]["price"]
		change = data["quotes"]["USD"]["percent_change_24h"]
		volume = data["quotes"]["USD"]["volume_24h"]/1000000
		mcap = data["quotes"]["USD"]["market_cap"]/1000000000

		if len(name) < 5 and rank < 10 and len(str(price)) >= 13:
			print(f'{rank}. {name}			$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) < 4 and rank > 9 and len(str(price)) >= 13:
			print(f'{rank}. {name}			$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) > 11 and rank > 9 and len(str(price)) >= 13:
			print(f'{rank}. {name}	$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) < 5 and rank < 10 and len(str(price)) < 6:
			print(f'{rank}. {name}			$ {price} 	{change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) < 4 and rank > 9 and len(str(price)) < 6:
			print(f'{rank}. {name}			$ {price} 	{change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) > 11 and rank > 9 and len(str(price)) < 6:
			print(f'{rank}. {name}	$ {price} 	{change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) < 5 and rank < 10:
			print(f'{rank}. {name}			$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) < 4 and rank > 9:
			print(f'{rank}. {name}			$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(name) > 11 and rank > 9:
			print(f'{rank}. {name}	$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		elif len(str(price)) < 6:
			print(f'{rank}. {name}		$ {price} 	{change}% 	$ {volume} million 	$ {mcap} billion')
		else:
			print(f'{rank}. {name}		$ {price} {change}% 	$ {volume} million 	$ {mcap} billion')
		x += 1

	print("")
	print(f"Last update: {datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')}")
	empty_lines()


# Call Bitfinex API, for last 30 trades, negative trades are sells
def fin_history():
	r = requests.get('https://api.bitfinex.com/v2/trades/tBTCUSD/hist')
	outcome = r.json()[:30]

	empty_lines()

	for trades in outcome:
		price = trades[3]
		amount = trades[2]
		if amount >= 0:
			if len(str(amount)) <= 3:
				print(f"Bought	{amount} BTC		| $ {price}")
			else:
				print(f"Bought	{amount} BTC	| $ {price}")
		else:
			if len(str(amount)) <= 3:
				print(f"Bought	{amount} BTC		| $ {price}")
			else:
				print(f"Sold	{amount} BTC	| $ {price}")

	empty_lines()


# Call Bitfinex API, for current BTCUSD orderbook
def fin_book():

	r = requests.get('https://api.bitfinex.com/v2/book/tBTCUSD/P0')
	outcome = r.json()

	print("Bitfinex Orderbook:")
	print("")
	print("Asks:")
#orders[0]= price, orders[1] = ordercount, orders[2] = amount
	for orders in outcome:
		if orders[2] >= 0:
			if len(str(orders[2])) < 3:
				print(f"{orders[2]} BTC			${orders[0]}	 {orders[1]} orders")
			elif len(str(orders[2])) > 10:
				print(f"{orders[2]} BTC 	${orders[0]}	 {orders[1]} orders")
			else:
				print(f"{orders[2]} BTC 		${orders[0]}	 {orders[1]} orders")
	print("")
	print("Bids:")

	for orders in outcome:
		if orders[2] < 0:
			if len(str(orders[2])) < 3:
				print(f"{orders[2]} BTC			${orders[0]}	 {orders[1]} orders")
			elif len(str(orders[2])) > 10:
				print(f"{orders[2]} BTC 	${orders[0]}	 {orders[1]} orders")
			else:
				print(f"{orders[2]} BTC 		${orders[0]}	 {orders[1]} orders")
	empty_lines()

#Calls Bitfinex API, and ask the user for a crypto ticker and a market
def fin_info():
	def print_fin_info():
		empty_lines()
		print("-" * 15 + " Bitfinex popular Markets " + "-" * 19)
		print("USD:		BTC:		ETH:		EUR/GBP/JPY:")
		print("")
		print("BTC		ETH		IOT		BTC")
		print("ETH		BCH		ESS		ETH")
		print("EOS		ZEC		EOS		EOS")
		print("BCH		XRP		POY		IOT")
		print("XRP		EOS		BCH		NEO")
		print("ETC		DSH		XLM		XLM")
		print("LTC		XRM		ELF		XVG")
		print("ZEC		LTC		ETP")
		print("IOT		ETC		NEO")
		print("NEO		IOT		ZRX")
		print("-" * 60)
		empty_lines()

	print_fin_info()
	print("Choose Bitfinex ticker: btc, eth, zrx, neo, eth......... ")
	user = str.upper(input(' Insert ticker: '))
	print("Choose Bitfinex market: usd, eur, jpy, btc, eth......... ")
	user2 = str.upper(input(' Insert market: '))

	r = requests.get(f'https://api.bitfinex.com/v2/tickers?symbols=t{user}{user2}')

	try:
		p = r.json()[0]
	except IndexError:
		empty_lines()
		print("Market probarbly doesn't exist, please try again")
		empty_lines()
	else:
		# p[0]   SYMBOL,
		# p[1]   BID,
		# p[2]   BID_SIZE,
		# p[3]   ASK,
		# p[4]   ASK_SIZE,
		# p[5]   DAILY_CHANGE,
		# p[6]   DAILY_CHANGE_PERC,
		# p[7]   LAST_PRICE,
		# p[8]   VOLUME,
		# p[9]   HIGH,
		# p[10]   LOW
		# The price in BTC on line 154 is not from the actual crypto's BTC market.
		# it's calculated from the crypto's USD market and divided by the BTC/USD rate

		empty_lines()
		print(f"Bitfinex {user}/{user2} Info:")
		empty_lines()
		print(f"Last {user} price: {p[7]:.8f} {user2}.")
		print("")
		print(f"Highest buy order: {p[1]:.8f} {user2}")
		print(f"Lowest sell order: {p[3]:.8f} {user2}")
		print(f"Spread: {(float(p[3]) - float(p[1])):.8f} {user2}")
		print("")
		print(f"Daily change: {p[5]:.8f} {user2}")
		print(f"Daily percentage change: {(p[6] * 100):.2f} %")
		print("")
		print(f"Daily high: {p[9]:.8f} {user2}")
		print(f"Daily low: {p[10]:.8f} {user2}")
		print(f"Daily volume: {p[8]:.2f} {user} / {p[8] * p[7]:.2f} {user2}")
		empty_lines()

def stamp_menu():
	print("1. BTC/USD      6.  XRP/BTC      11. ETH/EUR")
	print("2. BTC/EUR      7.  LTC/USD      12. ETH/BTC")
	print("3. EUR/USD      8.  LTC/EUR      13. BCH/USD")
	print("4. XRP/USD      9.  LTC/BTC      14. BCH/EUR")
	print("5. XRP/EUR      10. ETH/USD      15. BCH/BTC")
	print("0. Exit")
	print("-" * 44)
	empty_lines()

#Calls bitstamp API, and returns last 20 trades for the selected market by userinput
def stamp_history():
	def print_stamp_history():
		empty_lines()
		print("-" * 15 + " Bitstamp Trade History " + "-" * 5)
		stamp_menu()

	print_stamp_history()
	userinput = 0
	while userinput not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		try:
			userinput = int(input('Please choose a number: '))
			if userinput == 0:
				empty_lines()
				break
		except ValueError:
			print("Please choose a valid number")
			continue

	if userinput in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		choice = stamp_options[userinput].upper()
		r = requests.get(f'https://www.bitstamp.net/api/v2/transactions/{choice.lower()}/')
		outcome = r.json()[0:20]

		empty_lines()

		for trades in outcome:
			price = trades['price']
			bought = trades['type']
			amount = trades['amount']

			if bought == '0':
				if len(amount) <= 11:
					print(f"Bought 	{amount} {choice[:3]}		|	{price} {choice[3:]}")
				else:
					print(f"Bought 	{amount} {choice[:3]}	|	{price} {choice[3:]}")
			else:
				if len(amount) <= 11:
					print(f"Sold   	{amount} {choice[:3]}		|	{price} {choice[3:]}")
				else:
					print(f"Sold   	{amount} {choice[:3]}	|	{price} {choice[3:]}")
		empty_lines()

#Calls bitstamp API, and returns orderbook for the selected market by userinput
def stamp_book():
	def print_stamp_orderbook():
		empty_lines()
		print("-" * 15 + " Bitstamp Orderbook " + "-" * 9)
		stamp_menu()

	print_stamp_orderbook()
	userinput = 0
	while userinput not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		try:
			userinput = int(input('Please choose a number: '))
			if userinput == 0:
				break
		except ValueError:
			print("Please choose a valid number")
			continue

	if userinput in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		choice = stamp_options[userinput].upper()
		r = requests.get(f'https://www.bitstamp.net/api/v2/order_book/{choice.lower()}/')
		bookBid = (r.json()['bids'][:10])
		bookAsk = (r.json()['asks'][:10])

		print(f"Bitstamp {choice[:3]}/{choice[3:]} Orderbook:")
		print("")
		print("Bids:                                  Asks:\n")
		for bid, ask in zip(bookBid, bookAsk):
			if len(str(bid[1])) > 13:
				print(f"{bid[0]} {choice[3:]} | {bid[1]} {choice[:3]}	{ask[0]} {choice[3:]} | {ask[1]} {choice[:3]}")
			elif len(str(bid[1])) <= 9:
				print(f"{bid[0]} {choice[3:]} | {bid[1]} {choice[:3]}			{ask[0]} {choice[3:]} | {ask[1]} {choice[:3]}")
			else:
				print(f"{bid[0]} {choice[3:]} | {bid[1]} {choice[:3]}		{ask[0]} {choice[3:]} | {ask[1]} {choice[:3]}")
	empty_lines()

#Calls bitstamp API, and returns market selected by userinput
def stamp_info():
	def print_stamp_info():
		empty_lines()
		print("-" * 15 + " Bitstamp Price " + "-" * 13)
		stamp_menu()

	print_stamp_info()
	userinput = 0
	while userinput not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		try:
			userinput = int(input('Please choose a number: '))
			if userinput == 0:
				empty_lines()
				break
		except ValueError:
			print("Please choose a valid number")
			continue


	if userinput in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		choice = stamp_options[userinput].upper()
		r = requests.get(f'https://www.bitstamp.net/api/v2/ticker/{choice.lower()}/')
		x = r.json()

	#last      Last BTC price.
	#high      Last 24 hours price high.
	#low       Last 24 hours price low.
	#vwap      Last 24 hours volume weighted average price.
	#volume    Last 24 hours volume.
	#bid       Highest buy order.
	#ask       Lowest sell order.
	#timestamp Unix timestamp date and time.
	#open      First price of the day.

		empty_lines()
		print(f"Bitstamp {choice[:3]}/{choice[3:]} Info:")
		empty_lines()
		print(f"Last price: {x['last']} {choice[3:]}")
		print("")
		print(f"Highest buy order: {x['bid']} {choice[3:]}")
		print(f"Lowest sell order: {x['ask']} {choice[3:]}")
		print(f"Spread: {(float(x['ask']) - float(x['bid'])):.8f} {choice[3:]}")
		print("")
		print(f"Daily change: {(float(x['last']) - float(x['open'])):.8f} {choice[3:]}")
		print(f"Daily percentage change: {((float(x['last']) - float(x['open'])) / float(x['open']) * 100):.2f} %")
		print(f"Daily high: {x['high']} {choice[3:]}")
		print(f"Daily low: {x['low']} {choice[3:]}")
		print("")
		print(f"Daily volume: {x['volume']} {choice[:3]} / {float(x['volume']) * float(x['last'])} {choice[3:]}")
		print(f"Daily volume average weighted price: {x['vwap']} {choice[3:]}")
		print("")
		print(f"Last update: {datetime.datetime.fromtimestamp(int(x['timestamp'])).strftime('%d-%m-%Y %H:%M:%S')}")
		empty_lines()

def btc_bal_check():
	r = requests.get(f'https://blockchain.info/balance?active={btc_address}')
	x = r.json()

	empty_lines()
	print(btc_address)
	print("")
	print(f"# transactions: {x[btc_address]['n_tx']}")
	print(f"Total received: {(x[btc_address]['total_received']) /100000000}")
	print(f"Final Balance : {(x[btc_address]['final_balance']) /100000000}")
	empty_lines()

#graph, created with CoinDesk last 30 days API
def desk_graph():

	time = []
	price = []

	r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json')
	data = r.json()["bpi"]

	for k,v in data.items():
		time.append(k[-5:])
		price.append(v)

	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	ax.plot(time,price)
	ax.set_xlabel('time')
	ax.set_ylabel('USD')
	ax.set_title('Bitcoin Chart')

	plt.show()
	empty_lines()

def print_menu():
	empty_lines()
	print("-" * 32 + "Menu" + "-" * 32)
	print("1. Global Crypto Statistics	5.  Bitfinex Market Info")
	print("2. Crypto top25			6.  Bitstamp Trade History")
	print("3. Bitfinex Trade History	7.  Bitstamp Orderbook")
	print("4. Bitfinex Orderbook		8.  Bitstamp Market Info")
	print("9. Btc Balance Check		10. Last 30 Days Graph")
	print("0. Exit")
	print("-" * 68)
	empty_lines()

#Program:

#For all 3 bitstamp functions, the market options are the same
stamp_options = [None, 'btcusd', 'btceur', 'eurusd', 'xrpusd', 'xrpeur', 'xrpbtc',
'ltcusd', 'ltceur', 'ltcbtc', 'ethusd', 'etheur', 'ethbtc', 'bchusd', 'bcheur', 'bchbtc']
user_choice = None
while True:
	if user_choice in [1,2,3,4,5,6,7,8,9,99]:
		input("Press Enter to continue")
#		empty_lines(100) 	#Not sure if i want this, would print 100 empty lines, to clear screen
	print_menu()


	while True:
		try:
			user_choice = int(input("Please make a choice: "))
			break
		except ValueError:
			print("Oops! That was not a valid number. Try again...")

	if user_choice == 0:
		empty_lines()
		print("Goodbye")
		empty_lines()
		break

	elif user_choice == 1:
		cmcglobal()
	elif user_choice == 2:
		cmctop()
	elif user_choice == 3:
		fin_history()
	elif user_choice == 4:
		fin_book()
	elif user_choice == 5:
		fin_info()
	elif user_choice == 6:
		stamp_history()
	elif user_choice == 7:
		stamp_book()
	elif user_choice == 8:
		stamp_info()
	elif user_choice == 9:
		btc_bal_check()
	elif user_choice == 10:
		desk_graph()
#test option
	elif user_choice == 99:
		print("Testing 123")
	else:
		print("Please choose a correct number (0-8)")
