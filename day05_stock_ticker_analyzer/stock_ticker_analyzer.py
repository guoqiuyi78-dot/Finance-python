stock_ticker_symbol = input("Enter the stock ticker symbol: ")
for letter in stock_ticker_symbol:
    print(letter)
count = 0
for letter in stock_ticker_symbol:
    count = count + 1
print("The number of letters in the stock ticker symbol is: ", (count))
