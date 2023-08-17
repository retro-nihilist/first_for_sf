prices = [34562, 66572, 25683, 17683, 56389, 28973]
## filtered_prices = [25683, 17683, 28973]

prices = [21490, 24901, 24901, 34901, 24142, 64521]
## filtered_prices = [21490, 24901, 24901, 24901, 24521]


#filtered_prices = list()
lambda_filtered_prices = lambda x: x<30000
filtered_prices = list(filter(lambda_filtered_prices, prices))


print (filtered_prices)