usd = float(input("Enter usd amount:"))
cny_rate = 7.20
gbp_rate = 0.79
eur_rate = 0.92
hkd_rate = 7.82
cny = usd * cny_rate
gbp = usd * gbp_rate
eur = usd * eur_rate
hkd = usd * hkd_rate
print(usd, "USD is", round(cny, 2), "CNY")
print(usd, "USD is", round(gbp, 2), "GBP")
print(usd, "USD is", round(eur, 2), "EUR")
print(usd, "USD is", round(hkd, 2), "HKD")