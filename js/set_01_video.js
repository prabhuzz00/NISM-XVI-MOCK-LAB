/* 50 MCQs transcribed from set_01.mp4 (phone recording of a sample quiz).
   answer is the 0-based index of the correct option. */
window.SET_01_VIDEO = [
  {
    "id": 1,
    "q": "In commodity future trading, ________ is the price used for calculating the \"delivery default penalty\" in case of non delivery of short sell quantity.",
    "options": [
      "Exercise price of the related option contract",
      "Final settlement price of the futures contract",
      "Daily price range of that futures contract",
      "Closing price of the underlying commodity in the spot market"
    ],
    "answer": 1,
    "explanation": "Commodity futures have two settlement prices. The daily settlement price (DSP), also called the closing price, is used for daily mark-to-market profit or loss. The final settlement price (FSP), also called the Due Date Rate (DDR), is used for the delivery default penalty when a short sale quantity is not delivered, and for compensation to the buyer."
  },
  {
    "id": 2,
    "q": "Volatility is the magnitude of movement in the underlying asset's price in the ________ direction.",
    "options": [
      "Upward",
      "Downward",
      "Upward and downward",
      "flat"
    ],
    "answer": 2,
    "explanation": "Volatility is the magnitude of movement in the underlying asset's price, either up or down. It affects call and put options in the same way. Higher volatility of the underlying means a higher premium."
  },
  {
    "id": 3,
    "q": "________ arises when the buyer/seller has not received the goods/funds but has fulfilled his obligation of making payment/delivery of goods.",
    "options": [
      "Operational Risk",
      "Surveillance related risks",
      "Principal risk",
      "Obligation risk"
    ],
    "answer": 2,
    "explanation": "Principal risk arises when the buyer or seller has fulfilled their own obligation of payment or delivery but has not received the goods or funds. A central counterparty such as a clearing corporation eliminates this risk."
  },
  {
    "id": 4,
    "q": "________ opportunity arises when the futures price of the commodity is more than the sum of spot price and the cost of carrying it till the expiry date.",
    "options": [
      "Algorithm arbitrage",
      "Cash and Carry arbitrage",
      "Reverse Cash and Carry Arbitrage",
      "Spot versus spot arbitrage"
    ],
    "answer": 1,
    "explanation": "Cash-and-carry arbitrage is buying the physical commodity with borrowed funds and simultaneously selling the futures contract. The commodity is delivered at expiry. The opportunity exists when the futures price is higher than the spot price plus the cost of carry until expiry."
  },
  {
    "id": 5,
    "q": "Sticking to the ________ helps to neutralize the volatility difference between Spot and Futures.",
    "options": [
      "Volatility Ratio",
      "Exposure Ratio",
      "Risk Return Ratio",
      "Hedge Ratio"
    ],
    "answer": 3,
    "explanation": "The hedge ratio is the number of lots or contracts a hedger must buy or sell in the futures market to cover risk exposure in the physical or spot market. It neutralizes the volatility difference between spot and futures."
  },
  {
    "id": 6,
    "q": "When an option contract devolve into underlying asset, a PUT option is said to be In The Money (ITM), when ________.",
    "options": [
      "Spot price is lower than strike price",
      "Spot price is higher than strike price",
      "Spot price is equal to Futures price",
      "Spot price is equal to strike price"
    ],
    "answer": 0,
    "explanation": "An in-the-money option would give the holder a positive cash flow if it were exercised immediately. A put is ITM when the spot price is lower than the strike price. A call is ITM when the spot price is higher than the strike price."
  },
  {
    "id": 7,
    "q": "________ is NOT considered as financial futures.",
    "options": [
      "Gold Futures",
      "Currency Futures",
      "Bond Futures",
      "Stock Futures"
    ],
    "answer": 0,
    "explanation": "Futures on currency rates, interest rates (bond futures) and equity prices (stock or equity index futures) are financial futures. Futures on crude oil, metals such as gold, and agricultural products are commodity futures."
  },
  {
    "id": 8,
    "q": "What can an option seller do?",
    "options": [
      "An option seller can exercise the option once the expiration date has passed",
      "An option seller can ask to exercise the option on the expiration date",
      "An option seller can square off the option in the Exchange before the expiration date",
      "All of the above"
    ],
    "answer": 2,
    "explanation": "An option seller cannot demand exercise of the option. Only the option buyer can exercise. The seller can square off the position on the exchange before the expiry date."
  },
  {
    "id": 9,
    "q": "On May 25, a trader agreed to sell rice for delivery on a future specified date (say one month from May 25 i.e., on June 25) irrespective of the actual price prevailing on June 25. This agreement is an example of",
    "options": [
      "Commodity delivery contract",
      "Commodity future contract",
      "Commodity forward contract",
      "Commodity cash contract"
    ],
    "answer": 2,
    "explanation": "A forward contract is an agreement to deliver goods or the underlying asset on a specific future date at a price agreed on the date of the contract."
  },
  {
    "id": 10,
    "q": "If the closing price for Aluminum futures contract was Rs. 300 yesterday and Daily Price Range is 7 percent as per the contract specification. What would be the price range for this contract today?",
    "options": [
      "Rs. 279 to Rs. 321",
      "Rs. 290 to Rs. 321",
      "Rs. 283 to Rs. 311",
      "Rs. 300 to Rs. 330"
    ],
    "answer": 0,
    "explanation": "The daily price range is 7 percent. 7 percent of Rs. 300 is Rs. 21, so today's range is 300 − 21 to 300 + 21, that is Rs. 279 to Rs. 321."
  },
  {
    "id": 11,
    "q": "A hedger plans to buy a commodity in the spot market at a future date. What should be his first step in setting up a hedge to protect himself from any price rise?",
    "options": [
      "He buys futures contract",
      "He sells futures contract",
      "He buys and sells spot contract simultaneously",
      "He buys and sells futures contract simultaneously"
    ],
    "answer": 0,
    "explanation": "Buying a futures contract locks the purchase price. A later rise in prices is offset by the futures position. When he buys the commodity in the spot market, he sells the futures contract."
  },
  {
    "id": 12,
    "q": "While introducing derivatives contracts on a particular commodity, the commodity exchange will consider which of the following factors?",
    "options": [
      "Price volatility of the commodity",
      "Political sensitivity of commodity",
      "Demand for introduction of a particular commodity from the market players",
      "All of the above"
    ],
    "answer": 3,
    "explanation": "Before introducing a commodity, an exchange considers factors such as demand for the commodity, storability, and government regulation and control."
  },
  {
    "id": 13,
    "q": "Calculate the total cost of carry from the following data — Spot price of the commodity Rs 35000; Time period 180 days; Cost of interest 9% and Cost of storage 2%.",
    "options": [
      "Rs. 1677.36",
      "Rs. 1749.22",
      "Rs. 1898.43",
      "Rs. 1955.49"
    ],
    "answer": 2,
    "explanation": "Cost of carry has two parts for 180 days: interest cost and storage cost. Interest is Rs. 1,553.26 and storage is Rs. 345.17, so total cost of carry is Rs. 1,898.43."
  },
  {
    "id": 14,
    "q": "Which price is used to calculate the mark-to-market profit or loss at the end of each trading day for commodity futures trading?",
    "options": [
      "Due date rate of the respective futures contract",
      "Closing price of the underlying commodity in the spot market",
      "The daily price range of the respective futures contract",
      "Daily settlement price of the respective futures contract"
    ],
    "answer": 3,
    "explanation": "Mark-to-market profit or loss is calculated by marking all futures positions to the daily settlement price (DSP) at the end of each trading day."
  },
  {
    "id": 15,
    "q": "Ms. Reshma has entered a short speculative position in commodity futures. Which of the following would be a possible outcome for Ms. Reshma at the expiry of the contract?",
    "options": [
      "Ms. Reshma incurs a loss if the price of futures contract decreases",
      "Ms. Reshma incurs a loss if the price of futures contract increases",
      "Ms. Reshma would neither make a profit nor a loss in this position for any price of futures",
      "Ms. Reshma will always makes profit irrespective of whether the futures prices increases or decreases"
    ],
    "answer": 1,
    "explanation": "A short position means she has sold the futures expecting prices to fall. She profits if futures prices fall and loses if they rise. If she sells at Rs. 100 and the price at expiry is Rs. 120, she loses Rs. 20."
  },
  {
    "id": 16,
    "q": "A person who is long on a Call Option has",
    "options": [
      "A right to buy without any obligation to buy",
      "A right to sell with an obligation to sell",
      "A right to buy with an obligation to buy",
      "A right to sell without any obligation to sell"
    ],
    "answer": 0,
    "explanation": "The buyer of an option has a right but not an obligation. For that right, the buyer pays an option premium to the seller."
  },
  {
    "id": 17,
    "q": "Identify the true statement with respect to the relation between Time to Expiration and Option Premium. (Assume all other factors remain the same)",
    "options": [
      "When the time to expiration is higher, higher is the put option premium but lower is the call option premium",
      "When the time to expiration is higher, higher is the call option premium but lower is the put option premium",
      "When the time to expiration is higher, the premiums of both call option and put option is higher",
      "Time to expiration does not affect the option premium"
    ],
    "answer": 2,
    "explanation": "Generally, the longer the maturity of the option, the greater the uncertainty, and therefore the higher the premiums of both call and put options."
  },
  {
    "id": 18,
    "q": "Which type of strategy is adopted to benefit the trader when the near-month contract is under priced or the far-month contract is overpriced and the trader of the above strategy buys the near-month contract and sells the far-month contract when the spread is not fair and squares off the positions when the spread corrects and the contracts are traded at fair spread?",
    "options": [
      "Inter commodity spread",
      "Long hedge",
      "Selling a Spread",
      "Buying a Spread"
    ],
    "answer": 3,
    "explanation": "Buying a spread is an intra-commodity spread: buy the near-month contract and sell the far-month contract when the near month is underpriced or the far month is overpriced, then square off when the contracts trade at a fair spread."
  },
  {
    "id": 19,
    "q": "How does an arbitrageurs make riskless profits?",
    "options": [
      "Arbitrageurs are specialist traders and make profits irrespective of market conditions",
      "His selling price of an asset in one market should be lower than his buying price in another market after adjusting for transaction costs etc.",
      "His selling price of an asset in one market should be higher than his buying price in another market after adjusting for transaction costs etc.",
      "His selling price of an asset in one market should be exactly equal to his buying price in another market after adjusting for transaction costs etc."
    ],
    "answer": 2,
    "explanation": "Arbitrageurs simultaneously buy and sell in two markets. They earn a riskless profit when the selling price in one market is higher than the buying price in the other by more than the transaction costs."
  },
  {
    "id": 20,
    "q": "Since the ________ is paying the premium to the seller, he has the right to exercise the option when it is favourable to him but no obligation to do so.",
    "options": [
      "Writer",
      "Buyer",
      "Seller",
      "Arbitrageur"
    ],
    "answer": 1,
    "explanation": "The premium is the cost of the option, paid by the buyer to the seller, and it is not refundable. Because the buyer pays the premium, the buyer has the right but not the obligation to exercise. The seller has an obligation and no right."
  },
  {
    "id": 21,
    "q": "Mr. Amit is working with a commodity broking house and is an expert in Gold prices movements. As per his view, Gold should appreciate in the next 3 months and accordingly he advised some of his clients to take a long position in gold futures and as he was very confident, he also guaranteed against any losses. The senior manager takes an action against Mr. Amit for violating some trading guidelines. What should Mr. Amit have done to avoid the punishment?",
    "options": [
      "Mr. Amit should not have guaranteed against any losses",
      "Mr. Amit should have advised the clients correctly to take long position for 1 month and not 3 months as 3 month is a long period",
      "Mr. Amit should have advised the clients correctly to take long position for 6 months and not 3 months as 3 month is a short period",
      "Mr. Amit should have advised the clients to take short position"
    ],
    "answer": 0,
    "explanation": "Exchange regulations set a code of conduct for the commodity derivatives segment. One rule is that no trading member, or person associated with the trading member, shall guarantee a client against a loss in any transaction effected for that client."
  },
  {
    "id": 22,
    "q": "During the commodity payout process, ________ with the help of clearing banks transfer the funds (sale proceeds) to the clearing member of the seller.",
    "options": [
      "Clearing Corporation",
      "The Commodity Exchange",
      "SEBI",
      "Commodity Broker"
    ],
    "answer": 0,
    "explanation": "The clearing corporation, with the help of clearing banks, transfers funds equivalent to the contract value to the clearing member of the seller."
  },
  {
    "id": 23,
    "q": "The regulatory framework for commodity markets in India consist of three tiers. Which are these three tiers?",
    "options": [
      "Forward Markets Commission, Securities and Exchange Board of India and Government of India",
      "Forward Markets Commission, Securities and Exchange Board of India and Exchanges",
      "Forward Markets Commission, Exchanges and Government of India",
      "Securities and Exchange Board of India, Exchanges and Government of India"
    ],
    "answer": 3,
    "explanation": "The objective of commodity market regulation is to maintain and promote fairness, efficiency, transparency and growth of commodity markets, and to protect the interests of stakeholders. The three tiers are SEBI, the exchanges, and the Government of India."
  },
  {
    "id": 24,
    "q": "When the futures price is ________ than the spot price, it is known as Backwardation.",
    "options": [
      "higher",
      "lower",
      "more volatile",
      "less volatile"
    ],
    "answer": 1,
    "explanation": "When the futures price is less than the spot price, the basis is a positive number. That situation is known as a backwardation market."
  },
  {
    "id": 25,
    "q": "Which one of these complaints against a trading member can an Exchange take up for redressal?",
    "options": [
      "Claims regarding unauthorized transaction in the client's account",
      "Claims regarding notional loss for the disputed trade",
      "Complaints in respect of transactions which are already subject matter of Arbitrage proceedings",
      "Complaints regarding land dealings between a client and trading member"
    ],
    "answer": 0,
    "explanation": "An exchange can take up complaints such as non-receipt of funds or securities, non-receipt of documents such as the member-client agreement and contract notes, excess brokerage, unauthorized transfer of funds, and claims regarding an unauthorized transaction in the client's account."
  },
  {
    "id": 26,
    "q": "Which of the following are the risks generally faced by the Commodity importers?",
    "options": [
      "Foreign exchange rate risk",
      "Commodity price risk",
      "Geopolitical risk",
      "All of the above"
    ],
    "answer": 3,
    "explanation": "Importers and exporters face foreign-exchange risk because most commodities are priced in US dollars, commodity-price risk from adverse price moves, and geopolitical risk when global supply is disrupted."
  },
  {
    "id": 27,
    "q": "What will be the theoretical futures price of the futures contract, if the Spot price of a commodity is Rs 40000, the time period is 90 days, the interest rate is 6% and storage costs is 1%?",
    "options": [
      "40466.35",
      "41800.50",
      "41233.80",
      "40688.80"
    ],
    "answer": 3,
    "explanation": "Theoretical futures price equals spot price plus cost of carry. Here the cost of carry has two components: interest cost for 90 days and storage cost for 90 days. The quiz marks 40688.80."
  },
  {
    "id": 28,
    "q": "Which act gives SEBI the power to prohibit undesirable speculation in Indian securities market?",
    "options": [
      "Stock Exchange (Regulation) Act, 1992",
      "Securities Contracts (Regulation) Act, 1956",
      "Futures Contracts (Regulation) Act, 1952",
      "Anti Speculation (Regulation) Act, 2001"
    ],
    "answer": 1,
    "explanation": "The Securities Contracts (Regulation) Act, 1956 provides for direct and indirect control of securities trading and the running of stock exchanges, and it is used to prevent undesirable transactions in securities."
  },
  {
    "id": 29,
    "q": "________ are fully standardized and their contract terms are specified by the derivatives exchanges.",
    "options": [
      "OTC Contracts",
      "Exchange Traded Derivatives",
      "Forwards Contracts",
      "Multi-lateral Contracts"
    ],
    "answer": 1,
    "explanation": "Exchange-traded derivatives are fully standardized. The exchange specifies quantity and quality, delivery time and place, the method of closing the contract, and permissible price fluctuations."
  },
  {
    "id": 30,
    "q": "________ is the change in option price given a one percentage point change in the risk-free interest rate.",
    "options": [
      "Gamma",
      "Rho",
      "Theta",
      "Vega"
    ],
    "answer": 1,
    "explanation": "Rho is the change in an option's price for a one percentage point change in the risk-free interest rate. It measures how the option price changes when the cost of funding the underlying changes."
  },
  {
    "id": 31,
    "q": "Which of the following Acts are repealed?",
    "options": [
      "SEBI's Stock Exchange and Clearing Corporation Regulation, 2012",
      "Forward Contract Regulation Act, 1952",
      "SARFESI Act, 2002",
      "SEBI's (Vault Managers) Regulation, 2021"
    ],
    "answer": 1,
    "explanation": "Parliament passed the Forward Contracts (Regulation) Act in 1952 to regulate forward contracts in commodities. That Act was later repealed when regulation of commodity derivatives moved to SEBI."
  },
  {
    "id": 32,
    "q": "When can the Buyer or Seller express their intention to give or take delivery?",
    "options": [
      "Anytime during the contract's life",
      "Only on the last trading day of the contract",
      "Only during the tender marking period",
      "Only after the expiry of the contract"
    ],
    "answer": 2,
    "explanation": "Each commodity has its own delivery logic in the contract specification. The exchange permits tendering of deliveries on specific tender days during the delivery period."
  },
  {
    "id": 33,
    "q": "Identify the advantage(s) of Commodity Futures in comparison to Commodity Forwards?",
    "options": [
      "There is efficient price discovery in commodity futures",
      "There is transparency of pricing in commodity futures",
      "There is higher liquidity due to standardization of contracts in commodity futures",
      "All of the above"
    ],
    "answer": 3,
    "explanation": "Compared with forwards, commodity futures provide efficient price discovery by bringing together buyers and sellers, transparency of pricing, and higher liquidity because the contracts are standardized."
  },
  {
    "id": 34,
    "q": "The difference between the prices of two future contracts is known as",
    "options": [
      "Premium",
      "Basis",
      "Spread",
      "Margin"
    ],
    "answer": 2,
    "explanation": "Spread is the difference between the prices of two futures contracts. When the actual spread of the same commodity widens, a trader may buy the underpriced near-month contract and sell the overpriced far-month contract."
  },
  {
    "id": 35,
    "q": "In case of a Call Option, time decay will work in favour of",
    "options": [
      "Option Writer (Seller)",
      "Option Buyer",
      "Both option buyer and seller",
      "Neither option buyer nor option seller"
    ],
    "answer": 0,
    "explanation": "If the other factors that affect an option's price stay the same, the time-value portion of the premium decreases as time passes. That time decay works in favour of the option writer."
  },
  {
    "id": 36,
    "q": "ICAI's guidance note requires that all derivatives are recognised on the ________ and measured at fair value.",
    "options": [
      "Cashflow statement",
      "Balance sheet",
      "Speculative statement",
      "Income statement"
    ],
    "answer": 1,
    "explanation": "The guidance note of the Institute of Chartered Accountants of India requires derivatives to be recognised on the balance sheet and measured at fair value, because a derivative contract is a contractual right or obligation."
  },
  {
    "id": 37,
    "q": "Under the staggered delivery mechanism, the buyer who is randomly assigned a delivery obligation by the trading system of the exchange has to take the delivery from the delivery centre",
    "options": [
      "On the same day",
      "on T+2 day",
      "On the next day",
      "On the expiry date"
    ],
    "answer": 1,
    "explanation": "Under the staggered delivery mechanism, the seller may mark an intention to deliver on any day during the last 10 days before expiry. The corresponding buyer is randomly allocated by the trading system and takes delivery from the delivery centre on T+2 day. This confirms delivery in the near-month contract and keeps price volatility in check."
  },
  {
    "id": 38,
    "q": "Legal risks in commodities trading can be related to",
    "options": [
      "Commodities Transaction Tax (CTT)",
      "Essential Commodities Act",
      "FSSAI standards",
      "All of the above"
    ],
    "answer": 3,
    "explanation": "Exchanges face legal risk because of uncertainty from legal actions, or uncertainty in the applicability or interpretation of contracts, laws or regulations."
  },
  {
    "id": 39,
    "q": "What is the objective of Hedging?",
    "options": [
      "Hedging leads to diversification of portfolio",
      "Hedging helps generate 'Alpha' due to leverage offered by derivatives markets",
      "Hedging helps generate excessive returns",
      "Hedging limits the risks associated with the price changes"
    ],
    "answer": 3,
    "explanation": "The objective of hedging is to reduce or limit the risks associated with price changes."
  },
  {
    "id": 40,
    "q": "________ are allowed exposure in commodity derivatives",
    "options": [
      "Hedge Funds",
      "Gold ETFs",
      "Mutual Funds",
      "All of the above"
    ],
    "answer": 3,
    "explanation": "Financial institutions such as hedge funds, exchange traded funds, trading members and mutual funds can use commodity indices as a performance benchmark or as a way to take exposure to commodity markets."
  },
  {
    "id": 41,
    "q": "When a client registers a complaint, the dispute resolution mechanism follows following sequence -",
    "options": [
      "Exchange - SEBI - Grievance redressal committee",
      "Grievance redressal committee - Exchange - SEBI",
      "Arbitration - Grievance redressal committee - Exchange",
      "Exchange - Grievance redressal committee - SEBI"
    ],
    "answer": 0,
    "explanation": "The investor should first approach the concerned exchange or intermediary against whom the complaint is made. The quiz marks the sequence Exchange, then SEBI, then the grievance redressal committee."
  },
  {
    "id": 42,
    "q": "The relationship between Futures and Spot Price is logically explained by the formula F = S × e^(r × n). What does S stand for if F: Futures price, r: Cost of financing in percentage, n: time till the expiry of the contract and e = a constant number?",
    "options": [
      "Storage Cost",
      "Scrap value",
      "Spot Price",
      "Simple Interest"
    ],
    "answer": 2,
    "explanation": "In F = S × e^(r × n), S is the spot price, F is the futures price, r is the financing cost, n is the time to expiry, and e is a constant."
  },
  {
    "id": 43,
    "q": "The relationship between the Futures price and Spot price is expressed as F = S + C − Y, what does C indicate in this equation?",
    "options": [
      "Convenience yield",
      "Convergence Cost",
      "Cost of carry",
      "Cost of Living"
    ],
    "answer": 2,
    "explanation": "F = S + C − Y, where F is the futures price, S is the spot price, C is the cost of carry, and Y is the convenience yield."
  },
  {
    "id": 44,
    "q": "Which of the following hedging method should not be used by a manufacturer of a product?",
    "options": [
      "Selling the finished products in future",
      "Buy a Call Option on the raw materials use to manufacture the product",
      "Buy the raw materials use to manufacture the product in futures",
      "Selling a Put Option in the finished goods"
    ],
    "answer": 3,
    "explanation": "A manufacturer hedges either a rise in the price of raw materials or a fall in the price of finished goods. Selling a put option on the finished goods is not an appropriate hedge."
  },
  {
    "id": 45,
    "q": "On expiry of futures resulting into delivery, the seller will raise bill on the buyer and charges appropriate GST rate on",
    "options": [
      "Spot polling price",
      "Exercise price",
      "Daily settlement price",
      "Final settlement price"
    ],
    "answer": 3,
    "explanation": "Once delivery obligations are assigned, the seller raises the bill on the buyer at the final settlement price. The bill includes GST levied on that final settlement price."
  },
  {
    "id": 46,
    "q": "Black-Scholes option pricing model uses ________ to estimate theoretical options price.",
    "options": [
      "Underlying asset of the asset",
      "Strike price of the option",
      "Risk-free interest rate",
      "All of the above"
    ],
    "answer": 3,
    "explanation": "The Black-Scholes model estimates a theoretical option price from the underlying price, strike price, volatility, time to expiration, and the short-term risk-free interest rate."
  },
  {
    "id": 47,
    "q": "Miss Smita feels that Gold September futures are underpriced when compared to Gold November futures. To take advantage of this mispricing, she buys 1 Kg of September futures at Rs. 52000 per 10 grams and sells 1 Kg of November Gold futures at Rs. 52200. In October, she squares up the September Gold futures at Rs. 52100 and November Gold futures at Rs. 52250 and makes a profit of Rs. 5000. These trades done by Miss Smita is known as",
    "options": [
      "Reverse Cash and Carry Arbitrage",
      "Cash and Carry Arbitrage",
      "Buying a Spread",
      "Selling a Spread"
    ],
    "answer": 2,
    "explanation": "Buying a spread means buying the near-month contract and simultaneously selling the far-month contract, used when the near month is underpriced relative to the far month. She buys September and sells November, then squares both legs."
  },
  {
    "id": 48,
    "q": "Goods and Services Tax (GST) on goods is levied on which of these in commodity derivatives?",
    "options": [
      "Exercise of options leading to delivery of goods",
      "Trading in options",
      "Exercise of options devolving in futures",
      "Trading in futures"
    ],
    "answer": 0,
    "explanation": "GST on goods in commodity derivatives is levied when exercise of an option leads to delivery of the goods."
  },
  {
    "id": 49,
    "q": "Which of these margins is deposited with the Commodity Futures Exchange?",
    "options": [
      "Additional Margin",
      "Margin of Safety",
      "Crack Margin",
      "Crush Margin"
    ],
    "answer": 0,
    "explanation": "Futures margins include initial margin, extreme loss margin and mark-to-market margin, and additional margin may also be collected. Options on futures have a devolvement margin. Crack margin and crush margin are processing spreads, not exchange margins."
  },
  {
    "id": 50,
    "q": "An oil refiner may enjoy a ________ yield on crude oil inventories and without it, production will be interrupted and the refiner cannot produce any finished product.",
    "options": [
      "Current",
      "Spread",
      "Production",
      "Convenience"
    ],
    "answer": 3,
    "explanation": "Convenience yield is the benefit of owning the physical commodity rather than holding a futures contract on it. For an oil refiner, holding crude oil inventories avoids a break in production of finished products."
  }
];
