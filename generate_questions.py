"""Generate 5 NISM Series XVI mock sets (100 MCQs each) as js/questions.js"""
from __future__ import annotations
import json
import math
from pathlib import Path

CHAPTERS = {
    1: "Introduction to Commodity Markets",
    2: "Commodity Indices",
    3: "Commodity Futures",
    4: "Commodity Options",
    5: "Uses of Commodity Derivatives",
    6: "Trading Mechanism",
    7: "Clearing, Settlement and Risk Management",
    8: "Legal and Regulatory Environment",
    9: "Accounting and Taxation",
    10: "Code of Conduct and Investor Protection",
}

WEIGHTS = {1: 10, 2: 5, 3: 15, 4: 15, 5: 15, 6: 10, 7: 15, 8: 5, 9: 5, 10: 5}


def inr(n, nd=0):
    x = round(n, nd) if nd else int(round(n))
    if nd:
        s = f"{x:,.{nd}f}"
    else:
        s = f"{int(x):,}"
    return "Rs " + s.replace(",", ",")


def Q(ch, topic, q, options, ans, explanation, example):
    if not (0 <= ans <= 3):
        raise ValueError(q)
    if len(options) != 4:
        raise ValueError(q)
    return {
        "chapter": ch,
        "chapterName": CHAPTERS[ch],
        "topic": topic,
        "q": q,
        "options": options,
        "answer": ans,
        "explanation": explanation,
        "example": example,
    }


def distract(correct, offs, nd=0):
    vals = [correct]
    for o in offs:
        vals.append(correct + o)
    out = []
    seen = set()
    for v in vals:
        key = round(v, nd)
        if key in seen:
            continue
        seen.add(key)
        out.append(inr(v, nd) if nd else inr(v))
        if len(out) == 4:
            break
    while len(out) < 4:
        out.append(inr(correct * (1.05 + 0.02 * len(out)), nd) if nd else inr(correct + 50 * len(out)))
    return out
# ---------- CONCEPTUAL BANK (unique across all 5 sets) ----------
CONCEPTUAL = []

def C(ch, topic, q, options, ans, explanation, example):
    CONCEPTUAL.append(Q(ch, topic, q, options, ans, explanation, example))


# ===== Chapter 1 =====
C(1, "History", "Which of the following is regarded as the first organised futures market in the world?",
  ["Chicago Board of Trade (1848)", "Osaka Rice Exchange (1730)", "London Metal Exchange (1877)", "Bombay Cotton Trade Association (1875)"],
  1, "The Osaka Rice Exchange, set up in Japan in 1730, is treated as the earliest organised futures market. Rice bills represented the right to take delivery later at a price agreed today.",
  "If a merchant in 1730s Osaka bought a rice bill, he locked a future delivery price — the same economic idea as a modern futures contract.")

C(1, "History", "Organised commodity derivatives trading in India started in 1875 with which underlying?",
  ["Gold", "Wheat", "Cotton", "Jute"],
  2, "The Bombay Cotton Trade Association Limited started organised commodity derivatives trading in India in 1875 with cotton as the underlying.",
  "Think of 19th-century Bombay as a cotton hub: the first Indian futures-style contracts were written on cotton, not metals.")

C(1, "History", "Regulation of commodity derivatives in India shifted from FCRA to SEBI under SCRA with effect from:",
  ["28 September 2015", "1 April 2017", "1 October 2018", "24 March 2022"],
  0, "The Forward Contracts (Regulation) Act, 1952 was repealed and regulation moved to SEBI under the Securities Contracts (Regulation) Act, 1956 from 28 September 2015. FMC was merged into SEBI on that date.",
  "After 28-09-2015, a gold futures contract is a 'security' under SCRA, regulated by SEBI like an equity derivative.")

C(1, "History", "References to commodity trading practices in India appear as far back as 320 B.C. in:",
  ["Manusmriti", "Kautilya’s Arthashastra", "Ain-i-Akbari", "Rigveda"],
  1, "Kautilya’s Arthashastra (around 320 B.C.) contains early references to commodity trading practices in India.",
  "The exam often tests this date-and-text pair: 320 B.C. + Arthashastra.")

C(1, "Spot vs derivatives", "In a commodity spot (cash) market, delivery and payment typically occur:",
  ["On a future date at a price agreed today", "Immediately at the prevailing market price", "Only after warehouse assaying", "Only through the clearing corporation"],
  1, "Spot markets trade for immediate delivery and payment at the current demand-supply price. Futures lock a future date and price today.",
  "Buying 10 g gold from a jeweller today at the tag price is a spot trade; buying MCX gold futures for next month is a derivative trade.")

C(1, "Spot vs derivatives", "A key risk of OTC forward contracts that exchange-traded futures are designed to remove is:",
  ["Price risk", "Basis risk", "Counterparty default risk", "Currency risk"],
  2, "Forwards are bilateral and customised, so either party may default. Futures are guaranteed by the clearing corporation acting as central counterparty.",
  "If a mill agrees a forward with a farmer and the farmer walks away after prices rise, the mill has counterparty risk. On NCDEX/MCX that risk is taken by the clearing corporation.")

C(1, "Soft vs hard", "Which of the following is a 'hard' commodity?",
  ["Coffee", "Sugar", "Crude oil", "Cocoa"],
  2, "Hard commodities are mined or extracted natural resources (crude oil, gold, silver, metals). Soft commodities are perishable agricultural products.",
  "Wheat, coffee and sugar are soft; gold, silver and crude oil are hard.")

C(1, "eNAM", "eNAM is implemented by which organisation under the Ministry of Agriculture?",
  ["NABARD", "Small Farmers Agribusiness Consortium (SFAC)", "WDRA", "FCI"],
  1, "The Electronic National Agriculture Market (eNAM) is a pan-India electronic trading portal implemented by SFAC, networking APMCs into a unified market.",
  "A farmer in one APMC can receive bids from traders in other networked mandis through eNAM rather than being limited to local middlemen.")

C(1, "Instruments", "An option buyer has:",
  ["The right and the obligation to buy or sell", "The right but not the obligation to buy or sell", "Only an obligation and no right", "Neither right nor obligation"],
  1, "The option buyer pays premium for a right without obligation. The seller/writer has the obligation if the buyer exercises.",
  "A jeweller buying a gold call can ignore the option if gold falls and lose only the premium; the call writer must sell if the jeweller exercises.")

C(1, "Instruments", "In a fixed-for-floating commodity swap, the counterparties exchange:",
  ["The physical commodity for cash on T+2", "A series of cash payments based on fixed vs floating prices", "Only the option premium", "Warehouse receipts"],
  1, "Swaps are agreements to exchange a series of cash payments for a stated period based on fixed or floating prices, not a single futures settlement.",
  "An airline may pay a fixed jet-fuel price and receive floating market price, converting uncertain fuel cost into a stable cash flow.")

C(1, "Exchanges", "Which of the following is NOT a national exchange currently trading commodity derivatives in India?",
  ["MCX", "NCDEX", "NSE", "OTC Exchange of India"],
  3, "National exchanges for commodity derivatives are MCX, NCDEX, NSE and BSE. OTC Exchange of India is not a commodity derivatives exchange.",
  "A gold futures trade can be done on MCX (and some other recognised exchanges), not on an unrecognised OTC venue.")

C(1, "Participants", "Hedgers in commodity derivatives generally:",
  ["Have no underlying exposure and only seek price bets", "Have commercial exposure and use derivatives to manage price risk", "Only provide two-way quotes", "Only trade intra-day"],
  1, "Hedgers are typically producers, processors, exporters or importers with physical exposure. They use futures/options to reduce, not increase, price risk.",
  "A farmer fearing a fall in soybean prices sells soybean futures; a jeweller fearing a rise in gold prices buys gold futures.")

C(1, "Participants", "Day traders differ from position traders because day traders:",
  ["Always take delivery", "Square off before the close of the same trading day", "Must be FPIs", "Never pay margin"],
  1, "Day traders liquidate the same day. Position traders may hold overnight, for weeks or months, and may roll near-month contracts.",
  "Buying crude at 10 a.m. and selling before the evening session close is day trading; holding gold futures for three weeks is position trading.")

C(1, "Participants", "Market makers are distinguished from other speculators mainly by:",
  ["Exemption from margins", "An obligation to provide two-way quotes", "The right to avoid delivery", "Trading only in options"],
  1, "Market makers must continuously provide bid and ask quotes on terms prescribed by the exchange, supplying liquidity.",
  "If gold’s best bid-ask would otherwise be very wide, a market maker posts both a buy and a sell quote so others can trade.")

C(1, "Participants", "Arbitrageurs seek:",
  ["A one-sided bet on monsoon", "Riskless profit from price differences across markets", "Maximum overnight volatility", "Physical stocks only"],
  1, "Arbitrage is simultaneous buy and sell in two markets where one price is inconsistent with the other, aiming at a riskless profit. Opportunities vanish quickly.",
  "If gold futures trade above fair value (spot + carry), buy spot and sell futures; the reverse if futures are cheap.")

C(1, "FPI", "To begin with, FPIs were allowed in Indian ETCDs in:",
  ["All agricultural options on goods", "Cash-settled non-agricultural commodity derivatives and related indices", "Only electricity futures", "Only warehouse receipts"],
  1, "SEBI allowed FPIs in cash-settled non-agricultural commodity derivatives and indices of such commodities, subject to risk management conditions.",
  "An FPI can take a position in cash-settled crude or natural gas futures/index products, not in a sensitive agri contract meant for farmer hedging.")

C(1, "Commodity vs financial", "A feature more important in commodity derivatives than in typical financial derivatives is:",
  ["Daily MTM", "Physical delivery, grading and warehousing", "Use of a clearing corporation", "Margin collection"],
  1, "Commodity contracts must specify quality, warehouse delivery and often a delivery notice period. Equity index futures are usually cash-settled without grading.",
  "A gold bar delivered on MCX must meet purity and accredited-vault rules; a Nifty future does not require delivery of 50 shares.")

C(1, "Ecosystem", "Electronic Negotiable Warehouse Receipts (eNWRs) in India are issued through repositories such as:",
  ["Only RBI", "NeRL and CCRL", "Only SEBI", "Only FMC"],
  1, "National E-Repository Ltd (NeRL, NCDEX group) and CCRL (CDSL Commodity Repository) issue/maintain eNWRs, facilitating pledge finance on stored goods.",
  "A farmer deposits chana in a WDRA warehouse, gets an eNWR, and can pledge it to a bank instead of selling immediately at a weak harvest price.")

C(1, "Ecosystem", "WDRA is a statutory authority under which Act?",
  ["SCRA, 1956", "SEBI Act, 1992", "Warehousing (Development and Regulation) Act, 2007", "FCRA, 1952"],
  2, "The Warehousing Development and Regulatory Authority regulates warehouses, especially for agricultural commodities, under the 2007 Act. SEBI coordinates with WDRA on exchange-accredited warehouses.",
  "Only WDRA-registered warehouses can typically be used for agri delivery on exchanges.")

C(1, "Clearing", "The entity that becomes central counterparty and guarantees settlement of exchange trades is the:",
  ["Warehouse service provider", "Clearing corporation", "Repository participant", "Assayer"],
  1, "The clearing corporation uses novation: it becomes buyer to every seller and seller to every buyer, eliminating bilateral credit risk.",
  "After you buy gold futures through a broker, your counterparty for settlement is the clearing corporation, not the anonymous seller.")

C(1, "Price factors", "The basic commodity balance identity is:",
  ["Production = Price × Quantity", "Opening stock + production + imports = consumption + exports (+ closing stock)", "Futures price = Option premium + strike", "GDP = C + I + G only"],
  1, "Supply side (opening stock + output + imports) equals use (domestic consumption + exports), with any surplus becoming closing stock. Imbalance moves prices.",
  "If India produces 100, imports 20, opens with 10, consumes 90 and exports 15, closing stock is 25. A smaller closing stock usually supports prices.")

C(1, "Price factors", "Copper is often called 'Dr. Copper' because:",
  ["It is used only in medicines", "Its demand tends to track industrial/economic growth", "SEBI classifies it as a pharmaceutical commodity", "It has zero storage cost"],
  1, "Copper is widely used in power and construction, so its demand (and price) often signals the health of the real economy.",
  "A global capex boom typically lifts copper demand; a manufacturing recession often cools it.")

C(1, "Price factors", "Most internationally traded commodities are priced in USD. If INR depreciates against USD, the INR price of imported commodities tends to:",
  ["Fall", "Rise", "Become zero", "Be unaffected"],
  1, "A weaker INR means more rupees are needed to buy the same dollar-priced commodity, so domestic prices of imports such as crude or gold usually rise.",
  "If crude is $80/barrel and USDINR moves from 80 to 84, the rupee cost of that barrel rises even if the dollar price is unchanged.")

C(1, "Price factors", "Higher domestic interest rates tend to:",
  ["Always raise commodity futures prices", "Raise the cost of carrying inventories and can pressure commodity prices", "Eliminate backwardation forever", "Ban FPI participation"],
  1, "Higher rates increase inventory carrying cost, encourage extraction/sale today, and can shift speculators toward interest-bearing assets — generally bearish for spot commodity prices, though futures fair value also embeds financing.",
  "At 12% financing vs 6%, holding physical gold for a year costs more, so the fair futures premium over spot is larger, but cash demand for inventories may fall.")

C(1, "MF participation", "From 2019, SEBI allowed mutual funds to participate in commodity derivatives subject to restrictions. Multi-asset schemes must invest a minimum of 10% in at least:",
  ["Two asset classes", "Three asset classes", "Five asset classes", "Only gold ETFs"],
  1, "Multi-asset mutual fund schemes must invest at least 10% in each of at least three asset classes. Hybrid and multi-asset schemes are the typical MF vehicles for commodity exposure.",
  "A multi-asset fund might hold equity, debt and gold/commodity futures, each at least 10%.")

C(1, "Options history", "Commodity options on individual commodity futures in India started around:",
  ["2003", "Late 2017", "March 2022", "2015"],
  1, "Options on commodity futures began in late 2017 (initially devolving into the underlying futures). Index futures started in 2020; index options were permitted in March 2022.",
  "A 2018 gold option on MCX would devolve into a gold futures position, not directly into physical gold (options on goods came later, around 2020).")

C(1, "Custodians", "Custodians in the commodity markets are typically SEBI-registered entities that:",
  ["Assay metal purity in warehouses", "Safekeep assets and settle trades for institutional/FPI clients", "Set daily price limits", "Issue eNWRs"],
  1, "Custodians hold securities/cash, settle trades for DIIs and FPIs, and provide related services. They do not replace warehouses or exchanges.",
  "An FPI trading crude futures uses a custodian/clearing arrangement rather than a retail demat-only gold vault.")

C(1, "Weather", "WTI crude oil futures briefly traded at negative prices in April 2020 mainly because of:",
  ["A SEBI ban on energy futures", "A storage/demand shock during COVID lockdowns", "Introduction of CTT", "Demutualisation of MCX"],
  1, "Lockdowns crushed demand while storage filled up, so traders paid others to take delivery. Option prices still cannot go negative; puts became deep ITM.",
  "If storage is full, a long futures holder facing delivery may accept a negative price rather than take unstorable barrels.")

C(1, "RP", "Repository Participants (RPs) are intermediaries that mainly:",
  ["Trade only for their proprietary book", "Do KYC of depositors and facilitate eNWR issuance, pledge and transfer", "Fix MSP", "Collect CTT for CBDT"],
  1, "RPs (banks/FIs/SEBI-licensed intermediaries) handle depositor KYC and eNWR life-cycle services through the repository system.",
  "A bank acting as RP opens the eNWR account and helps pledge the receipt to itself for a warehouse-receipt loan.")

C(1, "Economic functions", "Transfer of risk in derivatives markets is primarily from:",
  ["Exchanges to SEBI", "Hedgers to speculators/investors", "Warehouses to WDRA", "FPIs to farmers"],
  1, "Hedgers lay off price risk; speculators and investors accept that risk hoping to profit. This risk transfer is a core economic function of derivatives.",
  "When a farmer sells futures and a speculator buys them, harvest-price risk moves from the farmer to the speculator.")

C(1, "Price discovery", "Futures price discovery is most efficient when:",
  ["Only one trader knows the information", "Information flows continuously and trading is transparent", "Warehouses are empty", "Options are banned"],
  1, "Efficient discovery needs continuous information, many participants and a transparent order book. Futures then guide producers on timing of sales and planting.",
  "A widely traded chana futures price that updates all day is a better planting signal than an opaque once-a-week mandi rumour.")

C(1, "AIF/PMS", "Which alternative investment category has been permitted in commodity derivative markets?",
  ["Only Category I AIF", "Category III AIF and PMS (subject to conditions)", "Only real-estate AIFs", "Only angel funds"],
  1, "Category III AIFs and PMS may participate in CDMs, widening the investor base and liquidity, subject to SEBI conditions and investor consents.",
  "A Cat III AIF can take a tactical long in energy index futures without running a physical oil inventory.")

C(1, "Delivery notice", "Commodity futures often have a delivery notice period because:",
  ["SEBI forbids cash settlement in all cases", "Physical settlement needs time for logistics, finance and quality checks", "Options cannot expire", "Tick size must change daily"],
  1, "Unlike many financial futures, commodity delivery needs warehouse nomination, assaying, transport and payment arrangements, so sellers give notice in a window.",
  "A short in gold futures intending to deliver must notify within the exchange window so the assigned buyer can arrange funds and vault receipt.")

C(1, "Spot-futures link", "Spot and futures markets are:",
  ["Completely independent", "Different in delivery timing but interrelated through prices", "The same legal contract", "Only linked for agricultural goods"],
  1, "Spot is immediate; futures is later delivery. Prices still influence each other via carry, inventories and arbitrage, and they converge at expiry.",
  "If gold spot jumps on a weak INR, near-month gold futures usually jump the same day.")

C(1, "Electricity", "Monthly electricity futures in India are typically:",
  ["Compulsory physical delivery of power to a factory", "Exchange-traded, standardised and cash-settled", "OTC only", "Reserved for state electricity boards"],
  1, "Electricity futures are standardised, cash-settled contracts on 28/30/31 days of round-the-clock power. They complement the physical electricity market.",
  "A discom can lock a month-ahead power price on the exchange without scheduling a physical plant.")

C(1, "Categories", "Commodities on Indian exchanges are commonly grouped as:",
  ["Only bullion and currency", "Bullion, metals, energy and agriculture", "Only agri and real estate", "Crypto and carbon only"],
  1, "The four usual buckets are bullion (gold, silver), metals (aluminium, copper, zinc, etc.), energy (crude, gas, electricity) and agriculture (spices, oilseeds, etc.).",
  "MCX is known for bullion/energy/metals; NCDEX is known for agri complexes such as guar.")

C(1, "Barter", "The earliest form of commodity trading was:",
  ["SPAN margining", "Barter of goods for goods", "Index options", "CTT collection"],
  1, "Barter exchanged goods with matching opposite needs. Later, metals and then currency became the medium of exchange; then spot and derivatives markets evolved.",
  "Bags of wheat for cattle is barter; selling wheat for rupees is a cash spot trade.")

C(1, "Mandi", "In a traditional mandi, price-setting power often rests mainly with:",
  ["The farmer", "Traders/middlemen inspecting and bidding for produce", "SEBI", "The clearing corporation"],
  1, "Farmers typically have weak bargaining power in physical mandis. eNAM and futures try to improve price discovery and bargaining.",
  "If only three local traders bid in a village mandi, the farmer may realise less than a nationally discovered futures price.")

C(1, "Speculators", "Speculators in commodity futures:",
  ["Must always take or give delivery", "Have no intention of using the physical commodity and seek profit from price moves", "Are prohibited on MCX", "Only hedge farmer output"],
  1, "Speculators accept risk to profit from expected price changes. They provide liquidity to hedgers. They usually square off before delivery.",
  "A trader buying crude futures on a geopolitical headline, with no refinery, is speculating.")

C(1, "Forwards origin", "Futures evolved from forwards mainly to:",
  ["Increase customisation", "Standardise contracts and reduce default risk via the exchange", "Remove all price risk automatically", "Ban speculators"],
  1, "Forwards are flexible but risky. Futures standardise quantity/quality/date and interpose the exchange/clearing corporation.",
  "Instead of a private 73-quintal wheat forward with a neighbour, you trade a standard exchange lot with daily MTM.")

C(1, "CBOT LME", "CBOT was established in 1848 in the USA and LME in 1877 in the UK. They are important because they:",
  ["Regulated Indian mandis", "Were pioneering global commodity exchange institutions", "Invented GST", "Replaced SEBI"],
  1, "CBOT and LME successfully launched organised commodity exchange trading and became global reference markets for grains and metals.",
  "LME aluminium prices still influence Indian metal hedging decisions even when you trade on MCX.")

C(1, "FCRA", "The Parliament passed the Forward Contracts (Regulation) Act to regulate commodity forwards/futures in:",
  ["1875", "1952", "1992", "2015"],
  1, "FCRA 1952 created the pre-SEBI regulatory framework (including FMC). It was repealed in 2015 when SEBI took over.",
  "Between 1952 and 2015, a pepper futures ban or permission would have been an FMC/FCRA matter, not a SEBI circular.")

C(1, "DMA FPI", "As per SEBI’s May 2023 circular, FPIs may:",
  ["Bypass KYC forever", "Have direct market access using broker terminal/infrastructure", "Trade only in cash agri", "Set exchange circuit filters"],
  1, "FPIs can use DMA through broker infrastructure, subject to conditions. They remain within the FPI and ETCD risk framework.",
  "An FPI algo can hit MCX crude through a broker DMA setup rather than phoning every order.")

C(1, "Gold vs inflation", "Gold is often treated as:",
  ["A perfect monsoon derivative", "A hedge against inflation and currency stress", "An agricultural soft commodity", "A WDRA warehouse receipt"],
  1, "Gold historically attracts demand when inflation rises or currencies weaken. That is a price-factor, not a guarantee of returns.",
  "During high CPI and a weak INR, jewellery and investment demand for gold often increases, lifting spot and futures.")

C(1, "News", "Agricultural commodity prices are especially sensitive to news on:",
  ["Only repo rate", "Monsoon and temperature", "Only CTT rates", "Only demat charges"],
  1, "Weather and crop news dominate agri. For metals/energy, mine strikes, hurricanes or geopolitics matter more.",
  "A delayed monsoon forecast can lift soybean and chana futures the same week.")

C(1, "Quality", "Grading is crucial in commodity derivatives because:",
  ["All commodities are identical worldwide", "Contracts must specify quality/certification of the physical good", "Options have no strike", "Indices ignore prices"],
  1, "Unlike a share, wheat or gold must meet stated quality. Premium/discount adjusts for allowed variation.",
  "Castor seed with lower oil content may be deliverable only at a 2% price discount per 1% oil shortfall (as in typical specs).")

C(1, "Transactional efficiency", "Derivatives improve transactional efficiency by:",
  ["Forcing physical delivery every day", "Lowering the cost of transferring risk compared with only using the spot market", "Abolishing warehousing", "Removing CTT"],
  1, "Hedging with a futures margin is cheaper than holding or shorting large physical inventories, which supports investment and growth.",
  "A refiner can hedge 10,000 barrels with futures margin instead of buying and storing all of it today.")

C(1, "Index futures intro", "Commodity index futures trading in India started in:",
  ["2015", "2017", "2020", "2024"],
  2, "Index futures began in 2020. In March 2022 SEBI permitted options on commodity indices.",
  "MCX iCOMDEX futures let a trader take a basket view of energy/metals/bullion without picking one metal.")

C(1, "Ecosystem list", "Which of the following is part of the commodity market ecosystem?",
  ["Only equity brokers in cash market", "WSPs, transporters, assayers, brokers, exchanges, clearing corporations and banks", "Only the Ministry of Corporate Affairs", "Only newspaper ticker services"],
  1, "Goods move from producer to user through storage, quality testing, transport, finance and exchange infrastructure.",
  "A soybean delivery involves warehouse, assayer, eNWR, clearing bank funds and the exchange matching engine.")

C(1, "Hybrid MF", "SEBI allowed Multi Asset Mutual Fund schemes to invest in gold, real estate, etc., expanding commodity-linked investment. This primarily increases:",
  ["Mandatory physical delivery by retail investors", "Institutional participation and liquidity in CDMs", "FCRA powers", "Mandi cess"],
  1, "Institutional products channel household savings into commodity derivatives within scheme rules, adding liquidity for hedgers.",
  "A multi-asset fund buying gold futures is an institutional long that can offset a jewellery exporter’s short hedge.")


# ===== Chapter 2 =====
C(2, "Index idea", "An index is best described as:",
  ["A warehouse licence", "A barometer of how prices/value of a defined basket are moving, usually from a base of 100 or 1000", "A type of CTT", "A clearing bank account"],
  1, "Indices create a proxy for a market so that index return can be treated as market return. Commodity indices in India use nearby futures prices, not equity-style spot market-cap.",
  "If a bullion index starts at 1000 and gold and silver futures rise, the index might print 1080 — an 8% basket move.")

C(2, "Construction", "Indian commodity indices are constructed from:",
  ["Spot mandi prices only", "Prices of nearby futures of constituent commodities", "Equity market capitalisation", "Only option premiums"],
  1, "Unlike equity indices (spot prices/market cap), commodity indices use nearby futures. They are price-based with weights typically fixed for a year.",
  "MCX BULLDEX moves with gold and silver futures, not with jewellers’ displayed making charges.")

C(2, "Weights", "SEBI’s typical production:liquidity weighting mix used by exchanges is around:",
  ["90:10", "50:50", "25:75 (minimum 25% each factor)", "0:100"],
  2, "Weights use Production Value and Liquidity Value scores, commonly 25:75, with at least 25% on each factor. Production value is 5-year average deliverable supply value; liquidity is last-12-month futures volume.",
  "A metal that is produced a lot but barely trades gets less index weight than a highly liquid contract.")

C(2, "Caps", "In a SEBI composite commodity index, each constituent generally has:",
  ["No minimum or maximum", "Minimum 1% and maximum 30% weight", "Minimum 40% weight", "Exactly equal weights"],
  1, "Composite indices: 1%–30% per commodity. Sectoral indices need not apply the 30% cap (exchanges may set their own). MCX also uses a sector cap around 40% on iCOMDEX.",
  "Crude cannot be 50% of a composite index under the 30% cap, but it can be ~50% of an energy sectoral index.")

C(2, "Eligibility", "A constituent futures should generally have existed for at least the last 12 months and traded on:",
  ["10% of days", "50% of days", "90% of trading days in those 12 months", "Only expiry days"],
  2, "Liquidity and continuity tests: 12-month existence and 90% of days traded. For composite indices with derivatives, ≥80% of weight must meet ADTV floors (Rs 75 cr agri / Rs 500 cr non-agri).",
  "A brand-new illiquid spice contract cannot immediately become 25% of a traded composite index.")

C(2, "Roll", "MCX typically rolls index constituent futures over:",
  ["30 days equally", "2 days (about 50% per day)", "One tick only", "Only on Muhurat day"],
  1, "NCDEX historically rolled over 3 days (1/3 each); MCX over 2 days (50% each). Spread trades are ignored in index calculation. Muhurat/special sessions are avoided for rolls.",
  "If gold near-month expires Friday, BULLDEX will blend next-month gold futures across the two roll days.")

C(2, "Index futures specs", "On the start date, commodity index futures have a minimum contract value around:",
  ["Rs 50,000", "Rs 5 lakh", "Rs 5 crore", "Rs 1 only"],
  1, "Base index value is often 1000 and lot size is set so value ≥ Rs 5 lakh (e.g., 500 units × 1000). Tick size is typically Rs 0.25. Lot units stay constant unless rebalancing drops value below the floor.",
  "Index 1200 × 500 units = Rs 6,00,000 contract value.")

C(2, "Hours", "On expiry day, commodity index futures trade only up to:",
  ["11:55 pm", "5:00 pm", "9:00 am", "Midnight"],
  1, "Normal hours match constituents for arbitrage, but expiry day trading in index futures is only until 5:00 pm. FSP uses VWAP of constituents from 4:00 pm to 5:00 pm.",
  "You cannot hold an index future through the late energy session on its expiry day; it is already set for cash settlement after 5 pm.")

C(2, "OI limits futures", "Client-level open position limit in commodity index futures is:",
  ["1% of OI or 100 lots, whichever is lower", "5% of OI or 1,000 lots, whichever is higher", "50% of OI", "Unlimited"],
  1, "Client: 5% of market OI or 1,000 lots, whichever is higher. Member: 15% of OI or 10,000 lots, whichever is higher.",
  "If index futures OI is only 8,000 lots, 5% is 400, so the floor of 1,000 lots applies at client level.")

C(2, "Index options OI", "Client-level open position limit in commodity index options is:",
  ["Same as futures", "Double that of index futures: 10% of OI subject to min 2,000 lots", "Zero for clients", "Only 50 lots"],
  1, "Index option limits are double futures limits in % and lots. Member: 30% of OI, minimum 20,000 lots.",
  "A client could be long 2,000 index option lots even if 10% of OI is smaller, because of the minimum floor.")

C(2, "Index options style", "Commodity index options in India are:",
  ["American and physically delivered", "European-style and cash-settled", "Only weekly like equity", "Unregulated OTC"],
  1, "SEBI (March 2022): European, cash-settled, up to 12 months, at least three strikes. ITM auto-exercised unless contrary instruction; OTM expire worthless. Expiry should not coincide with constituent roll.",
  "A bullion-index call that finishes ITM pays cash; it does not deliver gold bars.")

C(2, "Margins options", "Buyers of commodity index options:",
  ["Pay all SPAN, ELM, SOMM like sellers", "Pay the option premium; sellers face the margin stack", "Never pay anything", "Only pay CTT"],
  1, "Option buyers pay premium. Sellers face SOMM, initial margin, concentration, ad-hoc, ELM, pre-expiry etc. Initial margin is at client portfolio level. No delivery-period margin because cash-settled.",
  "Buying a 100-lot index call costs premium only; writing those calls needs substantial SPAN+ELM.")

C(2, "ADTV fail", "If a commodity fails the minimum ADTV test, its weight in the index should not exceed:",
  ["1%", "15%", "30%", "50%"],
  1, "Illiquid names are capped at 15% so that at least 80% of the index is in liquid ADTV-qualifying contracts.",
  "A thinly traded metal might still sit in a composite index but cannot dominate it.")

C(2, "Uses", "A construction company needing several metals may hedge with:",
  ["Only rainfall options", "Metal index futures as a basket hedge", "Only equity Nifty", "Warehouse KYD"],
  1, "Index futures hedge a diversified exposure when picking every metal future is impractical. Diversification also reduces the impact of one metal’s shock.",
  "A builder long METLDEX futures is protected if copper, zinc and aluminium all rally together.")

C(2, "Monsoon proxy", "Buying an agri index future is economically similar to betting that:",
  ["Monsoon will be excellent and prices will crash", "Supplies may tighten (e.g., deficit monsoon) and agri prices may rise", "USDINR will not move", "CTT will be abolished"],
  1, "Deficit monsoon → lower agri supply → higher prices → long agri index profits. A good monsoon view is often expressed by shorting the agri index.",
  "A food processor fearing a drought can buy agri index futures as a broad raw-material hedge.")

C(2, "BULLDEX", "In a bullion sectoral index such as MCX BULLDEX, gold weight can stay around 60% because:",
  ["Composite 30% cap always applies", "Sectoral indices are not bound by the composite 30% cap", "Gold is an agri commodity", "SEBI bans silver"],
  1, "Sectoral indices may have two names (gold and silver) with large weights. Composite indices cap a single name at 30%.",
  "BULLDEX 2025-style weights are roughly gold ~60% and silver ~40%.")

C(2, "Energy index", "MCX iCOMDEX Energy Index is essentially a basket of:",
  ["Wheat and chana", "Crude oil and natural gas", "Gold and silver", "Copper and zinc"],
  1, "Energy sectoral index is crude and natural gas, each near 50% in recent years (e.g., ~49.85% / 50.15%).",
  "If gas rallies 10% and crude is unchanged, energy index rises about 5%.")

C(2, "AGRIDEX", "NCDEX AGRIDEX was discontinued from 1 February 2022 mainly because:",
  ["SEBI banned all agri indices forever", "Trading in several constituent commodities was suspended", "Tick size became negative", "CTT on agri doubled"],
  1, "When constituents cannot trade, an index of those futures cannot be maintained. Extraordinary rebalancing or discontinuation follows.",
  "GUAREX (guar seed and guar gum) remained as a sectoral agri index example.")

C(2, "Global", "S&P GSCI was originally developed in 1991 by:",
  ["MCX", "Goldman Sachs (later owned by S&P)", "NCDEX", "WDRA"],
  1, "The Goldman Sachs Commodity Index became S&P GSCI in 2007. Other globals: Bloomberg Commodity Index (ex DJ-UBS), Rogers, MSCI, LME Index.",
  "A US pension fund might benchmark commodity exposure to BCOM or S&P GSCI, not to MCX iCOMDEX.")

C(2, "Spread exclusion", "Calendar spread and crush-margin paired trades are ignored in index computation because they are:",
  ["Illegal", "Not bona fide single-side trades", "Always in backwardation", "Only in options"],
  1, "Index valuation wants genuine outright liquidity. Spread legs can distort the printed futures price used for the index.",
  "A 1:1 gold calendar spread print should not revalue BULLDEX as if a large outright gold trade occurred.")

C(2, "Max tenor", "Maximum tenor of a commodity index futures contract shall not exceed:",
  ["1 week", "1 month", "12 months", "10 years"],
  2, "Index futures can be launched for 1, 2, 6 or 12 months, but not beyond 12 months.",
  "You may hedge a one-year commodity-basket view with a 12-month index future, not a 5-year contract.")

C(2, "VaR MPOR", "Initial margin on index futures is based on 99% VaR with MPOR of at least:",
  ["1 hour", "2 days", "30 days", "1 year"],
  1, "Value at Risk at 99% over a minimum 2-day margin period of risk determines initial margin, consistent with CPMI-IOSCO PFMI thinking.",
  "If two-day 99% VaR is 4% of contract value, that is the core initial margin before add-ons.")

C(2, "ETF", "A commodity ETF linked to an index allows investors to:",
  ["Avoid all regulation", "Gain packaged exposure that tracks the basket without selecting each future", "Set MSP", "Replace WDRA"],
  1, "ETFs are listed portfolios. Gold/silver ETFs and potential index ETFs give commodity exposure in securities-market form.",
  "Buying a gold ETF is economically closer to holding gold exposure than to running a jewellery shop.")

C(2, "Inflation proxy", "If METLDEX rises 10% in a year, it roughly indicates:",
  ["Exactly 10% CPI inflation in India", "About 10% price rise in that metal basket (before carry/roll effects)", "A 10% rupee appreciation", "Zero industrial demand"],
  1, "Fixed weights make a sectoral index a crude inflation/price proxy for that family, subject to cost-of-carry and roll.",
  "Copper, zinc, aluminium all up ~10% will lift METLDEX even if CPI food inflation is unchanged.")

C(2, "Rebalancing disclosure", "A newly rebalanced commodity index must be disclosed at least:",
  ["1 day before", "3 months before the new weights apply", "5 years before", "Never"],
  1, "Ordinary rebalancing is at least annually (MCX/NCDEX often calendar year). Disclose at least 3 months ahead. Index level is not reset to 1000 on rebalance.",
  "If 2026 weights are announced in September 2025, the January 2026 index still continues from the old level, just with new weights.")


# ===== remaining conceptual chapters continue in this module via more C() calls
# Chapter 3 conceptual
C(3, "Futures definition", "A commodity futures contract is:",
  ["A gift of goods", "A standardised exchange-traded agreement to buy/sell a specified amount at a future date at a price agreed today", "Always an option", "An unenforceable IOU"],
  1, "Both sides are obligated. Size, grade and date are standardised so every contract is fungible.",
  "MCX gold 1 kg futures for February is the same contract for every trader, unlike a private forward.")

C(3, "Futures vs forwards", "Futures differ from forwards because futures:",
  ["Are OTC and customised", "Are exchange-traded, margined and marked to market daily", "Never need delivery specifications", "Have no price"],
  1, "Futures: standardised, CCP, daily MTM. Forwards: OTC, usually no daily margin, settled at maturity, higher credit risk.",
  "A listed February gold future is MTM tonight; a jeweller’s OTC forward with a bank may wait until February to settle.")

C(3, "Convergence", "On the delivery/expiry date, cost of carry becomes zero and spot and futures prices:",
  ["Diverge infinitely", "Converge", "Are set by CTT", "Must be in contango"],
  1, "Carry costs shrink with time. At expiry, holding the future is economically holding the spot, so prices meet (allowing for location/quality).",
  "A February gold future and Mumbai spot gold should be almost equal on expiry day; otherwise arbitrageurs act.")

C(3, "Contango", "Contango means:",
  ["Futures price < spot price", "Futures price > spot price", "Option premium is zero", "Basis is always positive"],
  1, "Contango: F > S, usually from positive carry. Basis = S − F is then negative. Markets may still go to backwardation due to tightness or seasonality.",
  "Gold spot 1,20,000 and 4-month future 1,24,800 is contango of Rs 4,800.")

C(3, "Backwardation", "Backwardation often appears in agri markets during sowing because:",
  ["Storage cost is infinite", "Harvest later is expected to increase supply, so later futures can sit below current tight spot", "SEBI requires F < S", "Options cannot be used"],
  1, "Spot may be high in the lean season while harvest-month futures discount expected new supply. Convenience yield can also pull F below S+C.",
  "Chana spot may be firm in June while October (post-harvest) futures trade cheaper.")

C(3, "Convenience yield", "Convenience yield is the benefit of:",
  ["Writing naked calls", "Holding the physical commodity rather than only a futures contract", "Paying extra CTT", "Avoiding KYC"],
  1, "Processors value inventory that keeps plants running. Then F = S + C − Y. High Y reduces futures premium and can create backwardation.",
  "A refiner with crude tanks full can keep refining even if a pipeline is disrupted — that comfort is convenience yield.")

C(3, "Advantages", "An advantage of futures over forwards is:",
  ["Complete customisation of every clause", "Elimination of counterparty credit risk through the CCP", "No need for any contract specifications", "Guaranteed profit"],
  1, "Standardisation, access for small and large players, transparent discovery, scientific margining and CCP guarantee are the textbook advantages.",
  "A 2-lot gold hedge by a small jeweller is possible on MCX; a bank may not offer a tiny OTC forward.")

C(3, "Linear payoff", "Commodity futures have a linear payoff, meaning:",
  ["Profit is capped at premium", "P/L moves in proportion to the price change; long and short are mirror images", "P/L is always zero", "Only options are linear"],
  1, "Long P/L = ST − F; short = F − ST. Unlike options, there is no kink at a strike.",
  "Gold up Rs 100/10 g: long 1 kg gains Rs 10,000 and short loses Rs 10,000.")

C(3, "Long short", "'Going long' a futures contract means:",
  ["Selling to deliver", "Buying, committing to purchase at the futures price", "Buying a put", "Placing only GTC orders"],
  1, "Long = buyer. Short = seller. Open short at expiry must deliver eligible stock or face delivery default penalty.",
  "Buy August gold futures at 50,000/10 g: you profit if gold is above that later.")

C(3, "Polling", "Spot price polling compiles prices from empanelled participants. Extreme quotes are handled using:",
  ["Random pick of the highest quote", "Bootstrapping/outlier removal and a least-error type selection around the median", "Only the exchange CEO’s view", "Yesterday’s Nifty close"],
  1, "Exchanges disclose polling method, tax inclusion, outsourcing and participant criteria. NCDEX often shows polls twice a day; prices may be ex-warehouse, cess-in, GST-out.",
  "If 9 of 10 chana polls cluster at Rs 5,100 and one is Rs 7,000, the bootstrap ignores the outlier.")

C(3, "FSP polling", "Final settlement price of futures/options on goods is typically the simple average of polled prices of:",
  ["The last 30 days", "The last 3 days including expiry (E, E-1, E-2)", "Only the first day of the contract", "Only international LME close"],
  1, "FSP = average of last three polling days. If some days are missing, exchanges have fallbacks (available polls, futures trend, last poll).",
  "Expiry Friday polls of Wed, Thu, Fri averaged become the delivery/cash settlement rate.")

C(3, "Tick meaning", "Tick size is:",
  ["The lot size in kg", "The minimum permitted price movement of an order", "The SPAN scenario count", "Always Rs 100"],
  1, "Prices can move only in ticks (e.g., Rs 1 per 10 g gold, Rs 0.05 per kg zinc, Rs 0.25 for index). Tick value = (lot/quotation factor) × tick size.",
  "If gold can be 50,000 or 50,001 but not 50,000.50 per 10 g, tick is Re 1.")

C(3, "MTM", "Daily mark-to-market of futures:",
  ["Is optional for hedgers", "Settles that day’s gain/loss in cash, reducing default risk at expiry", "Is paid only in gold bars", "Applies only to options buyers"],
  1, "DSP (usually last-half-hour VWAP) vs prior DSP/traded price gives MTM. Pay-in/pay-out before next day’s start.",
  "Short gold from 50,000 to close 50,100: pay Rs 100 per 10 g tomorrow morning.")

C(3, "Carry components", "Main components of cost of carry are:",
  ["Only brokerage", "Finance (interest), storage and insurance", "Only CTT", "Only option theta"],
  1, "F ≈ S + C. The futures buyer earns interest on cash and avoids storage, so paying S+C is rational in a normal market.",
  "Financing gold at 12% for 4 months on Rs 1,20,000 is Rs 4,800 of carry.")

C(3, "Fair value rule", "If the traded futures price is below fair value (spot + carry), a buyer needing the goods later is generally better off:",
  ["Buying spot and storing", "Buying the cheap futures", "Writing uncovered calls only", "Avoiding both markets"],
  1, "Cheap futures beat buying spot and paying full carry. If futures are rich, buy spot and carry. Convenience yield may still justify holding inventory.",
  "Fair gold future 52,030 but market 51,500 → lock purchase via futures.")

C(3, "Compounding", "Fair value with compounding m times a year uses:",
  ["F = S − r", "F = S × (1 + r/m)^(m×n)", "F = K + premium", "F = tick × lot only"],
  1, "Annual: (1+r)^n. Periodic: (1+r/m)^(mn). Continuous: S e^(rn). Workbook gold example: 50,000 at 12% monthly for 4 months → Rs 52,030.",
  "Semi-annual m=2; quarterly m=4; monthly m=12.")

C(3, "Algo tick", "A larger tick size generally helps which users more, relative to fine hedging?",
  ["Hedgers needing exact prices", "Algo/speculative traders capturing tick-by-tick moves", "Warehouse assayers", "KYC agencies"],
  1, "Hedgers prefer finer ticks for precise hedges. Higher ticks can suit high-frequency strategies.",
  "Electricity futures tick of Rs 1/MWh is coarse versus a 1-paise agri tick.")

# Chapter 4 conceptual
C(4, "Rights", "The seller of a call option has:",
  ["The right to buy the commodity", "The obligation to sell if the buyer exercises", "The right to cancel CTT", "No possible loss"],
  1, "Call seller must sell at strike if exercised. Put seller must buy at strike. Buyers have rights only; they pay premium.",
  "You sell a 48,000 gold call; if gold is 50,000 you are forced to sell at 48,000.")

C(4, "Style", "Currently permitted commodity options in India (on futures and on goods) are:",
  ["Only American", "European-style (exercise on expiry)", "Bermudan weekly", "Perpetual"],
  1, "European: exercise only on expiry. American would allow any day. Indian commodity options are European.",
  "You cannot exercise an MCX gold option on a random Tuesday before expiry.")

C(4, "ITM call", "A call is in-the-money when:",
  ["Spot/underlying < strike", "Underlying > strike", "Premium = 0", "Delta is necessarily negative"],
  1, "Call ITM: S > K. Put ITM: S < K. ATM: S = K. OTM: the opposite inequality. ITM options are auto-exercised unless contrary instruction.",
  "Gold 50,000, strike 48,000 call is ITM by 2,000.")

C(4, "CTM", "Close-to-the-money (CTM) classification is used for:",
  ["Options on futures only", "Options on goods (typically ATM ± 3 strikes)", "Index futures", "Only equity options"],
  1, "CTM (about 7 strikes if FSP on a strike; 6 if FSP mid-two strikes) matters for options on goods. CTM exercise needs explicit instruction, else they expire. Symbol suffix S = goods, F = futures.",
  "MAIZE20MAY20CE2100S is a European call on maize goods at 2100.")

C(4, "IV floor", "Intrinsic value of an option:",
  ["Can be negative", "Is at least zero; call max(S−K,0), put max(K−S,0)", "Equals vega", "Is paid only by hedgers"],
  1, "IV never negative. Even if WTI futures went negative, option prices stay ≥ 0; puts become deep ITM.",
  "Call K=1170, S=1280 → IV=110. If premium=200, time value=90.")

C(4, "Time value", "Time value equals:",
  ["Strike − spot always", "Premium − intrinsic value", "Delta × gamma", "Only interest rates"],
  1, "PM = IV + TV. ATM/OTM have only TV. TV decays to 0 at expiry (theta). Options are wasting assets.",
  "ATM put premium Rs 400 with IV 0 has time value 400, which will vanish if it stays ATM to expiry.")

C(4, "Long call risk", "Maximum loss for a long call is:",
  ["Unlimited", "Limited to premium paid", "Strike + premium", "Twice the margin"],
  1, "Long options: limited loss (premium), theoretically large gain. Short call: limited gain (premium), unlimited loss.",
  "Pay Rs 500 for a gold call: worst case lose 500 even if gold crashes.")

C(4, "Premium drivers", "An increase in volatility, other things equal, will:",
  ["Lower both call and put premiums", "Raise both call and put premiums", "Affect only futures", "Affect only rho"],
  1, "Higher vol → higher chance of finishing ITM → higher premium for both calls and puts. Longer time also raises premium. Higher rates lift calls and lower puts.",
  "Before a major OPEC meeting, crude option IVs and premiums usually jump.")

C(4, "Greeks", "Delta of a long put is:",
  ["Positive", "Negative", "Always +1", "Undefined"],
  1, "Call delta > 0; put delta < 0. Gamma is change in delta. Theta usually negative for longs. Vega positive for longs. Rho positive for calls, negative for puts.",
  "Gold down Rs 100, a put premium up Rs 40 implies put delta about −0.4.")

C(4, "Models", "Options on futures are typically priced with:",
  ["Only CAPM", "Black-76 (futures-based Black–Scholes variant)", "Only dividend discount model", "WDRA circulars"],
  1, "Black-76 uses F instead of S. Black–Scholes is used for options on goods/spot. Binomial trees (Sharpe 1978) are flexible but heavy.",
  "A gold-futures option uses F of the underlying future in d1/d2, not the jewellery shop price.")

C(4, "Put-call parity", "For ATM options on futures, put-call parity implies:",
  ["Calls always cost twice puts", "Call premium equals put premium", "IV is negative", "Theta is zero always"],
  1, "C − P = (F − K) discounted. If F = K, C = P.",
  "ATM gold futures call at Rs 700 should have the put near Rs 700, else convert via futures.")

C(4, "MSP", "Minimum Support Price for farmers is economically similar to:",
  ["A call sold by farmers", "A put option with strike = MSP, Government as writer", "A calendar spread", "A tick size"],
  1, "Farmers can sell to the Government at MSP if market < MSP — like a put. Government bears the obligation without receiving an option premium.",
  "MSP wheat Rs 2,000: if mandi is 1,800 the farmer ‘exercises’; if mandi is 2,200 he sells in the market.")

C(4, "Devolvement", "On exercise, a long call option on futures becomes:",
  ["Short futures", "Long futures at the strike", "Physical gold automatically in all cases", "A put"],
  1, "Long call → long futures; long put → short futures; short call → short futures; short put → long futures. Devolvement is around 10–13 days before futures expiry. Assignment is fair/non-preferential.",
  "ITM 48,000 gold call buyer wakes up long February gold futures at 48,000.")

C(4, "On goods vs futures", "Options on goods may be costlier than options on futures because:",
  ["Spot is unregulated without DPL and delivery obligations are physical", "Greeks do not exist", "SEBI bans futures options", "IV is always higher by law"],
  1, "Spot can gap without circuit filters; writers face actual goods/payment. Hence extra premium. Goods options also attract delivery-period type margins near expiry.",
  "A maize goods call writer may have to deliver maize, not just a futures position.")

C(4, "Closing", "The most common way to close an option before expiry is:",
  ["Wait for negative premium", "Offset by trading the opposite option", "Ask WDRA to cancel", "Convert to barter"],
  1, "Offset, exercise (at expiry for European), or expire OTM. Offset is used to take TV profits or cut risk.",
  "Buy a crude call at 80, sell it at 140 when IV explodes, without ever exercising.")

C(4, "Commodity vs equity options", "Compared with equity options, commodity options typically:",
  ["Have daily expiries as the main product", "Have monthly expiries and longer market hours (often 9 am to 11:30/11:55 pm)", "Never use Greeks", "Are American only"],
  1, "Equity: 9:15–3:30, weekly/daily expiries common. Commodity: longer hours, monthly, often higher vol, futures-devolution feature.",
  "You can trade a gold option at 10 pm; a stock option cannot.")

C(4, "OI", "Open interest in options is:",
  ["Only today’s traded volume", "Outstanding contracts not yet closed, exercised or expired", "Always equal to volume", "A type of margin"],
  1, "OI shows how many contracts remain open and is a liquidity/participation gauge.",
  "If 1,000 new calls are created, OI rises 1,000; if they are squared, OI falls.")

C(4, "Interest rates", "A rise in interest rates, other things equal, tends to:",
  ["Increase call values and decrease put values", "Decrease both", "Increase only theta", "Have no textbook effect"],
  0, "Higher r raises the forward, helping calls and hurting puts (rho).",
  "Gold call premia may firm slightly if financing rates jump, even if spot is unchanged.")

C(4, "Theta", "Theta is usually negative for long options because:",
  ["Exchanges fine option buyers daily", "Time value erodes as expiry approaches, especially faster near expiry", "Delta cannot change", "IV is illegal"],
  1, "Time decay is not linear; it accelerates into expiry. That structurally favours option sellers if realised vol is tame.",
  "An ATM weekly-style option can lose a large fraction of TV in the last few days.")

# Chapter 5 conceptual
C(5, "Hedging def", "Hedging means taking a derivatives position that is:",
  ["In the same direction as physical exposure to increase risk", "Opposite to physical exposure to reduce price risk", "Always a straddle", "Only for speculators"],
  1, "Spot and futures tend to move together, so opposite positions offset. Residual risk is basis risk.",
  "Own 100 kg silver (long physical) → short silver futures.")

C(5, "Long hedge", "A long hedge is used by someone who:",
  ["Already holds surplus inventory to sell", "Will need to buy the commodity later and fears a price rise", "Only writes calls", "Never uses futures"],
  1, "Natural short (needs to buy later) → buy futures. Natural long (producer) → sell futures (short hedge).",
  "Jeweller needs gold in July: buy August futures today.")

C(5, "Speculation", "A speculator is different from a hedger because the speculator:",
  ["Has matching physical exposure", "Has no commercial underlying exposure and seeks profit from the price bet", "Never pays margin", "Must take delivery"],
  1, "Long speculator expects prices up; short speculator expects prices down. Selective ‘hedging’ based only on a view is effectively speculation.",
  "Buying crude futures with no oil business is a long speculation.")

C(5, "Arbitrage types", "The two broad futures arbitrage types are:",
  ["Only weather vs geopolitics", "Spot vs futures and futures vs futures", "Only options vs CTT", "Only IPO vs FPO"],
  1, "Cash-and-carry if F > S+C: buy spot, sell futures. Reverse if F < S+C: sell spot, buy futures. Inter-month if calendar spread ≠ carry.",
  "Gold fair 50,700, future 51,200 → buy spot, sell future, lock ~500.")

C(5, "Spreads", "Buying an intra-commodity spread means:",
  ["Buy far month and sell near month always", "Buy near month and sell far month (near cheap / far rich)", "Buy two unrelated commodities", "Sell both months"],
  1, "Buy spread: long near, short far. Sell spread: short near, long far. Inter-commodity: related goods (guar seed/gum, soya complex). Crush = beans vs meal/oil; crack = crude vs products.",
  "If October gold is too expensive vs August, sell October and buy August.")

C(5, "Spread margin", "SEBI (March 2023) spread margin benefit can be up to:",
  ["5% always", "75% of initial margin for same underlying; 50% for correlated different commodities (ρ ≥ 0.90)", "100% ELM waiver forever", "Zero"],
  1, "ELM still applies on each leg. Benefit only among first six expiries. Spreads are less volatile than outright, hence lower margin.",
  "A gold Aug–Oct calendar spread posts much less IM than a naked gold long.")

C(5, "Basis def", "Basis is defined as:",
  ["Futures − strike", "Spot − futures", "Premium − delta", "Tick × days"],
  1, "Basis = S − F. Contango ⇒ negative basis. Backwardation ⇒ positive basis. Strengthening: more positive / less negative. Weakening: opposite. Basis → 0 at expiry.",
  "Spot 100, future 150 → basis −50 (contango).")

C(5, "Basis who benefits", "Long hedgers generally benefit if basis:",
  ["Strengthens", "Weakens (futures rise relative to spot)", "Is illegal", "Equals CTT"],
  1, "Long hedge: long futures, short spot. Weakening basis helps them. Short hedgers benefit from strengthening basis. Holding to expiry kills basis risk via convergence.",
  "If you are long futures as a jeweller and futures rally more than spot, your hedge over-performs.")

C(5, "Covered call", "A covered short call combines:",
  ["Short commodity + short call", "Long underlying + short call", "Long put + short futures only", "Two unrelated stocks"],
  1, "Covered call earns premium in a range-bound market and caps upside. Naked short call is speculative. Covered short put: cash ready to buy if put is exercised.",
  "Hold 1 kg gold, sell a slightly OTM call — extra income if gold goes sideways.")

C(5, "Straddle", "A long straddle is:",
  ["Sell call and sell put, same strike", "Buy call and buy put, same strike and expiry", "Buy only futures", "A type of warehouse receipt"],
  1, "Long straddle: big move either way needed to beat two premiums. Long strangle uses OTM strikes, cheaper, needs even larger move. Short straddle/strangle profit from low vol.",
  "Buy 50,000 gold call and put paying 800 total; need gold beyond 50,800 or 49,200 to profit.")

C(5, "Vertical", "A bull call spread is:",
  ["Sell low strike call, buy high strike call", "Buy lower strike call, sell higher strike call", "Buy two puts of same strike", "Short the index only"],
  1, "Net debit, bullish, limited risk and reward. Bear call spread is the reverse (net credit). Horizontal = same strike, different expiry (vega play). Diagonal mixes both.",
  "Buy 50k call, sell 52k call on gold — cheaper than a naked long call.")

C(5, "Index uses", "Index futures can be used for:",
  ["Only physical delivery of every metal", "Hedging, speculation and inter-month arbitrage on the basket", "Avoiding all regulation", "Setting MSP"],
  1, "Construction firms hedge metals via metal index; traders speculate on monsoon via agri index; arb if 2-month index is mispriced vs 1-month plus interest.",
  "If 1-month index 14,175 and 2-month 14,150 with 1% monthly rates, 2-month is cheap — buy 2m, sell 1m.")

C(5, "Disclosure", "SEBI (Nov 2018) requires listed companies to disclose in annual reports:",
  ["Only CEO hobbies", "Commodity risk policy, physical exposure and extent of OTC vs exchange hedges, domestic vs international", "Only CTT paid by employees", "Warehouse CCTV passwords"],
  1, "HUL and RIL style disclosures show % of crude/product exposure hedged and where.",
  "A listed refiner must say how much next year’s crude is hedged on MCX vs ICE/OTC.")

C(5, "Limitations", "A key limitation of hedging is:",
  ["Price risk becomes exactly zero always", "Basis risk, transaction costs and margin cash-flow remain", "Futures cannot be sold", "SEBI forbids producers from hedging"],
  1, "Hedges minimise, not vaporise, risk. Margins can strain cash even when the economic hedge is working.",
  "A farmer short futures may face MTM pay-ins if prices rally before harvest, even though the crop will be worth more.")

C(5, "Option hedge", "A commodity consumer fearing a price spike can hedge by:",
  ["Selling calls only", "Buying calls (or call spreads)", "Selling puts naked without cash", "Avoiding all options"],
  1, "Buyers use calls for upside protection; they may sell puts to lower purchase cost in a stable market. Sellers buy puts; they may sell calls to enhance selling price.",
  "An airline buys crude calls as a fuel-price insurance premium.")

# Chapter 6
C(6, "Members", "A Professional Clearing Member (PCM):",
  ["Executes trades but cannot clear", "Clears others’ trades but does not execute trades itself", "Only assays gold", "Is the same as an AP"],
  1, "TM executes (own/client) and needs a clearer. TCM/SCM executes and clears. PCM (often banks/custodians) only clears.",
  "A small TM routes gold trades to a bank PCM for clearing.")

C(6, "AP", "Authorised Persons must:",
  ["Handle client money in their personal account", "Route all monetary client transactions through the broker and cannot act independently", "Replace SEBI", "Issue contract notes in their own name as exchange members"],
  1, "APs interact with clients under the member. Sub-brokers as a category ended 1 April 2019; they migrated to APs or TMs.",
  "Your local AP can take your gold order but funds go to the broker, not to the AP’s savings account.")

C(6, "Matching", "Screen-based trading matches orders by:",
  ["Broker seniority only", "Price-time priority", "Random lottery", "Largest lot first always"],
  1, "Best price first; then earlier time. Reducing quantity does not lose time priority; changing price does.",
  "A 50,000 gold bid entered at 10:01 trades before a 50,000 bid at 10:02.")

C(6, "HFT", "SEBI’s illustrated HFT order-rate limit is:",
  ["1 order per day", "120 orders per second measured over a rolling 5 seconds", "Unlimited", "Only 2 orders per hour"],
  1, "HFT is latency-sensitive algo. Kill switch is the emergency halt. Low-frequency algos (≤10 OPS) may not need the same registration as >10 OPS HFT algos.",
  "A runaway gold algo hitting 200 orders/sec should be killed automatically.")

C(6, "White vs black box", "Black-box algos:",
  ["Have fully disclosed logic and need no RA registration", "Have undisclosed logic; provider must register as a Research Analyst", "Are banned in all cases", "Are the same as GTC orders"],
  1, "White-box/execution algos are transparent and replicable. Black-box signals are research products.",
  "A VWAP execution algo is white box; a secret ‘AI gold predictor’ sold to clients is black box.")

C(6, "Hours agri", "Domestic agricultural commodities generally trade:",
  ["24×7", "Monday–Friday about 9:00 am to 5:00 pm IST (agri including processed up to 9:00 pm)", "Only on Sundays", "Only after 11:30 pm"],
  1, "Non-agri: ~9:00 am to 11:30/11:55 pm to overlap global energy/bullion. Index futures match constituents except expiry 5 pm.",
  "You can trade crude at 10 pm but not typically chana.")

C(6, "DSP", "Daily Settlement Price is commonly:",
  ["The day’s opening tick", "Volume-weighted average of last half-hour trades (with fallbacks)", "Only polled spot", "The strike of ATM options"],
  1, "DSP is used for MTM. Base price of a new contract is set by the exchange; thereafter previous close/DSP feeds DPL.",
  "If gold’s last 30 minutes average Rs 50,120, that is DSP for tonight’s MTM.")

C(6, "DPL", "Circuit filters / Daily Price Limits:",
  ["Guarantee profits", "Cap the day’s permitted price range and create cooling-off in volatility", "Apply only to IPOs", "Replace margins"],
  1, "Agri broad/narrow: 4% then 6% after 15 minutes. Sensitive agri: 3% then 4%, then halt. Index DPL ≥ single-commodity DPLs in spirit.",
  "Chana up 4% hits a pause; after cooling it may move to 6%.")

C(6, "Orders", "An IOC order:",
  ["Rests all day", "Fills immediately in full or part; unfilled remainder is cancelled; not for algo traders", "Is the same as GTC", "Always becomes a stop"],
  1, "Day orders die at session end. GTD until a date. GTC until cancelled. Stop becomes active after trigger. Trailing stop follows favourable price.",
  "IOC buy 10 lots gold at 50,000: if 4 lots available, 6 cancel.")

C(6, "IRRA", "Investor Risk Reduction Access (IRRA) lets individual investors:",
  ["Open new speculative positions during a broker outage", "Square off or cancel pending orders when the TM has a technical disruption", "Avoid KYC", "Change tick size"],
  1, "IRRA is a joint-exchange safety valve for individuals, not for initiating fresh risk.",
  "If your broker’s terminal dies while you are long crude, IRRA can help you flatten.")

C(6, "Glitch", "Brokers must inform exchanges of a technical glitch within:",
  ["1 hour, preliminary report T+1, RCA within 14 days", "1 month", "1 year", "Never"],
  0, "1 hour intimation, T+1 preliminary incident report, 14-day root-cause analysis.",
  "A 2-hour trading outage at 11 am must be flagged to the exchange by noon.")

C(6, "Selection", "A commodity is more suitable for futures if it has:",
  ["Tiny unstandardisable supply and rigid government price freeze", "Large marketable surplus, volatility, storability, homogeneity and limited excessive controls", "Only one buyer nationally", "Negative tick size"],
  1, "SEBI approval is needed to launch or withdraw a contract. Options on futures need ADTV ≥ Rs 100 cr agri / Rs 1,000 cr others on that exchange.",
  "Wheat with huge surplus and standard grades is a better futures candidate than a tiny perishable herb with no grades.")

C(6, "Contract mods", "Category C contract specification changes (e.g., DPL, settlement rate) require:",
  ["Only a tweet", "Prior SEBI approval", "No notice", "Only warehouse consent"],
  1, "Cat A (symbol, tick): exchange with 10 days’ notice. Cat B (expiry, delivery centre): internal committee. Cat C: SEBI prior approval.",
  "Changing gold’s settlement methodology is not a casual website edit.")

C(6, "CTT futures", "CTT on sale of commodity futures is:",
  ["0.05% on buyer", "0.01% on seller", "1% on both", "Exempt for all metals"],
  1, "Futures sale 0.01% seller. Option sale 0.05% of premium (seller). Exercise with delivery 0.0001% purchaser; cash exercise 0.125% purchaser. Unprocessed agri exempt.",
  "Sell 1 kg gold future at Rs 49,80,000 → CTT Rs 498.")

C(6, "FPO", "Farmer Producer Organisations mainly use commodity derivatives to:",
  ["Speculate overnight in crude", "Hedge harvest selling prices (sell futures or buy puts)", "Issue EGRs", "Act as PCMs"],
  1, "FPOs can sell harvest-month futures at sowing or buy puts, locking farm-gate realisation.",
  "A soybean FPO sells October futures in June while crop is in the field.")

C(6, "MF limits", "Mutual funds in commodity derivatives generally cannot:",
  ["Use hybrid/multi-asset/gold ETF routes at all", "Take positions in sensitive commodities or in the options segment, or run net shorts", "Hold any gold exposure", "Use index futures ever"],
  1, "MF participation is restricted: no sensitive commodities, no options, no net short. PMS/AIF have their own conditions.",
  "A hybrid fund may hold gold futures long, not a short option book on chana.")

C(6, "LES", "Liquidity Enhancement Scheme (2019) is meant to:",
  ["Ban market makers", "Incentivise market makers to quote new/illiquid commodity contracts", "Increase CTT", "Close warehouses"],
  1, "LES pays for continuous two-way quotes so new contracts can discover prices.",
  "A new electricity future may need LES quotes until natural liquidity appears.")

C(6, "Staggered", "SEBI reduced the minimum staggered delivery period to:",
  ["30 days", "3 days (circular May 24, 2024)", "1 hour", "1 year"],
  1, "During staggered delivery, parties can intend delivery; assigned buyers typically take delivery on T+2 at the centre. Random allocation of buyers.",
  "A 3-day window before expiry can be used to give gold delivery rather than waiting for the last tick.")

C(6, "Impact cost", "A wider bid–ask spread implies:",
  ["Higher liquidity and lower impact cost", "Lower liquidity and higher impact cost", "Zero SPAN", "Compulsory delivery"],
  1, "Impact cost = difference between actual trade price and ideal mid for a given size.",
  "Gold with 1-tick spread is cheaper to enter/exit than an illiquid spice with a huge spread.")

C(6, "Bhav copy", "Bhav copy is:",
  ["A KYC form", "The exchange’s daily closing price file/disclosure", "A warehouse assay", "An STR to FIU"],
  1, "Exchanges also disclose OI (including top participants), warehouse stocks and polled spots.",
  "Downloading MCX bhav copy gives official closing prices for back-office MTM.")

# Chapter 7 conceptual
C(7, "Novation", "Novation by the clearing corporation means:",
  ["Trades become illegal", "CCP becomes buyer to every seller and seller to every buyer", "Warehouses disappear", "Margins are optional"],
  1, "Clearing nets obligations; settlement transfers goods vs funds (DVP). Funds net at member level; commodity ownership nets at client and is grossed at member.",
  "Your gold buy is versus the CCP, not versus the anonymous opposite client.")

C(7, "Compulsory vs both-option", "In a both-option delivery contract, delivery happens when:",
  ["Always, for every open position", "Both buyer and seller opt to give/take delivery; else cash settle at DDR", "Never", "Only FPIs opt"],
  1, "Compulsory delivery (e.g., gold): remaining OI delivers. Both-option: need matching intentions; otherwise cash at due date rate.",
  "If you stay long compulsory gold into expiry, expect to pay and receive metal.")

C(7, "Quality PD", "If gold of 0.999 purity is delivered on a 0.995 contract, the buyer typically:",
  ["Pays a discount", "Pays a premium scaled by 999/995", "Pays nothing", "Receives a penalty automatically"],
  1, "Premium/discount adjusts quality. Example: 25,000 × 999/995 = 25,100.50. Castor: 1% oil drop → 2% price discount.",
  "Better metal than spec → seller earns premium; worse (within band) → discount.")

C(7, "Seller default agri", "Seller delivery-default penalty on agri futures is:",
  ["0.01% only", "4% of settlement price + replacement cost (with prescribed sharing to SGF, CC and buyer)", "100% of lot", "Only a warning letter"],
  1, "At least 1.75% to SGF, up to 0.25% to CC, balance (2% + replacement) to buyer. Non-agri seller default: 3% + replacement (buyer gets 1% + replacement).",
  "Defaulting on chana delivery is far costlier than a normal MTM day.")

C(7, "Buyer default", "Buyer delivery default penalty (from May 2021) is:",
  ["Unlimited always", "Leviable based on seller’s loss, capped within delivery margins collected from the defaulting buyer", "Zero by law", "Paid to FIU"],
  1, "Protects non-defaulting sellers. Staggered assignment still requires the tagged buyer to perform.",
  "If you are allocated gold delivery and do not pay, penalty can be taken from your delivery margins.")

C(7, "Risk types", "Principal risk is eliminated by CCP novation. It is the risk that:",
  ["Volatility exists", "You delivered/paid but did not receive the other leg", "Monsoon fails", "Theta decays"],
  1, "Counterparty risk = replacement cost (pre-settlement) + principal (settlement). Systemic risk is cascade default. Operational = people/process/systems. Legal = unenforceability.",
  "Paying for gold and not getting the eNWR is principal risk — the CCP’s job to stop.")

C(7, "Open position", "Client-level open position in a commodity is:",
  ["Buy + sell", "Net of buy vs sell for that client; member level grosses the higher of buy/sell across clients", "Always zero", "Equal to warehouse stock"],
  1, "Member limit is often ~10× client numeric limit. Position limits fight corners.",
  "Client long 8, short 3 → open 5. Member sums such client exposures gross.")

C(7, "SGF IPF", "Minimum required corpus of commodity derivatives SGF is:",
  ["Rs 10 lakh", "Rs 10 crore (SEBI, July 11, 2018)", "Rs 10,000", "Zero"],
  1, "SGF backstops residual settlement risk. IPF funds education/awareness and client claims on member default; funded by penalties (other than settlement) and 1% of turnover fee.",
  "If a member fails after margins, SGF is the next line; IPF is for investor compensation/education, not routine MTM.")

C(7, "SPAN", "SPAN initial margin looks at:",
  ["Only today’s close vs open", "A set of 16 risk scenarios on price and volatility to estimate maximum likely loss", "Only CTT", "Only warehouse rent"],
  1, "IM via 99% VaR; ELM often ~1% on gross OI. Peak margin (2020) uses intra-day snapshots (four) so you cannot under-margin intra-day.",
  "A short crude option might show large SPAN because a +3σ jump hurts the writer.")

C(7, "Additional vs special", "Additional margin is levied on both sides to cool high OI; special margin is levied:",
  ["Also always on both sides", "On one side to counter one-sided momentum", "Only on index options buyers", "Only after 5 years"],
  1, "Concentration margin targets clients with outsized OI share, not everyone.",
  "A runaway short-covering rally may get a special margin on the buy side.")

C(7, "Tender margin", "Tender/delivery period margin is typically:",
  ["Zero", "3% + 5-day 99% VaR of spot, or 20%, whichever is higher", "Only Rs 1", "Equal to CTT"],
  1, "Extra IM in last 5–10 days. Lean-period agri margins can add up to ~7% on pre-harvest volatility.",
  "Sitting in gold into delivery week needs much more cash than a first-day position.")

C(7, "SOMM devolvement", "Devolvement margin on options-on-futures is charged:",
  ["Only to buyers, 100% on E-10", "Equally (1/3 each) on E-2, E-1 and E to both sides", "Never", "Only in cash agri"],
  1, "Prepares both sides for futures IM after devolvement. SOMM applies to option writers using minimum volatility scan ranges (agri 5/6/7%, non-agri 4/5/6%). Options on goods use delivery-period margins on ITM/CTM in last 3–5 days; options on futures do not.",
  "Two days before gold option expiry you start posting futures-like margin in thirds.")

C(7, "ARMF", "Alternate Risk Management Framework activates if prices fall more than 50% in 20 days (or negative-price measures abroad). Then pre-expiry margins:",
  ["Fall to zero", "Rise by 5% each day in the last five trading days", "Are replaced by CTT", "Apply only to farmers"],
  1, "ARMF is the post-WTI-negative playbook so longs cannot walk away from crashing commodities.",
  "If a metal crashes 50% in three weeks, expect escalating pre-expiry IM.")

C(7, "Bills", "The seller’s delivery bill is raised at:",
  ["Each party’s original traded price", "Final Settlement Price, inclusive of GST; prior gaps already went through MTM", "Option strike only", "Yesterday’s DSP always"],
  1, "Even if you bought gold at 49,000 and FSP is 50,000, the bill is at FSP; you already received MTM along the way.",
  "Think of FSP invoice + daily MTM as adding back to your true economic price.")

C(7, "CSCRF", "SEBI’s Cyber Security and Cyber Resilience Framework (2024) is built around five goals:",
  ["Buy, sell, hold, pledge, gift", "Anticipate, withstand, contain, recover, evolve", "SPAN, ELM, MTM, SOMM, ARMF", "KYC, KRA, UCC, PAN, RDD"],
  1, "Applies to SEBI REs including MIIs (exchanges, depositories, CCs, KRAs, QRTAs), phased from 1 Jan 2025.",
  "A broker must be able to contain a ransomware hit and restore trading access — not only write an SOP.")

C(7, "WSP", "Exchange-empanelled agri warehouses must be WDRA-registered. SEBI’s indicated WSP net-worth band is about:",
  ["Rs 10 lakh–50 lakh", "Rs 10 crore–50 crore", "Rs 1,000 only", "Unlimited negative net worth"],
  1, "WSPs store deliverable goods, do KYD, and need assay/NABL-or-BIS-linked testing. NERL and CDSL repository connectivity for e-NWRs.",
  "A fly-by-night godown without net worth cannot be an MCX/NCDEX delivery warehouse.")

C(7, "Alerts", "Online surveillance typically alerts as utilisation hits:",
  ["10% only", "70%, 85%, 90%, 95% of limits, then may deny further trading", "Only after bankruptcy", "Randomly once a year"],
  1, "Real-time exposure vs margin/position caps. Capital adequacy excludes many illiquid/intangible items from net worth.",
  "At 95% of gold position limit, new longs may be blocked.")

C(7, "Cross margin", "Cross-margin benefit of up to 75% is available between:",
  ["Unrelated equity and agri", "Commodity index futures and constituent futures (or variants)", "Two KRAs", "CTT and GST"],
  1, "Index vs underlyings are economically offsetting, so IM can be reduced like calendar spreads.",
  "Long BULLDEX and short gold+silver futures in index weights can receive cross-margin.")

C(7, "Index FSP", "Index futures FSP is based on constituent VWAP between:",
  ["9–9:15 am", "4:00 pm and 5:00 pm on expiry, after 5 pm determination", "11:30–11:55 pm", "Sunday auction"],
  1, "Cash settled next morning vs prior DSP. No physical metals are delivered on the index.",
  "Energy components’ 4–5 pm trades feed iCOMDEX expiry.")

C(7, "Running account", "Brokers must settle client running accounts:",
  ["Never", "Monthly or quarterly as per client mandate", "Once in 10 years", "Only if profit exceeds Rs 1 cr"],
  1, "Stops idle client cash sitting with brokers. Margins release on square-off/expiry; delivery margins after final settlement.",
  "If you choose monthly, surplus above margin should come back each month.")

# Chapter 8
C(8, "Three tier", "The three-tier commodity market framework is:",
  ["WDRA, GSTN, FIU", "Central Government (policy), SEBI (regulation), Exchanges (front-line)", "RBI, IRDAI, PFRDA only", "States, panchayats, mandis only"],
  1, "Spot agri is a State List subject; derivatives as securities are Union List. FCRA repealed 28 Sep 2015; erstwhile FMC merged into SEBI. CDMRD later merged into Market Regulation Department. Single-exchange equity+commodity from 1 Oct 2018. Broking integration circular Sep 2017.",
  "SEBI writes the rulebook; MCX/NCDEX police the trading day; Government lists which goods can be derivatives.")

C(8, "SCRA securities", "Under SCRA, securities include derivatives, MF units, government securities and, from December 2021:",
  ["Only cryptocurrencies", "Electronic Gold Receipts (EGR)", "Mandi cess receipts", "Rainfall only"],
  1, "Options in goods are also securities (s.2(h)). Security receipts under SARFAESI and CIS units are securities; ULIPs are not. ADB/IFC onshore rupee bonds were declared securities.",
  "An EGR is legally a security, though trading has been slow on tax issues; vaults via SEBI Vault Managers Regulations 2021 with NSDL/CDSL.")

C(8, "18A", "Section 18A of SCRA makes a derivative legally valid only if it is:",
  ["Signed on plain paper between friends", "Traded on a recognised stock exchange and settled through its clearing house", "Approved by a village panchayat", "Mentioned in a WhatsApp group"],
  1, "OTC commodity futures that pretend to be exchange contracts are not legally protected under 18A. This is why dabba trading is dangerous and illegal.",
  "A ‘gold future’ with a local bucket-shop has no 18A cover.")

C(8, "SEBI Act", "SEBI Act, 1992 empowers SEBI to protect investors, develop and regulate the market, and among other things:",
  ["Print currency", "Register brokers, prohibit fraud, inspect/audit, promote SROs and adjudicate penalties (s.15)", "Set MSP for wheat", "Repeal the Constitution"],
  1, "Jurisdiction covers issuers, intermediaries and persons associated with securities markets, including commodity brokers, warehouses in the ecosystem, etc.",
  "SEBI can inspect a commodity broker and levy monetary penalties for KYC or contract-note failures.")

C(8, "SECC", "SECC Regulations, 2012 govern:",
  ["Only mutual fund advertisements", "Recognition and operations of stock exchanges and clearing corporations, including commodity CCs", "Only income-tax slabs", "Only FPO elections"],
  1, "SEBI amended SECC so exchanges guarantee settlement including good delivery. Demutualisation/corporatisation sits here: separate ownership, management and trading rights.",
  "NCDEX’s clearing corporation must meet SECC net-worth and governance norms.")

C(8, "Bye-laws", "Exchange bye-laws:",
  ["Can ignore SEBI", "Are made under SCRA with SEBI oversight; material/Category C changes need SEBI approval", "Are oral only", "Apply only to farmers"],
  1, "Exchanges are SROs/front-line regulators but SEBI can make/amend bye-laws, call returns, supersede governing boards, suspend business, and stop undesirable speculation.",
  "MCX cannot secretly rewrite gold delivery rules without the SEBI process.")

C(8, "Master circular", "The commodity derivatives master circular cited in the workbook updates is dated:",
  ["4 August 2023", "1 January 2000", "15 August 1947", "31 March 1992"],
  0, "SEBI Master Circular 4 Aug 2023 compiles segment circulars. Individual circulars still matter (FPI, index options March 2022, peak margin, etc.).",
  "When in doubt on a process, look at the latest master circular plus later amending circulars.")

C(8, "Turnover fee", "SEBI turnover fee on commodity derivatives is:",
  ["Rs 15 per crore (0.00015%) non-agri and Rs 1 per crore agri, with agri fee-forgone going to a farmers/FPO fund", "10% of premium", "Equal to GST", "Paid only by WDRA"],
  0, "Agri regulatory fee is largely forgone into a dedicated development fund. This is separate from CTT and stamp duty.",
  "Rs 1 crore of gold futures turnover → Rs 15 SEBI fee (passed through the chain).")

C(8, "LODR", "Listed-company commodity hedging disclosures sit under:",
  ["Only the Factories Act", "SEBI LODR, plus RBI expecting banks to push commodity borrowers to hedge", "Only state APMC Acts", "Only FEMA compounding"],
  1, "Annual reports must show policy, exposure and hedge percentages, domestic vs international, OTC vs exchange.",
  "A listed edible-oil company must disclose palm-oil hedge cover.")

C(8, "EFE", "Eligible Foreign Entities may:",
  ["Freely speculate in all Indian agri options without exposure", "Hedge Indian commodity exposures in Indian ETCDs under prescribed conditions", "Regulate MCX", "Issue eNWRs"],
  1, "EFEs need underlying Indian commodity exposure. FPIs later got a broader cash-settled non-agri route.",
  "A foreign cotton merchant with Indian procurement can hedge on Indian exchanges as EFE, subject to rules.")

C(8, "KRA", "KYC Registration Agencies maintain central KYC. Examples include:",
  ["Only FMC", "CVL, NDML, DotEx, CAMS Investor Services, etc.", "Only WDRA", "Only rural co-ops"],
  1, "KRA Regulations 2011. Members upload KYC within 10 days of document receipt.",
  "Once you are in a KRA, a new commodity broker can fetch KYC instead of a full paper redo.")

C(8, "Recognition", "Organised trading in securities including commodity derivatives can take place only on:",
  ["Any Telegram channel", "Recognised stock exchanges complying with SEBI conditions", "Village weekly haats", "Unregistered dabba"],
  1, "SCRA recognition is the gateway. Listing/contract launch still needs SEBI-conformant criteria.",
  "If an entity is not a recognised exchange, its ‘futures’ are not exchange-traded derivatives.")

C(8, "Integration", "From October 1, 2018, SEBI permitted:",
  ["FCRA revival", "Commodity derivatives and other securities segments on a single exchange", "Ban on gold futures", "Removal of clearing corporations"],
  1, "NSE/BSE could offer commodities; MCX/NCDEX path to other segments also opened in the integration era. Brokers could be unified after Sep 2017 circular.",
  "You may see commodity and equity derivatives on one membership and one clearing relationship.")

C(8, "Inspection", "SEBI’s inspection and information-calling powers:",
  ["Stop at equity brokers", "Extend to commodity exchanges and associated persons/intermediaries", "Apply only to unlisted firms", "Were deleted in 2015"],
  1, "Unified regulator after FMC merger. Powers include audit of SEs, MFs and associated persons.",
  "A commodity warehouse-related intermediary in the SEBI perimeter can be inspected.")

C(8, "Undesirable speculation", "Position limits, DPLs and margins are legally anchored in the power to:",
  ["Print eNWRs", "Prohibit undesirable speculation in securities including commodity derivatives", "Set GST rates", "Appoint village patwaris"],
  1, "SCRA lets Government/SEBI curb harmful speculation while still allowing legitimate hedging and liquidity.",
  "Sensitive agri extras (tighter DPL, lean margin) come from this policy toolkit.")

# Chapter 9
C(9, "ICAI 2021", "ICAI’s revised Guidance Note on derivatives (2021) is effective for periods beginning on or after:",
  ["1 April 2013", "1 April 2021", "1 January 1992", "28 September 2015"],
  1, "All derivatives on balance sheet at fair value (exit price). Applies to Indian GAAP (AS) entities, not the separate Ind AS model. Covers FX, equity and commodity derivatives whether or not used as hedges.",
  "A private company using AS that is long gold futures must show the MTM asset/liability, not hide it off-balance-sheet.")

C(9, "Hedge types", "The three hedge-accounting types are:",
  ["SPAN, ELM, MTM", "Fair value, cash flow and net investment hedges", "Call, put and straddle", "TM, TCM, PCM"],
  1, "Fair value hedge: both instrument and hedged item hit P&L immediately. Cash flow hedge: effective MTM in equity (CF hedge reserve) then recycle. Net investment: foreign operation FX. Firm commitments are usually FV hedges; highly probable forecasts are CF hedges. FX firm commitments may be either.",
  "Hedging next season’s copper sales with short futures is typically a cash-flow hedge of a forecast sale.")

C(9, "Effectiveness", "Retrospective hedge effectiveness must usually fall in:",
  ["0–10%", "80–125%", "200–300%", "Exactly 50%"],
  1, "Prospective test: expect almost full offset. Retrospective: 80–125% (dollar offset etc.). Ineffectiveness hits P&L. Documentation and board-approved policy required at inception.",
  "If inventory rose 100 and the short future gained 70, 70% is too low — hedge accounting may fail.")

C(9, "Options accounting buyer", "Premium on a purchased call that is exercised into goods is typically:",
  ["Ignored", "Added to the cost of the asset acquired", "Always treated as a capital reserve", "Paid to SEBI as fee"],
  1, "Purchased options are assets. Lapse → expense premium. Put exercise: premium reduces sale proceeds. Written options: premium income in P&L; contingent liability until expiry. Devolvement into futures folds premium into futures cost basis rather than a separate lapse expense.",
  "Pay Rs 2 lakh for a copper call, exercise, buy copper: copper inventory cost includes that premium.")

C(9, "CTT who", "CTT on futures and on option sales is paid by the seller; on option exercise it is paid by the:",
  ["Clearing corporation only", "Purchaser (exercising buyer)", "WDRA", "Always the farmer"],
  1, "Unprocessed agri derivatives exempt; processed agri, metals, energy are in the net. Finance Act 2013 introduced CTT; 2018 brought options on futures fully in. Aggregated per client on contract notes.",
  "You sell a gold option: 0.05% CTT on premium. If the buyer exercises to delivery, buyer pays 0.0001%.")

C(9, "Stamp", "From 1 July 2020, stamp duty on commodity derivative trades is levied uniformly at:",
  ["Rs 2 per Rs 1 lakh (0.002%) of value, collected via exchanges", "10% of profit", "Rs 500 flat per year", "Zero nationally"],
  0, "Exchange collects from brokers and remits to the state where the buyer is registered — a uniform regime replacing patchy state rules.",
  "Rs 1 lakh gold futures notional → Rs 2 stamp.")

C(9, "GST brokerage", "GST on brokerage and exchange/clearing fees is:",
  ["5%", "12%", "18%", "28%"],
  2, "18% GST on brokerage and trading/clearing fees. Physical delivery GST is on the goods at FSP. GST subsumed excise, VAT, octroi/mandi tax but not mandi cess or customs duty. Intra-state: CGST+SGST; inter-state: IGST. Exchanges operationally collect CGST+SGST at settlement; inter-state delivery can create registration issues.",
  "Rs 1,000 brokerage → Rs 180 GST. Delivering zinc to another state may need IGST compliance beyond the exchange’s CGST/SGST path.")

C(9, "Speculative derivatives", "Derivatives held for trading (not hedge accounting) are:",
  ["Kept off balance sheet", "Current assets/liabilities at fair value, gains/losses in P&L", "Always equity reserves", "Treated as share capital"],
  1, "No CF reserve. Full MTM volatility hits profit. Classification as current because they are trading.",
  "A prop desk long crude futures books daily MTM in the income statement.")

C(9, "AS 2", "In a fair value hedge of inventory, AS 2 still carries inventory at lower of cost and NRV, while:",
  ["Hedge accounting adjustments are shown separately so the hedged risk is visible", "Inventory is deleted", "Futures are ignored", "Only CTT is capitalised"],
  0, "Workbook example: copper inventory FV hedge — derivative MTM and inventory hedge adjustment both go to P&L, inventory note shows the hedge adjustment separately from AS 2 carrying amount.",
  "Copper cost 100, NRV 100, hedge adj +8, derivative liability 8 — P&L matches.")

C(9, "CTT agri", "Unprocessed agricultural commodity derivatives are:",
  ["Taxed at 1% CTT", "Exempt from CTT", "Taxed only on Mondays", "Subject to STT not CTT"],
  1, "Processed agri (sugar, guar gum, soya oil) and all metal/energy attract CTT. The exemption is a farmer/agri-market policy choice.",
  "Chana futures sale typically has no CTT; gold futures sale does.")

C(9, "SEBI fee agri fund", "The SEBI turnover fee forgone on agricultural commodities is:",
  ["Returned to brokers as bonus", "Put in a dedicated fund for farmers/FPOs", "Paid as CTT", "Used as option premium"],
  1, "Rs 1 per crore agri vs Rs 15 non-agri, difference channelled to farmer participation initiatives.",
  "Higher chana turnover still feeds the agri development fund rather than SEBI’s general fee.")

C(9, "Contract note CTT", "CTT for a day is determined by aggregating:",
  ["Only option buys", "Sell transactions at contract level per client code, shown on the contract note", "Warehouse rents", "Only MTM losses"],
  1, "The TM’s contract note is the legal tax document for that day’s CTT.",
  "Three gold future sells in a day appear as one aggregated CTT line on the note.")

C(9, "CF reserve recycle", "Cash-flow hedge reserve is reclassified to P&L when:",
  ["The CEO retires", "The forecast transaction occurs and affects profit (e.g., sales happen)", "Tick size changes", "SPAN is updated"],
  1, "Until then, effective MTM sits in equity. Disclosures include reserve reconciliation and instruments’ fair values.",
  "March MTM on a September copper sales hedge stays in OCI/equity until September invoices.")

# Chapter 10
C(10, "Integrity", "SEBI’s broker code requires high integrity and forbids:",
  ["Best-price execution", "Manipulative/fraudulent trades, rumour-spreading and creating a false market", "Issuing contract notes", "KYC"],
  1, "Skill, care, diligence; no churning for brokerage; no false quotes; suitable advice; do not refuse small clients merely for low volume.",
  "Pushing a retiree into 50 lots of crude to earn brokerage violates the code.")

C(10, "Contract note", "Electronic contract notes require:",
  ["No consent", "Prior client consent (agreement or separate)", "Only a phone call after 1 year", "SEBI chairperson’s signature"],
  1, "Notes without delay, in exchange format. Disclose if acting as principal vs agent; manage conflicts; do not prefer own interest.",
  "You must opt-in to ECN; otherwise expect physical/email as per rules.")

C(10, "Confidentiality", "Client personal/investment information:",
  ["May be sold to anyone", "Must not be disclosed or misused", "Must be posted on social media", "Belongs to authorised persons personally"],
  1, "Breach of trust is a code violation. July 2021 collateral segregation: one client’s securities cannot margin another.",
  "A broker cannot pledge Client A’s gold ETF to cover Client B’s crude MTM.")

C(10, "Public advice", "Before giving investment advice in public media, a broker/employee must:",
  ["Hide all holdings", "Disclose interest including family/employer long-short in that security", "Only use WhatsApp status", "Pay extra CTT"],
  1, "Applies to real-time and recorded media. Social handles must show registered name and registration number, including at the start of videos.",
  "Tweeting ‘buy silver’ while the firm is max long silver without disclosure is a violation.")

C(10, "KYC", "UCC and PAN upload is mandatory; exchanges must not allow trades without UCC. Aadhaar for KYC is:",
  ["The only allowed OVD", "Voluntary; other OVDs include passport, voter ID, driving licence, NREGA card", "Banned", "Required every hour"],
  1, "Documents: KYC, member-client agreement, RDD. IPV/video-KYC (Apr 2020). Upload to KRA in 10 days. May 23, 2025 accessibility: PwD-friendly liveliness, guardian where needed.",
  "A client with passport and address proof can open a commodity account without Aadhaar.")

C(10, "RDD", "By signing the Risk Disclosure Document the client acknowledges:",
  ["Guaranteed profits", "Awareness of price, liquidity, basis, counterparty, tech and delivery/quality risks", "That margins are optional", "That dabba trading is recommended"],
  1, "Members may refuse clients who will not sign RDD, who default, or who starve margins. They may levy extra margin by risk category (low/medium/high).",
  "RDD is not a prospectus of returns; it is a warning that you can lose more than initial margin.")

C(10, "STR", "Suspicious transactions (reversals, profit transfer, dabba-linked) must be reported to FIU. Tipping off the client is:",
  ["Mandatory", "Illegal", "A KYC shortcut", "Required on the contract note"],
  1, "AML master circular (e.g. 15 Oct 2019). Enhanced due diligence for non-face-to-face, common-parameter multiple accounts, dormant reactivation, unexplained transfers.",
  "If two clients swap profits via matched trades, file STR — do not WhatsApp them a warning.")

C(10, "SCORES", "After approaching the member/exchange, unresolved complaints go to SEBI SCORES, where the entity must resolve/ATR within:",
  ["21 days of SEBI intimation", "5 years", "1 hour always", "Never"],
  0, "SCORES gives a registration number. Next step is ODR/SMARTODR: conciliation 21 days (+10 with consent), then arbitration. Award payment in 15 days. Challenge intent under s.34 in 7 days; if no stay in 3 months, comply.",
  "Wrong gold execution → member → exchange → SCORES → SMARTODR conciliation/arbitration.")

C(10, "Voice", "Dealing-room orders should go on recorded lines kept at least for the arbitration complaint window. Client funds:",
  ["May fund proprietary trades freely", "Must not be used for proprietary trades", "Belong to authorised persons", "Are exempt from running-account rules"],
  1, "Daily margin and ledger statements are a member duty. Explain GST on delivery. Members need not square last-day positions without instruction (important if FSP gaps from last trade).",
  "Your idle cash cannot fund the broker’s own crude prop book.")

C(10, "Dos donts", "Investors in commodity derivatives should NOT:",
  ["Trade via registered members after reading specs", "Share internet-trading passwords, deal in cash, or participate in dabba trading", "Keep collateral acknowledgements", "Check SMS/email contract confirmations"],
  1, "Do: registered members only, understand contracts, analyse, keep proofs, query mismatches. Don’t: rumours, luring ads, reversal/profit-transfer trades, delivery default.",
  "If someone offers ‘MCX rates in cash at a tea stall’, that is dabba — illegal.")

C(10, "Defaulting clients", "A broker must not deal for a client who has failed commitments with another broker. Unauthorised PMS by the broker:",
  ["Is encouraged", "Makes the broker responsible for resulting client losses", "Is a WDRA function", "Needs no disclosure"],
  1, "Also cooperate with other brokers on corporate-action type rights where relevant; do not advertise except as exchange permits.",
  "Running an informal ‘I will manage your gold futures’ book without PMS registration shifts loss liability onto the broker.")

C(10, "FX risk", "An exporter hedging only the commodity price but not USDINR still faces:",
  ["No risk at all", "Foreign-exchange risk on dollar-priced goods", "Only theta risk", "Only warehouse risk"],
  1, "Most commodities are dollarised. Hedge both price and currency if you invoice/pay in FX. Liquidity risk: some contracts are hard to exit.",
  "A basmati exporter short rice futures but long an unhedged dollar receivable can still lose on a rupee move.")

C(10, "Last day square-off", "A member has the right, not the duty, to avoid last-day square-off without client instruction because:",
  ["FSP can differ sharply from last traded price due to spot polling", "Margins are illegal on expiry", "Options cannot devolve", "UCC is optional that day"],
  0, "Auto-square at last tick can harm a client if FSP (polled spot average) is away from the future’s last trade. Better to take explicit instructions.",
  "Gold future last trade 50,000 but 3-day poll FSP 49,200 — blind square-off at 50,000 is not the true expiry economics.")

C(10, "Complaints language", "Investor complaints may be filed in:",
  ["English only", "English, Hindi or a regional language, signed, without fee; anonymous/frivolous ones are not entertained", "Only Latin", "Only through newspapers"],
  1, "First the exchange of the member, then SEBI. No fee. Sequence protects both sides.",
  "A Tamil complaint to the exchange is valid; a fake anonymous email may be ignored.")

C(10, "Client rights", "Clients can complain about servicing even without a money claim, and they have access to:",
  ["Only civil court immediately, never SCORES", "Member, exchange and SEBI/ODR grievance systems", "Only WDRA for all issues", "Only income-tax appeals"],
  1, "Rights include fair access to redress. Obligations include margins, delivery/payment, truthful KYC updates, GST invoices when they are delivering.",
  "Delayed contract notes can be a SCORES item even if the trade itself made money.")

# Extra conceptual fillers so smaller chapters stay unique across 5 papers
C(6, "Limit order", "A buy limit order is typically placed:",
  ["Above the best ask to chase the market", "At or below the price the buyer is willing to pay, often below the prevailing ask", "Only after expiry", "Without a price"],
  1, "Limit = specified price. Buy limits sit at or below willingness-to-pay; sell limits at or above. Market orders take the opposite best quote immediately.",
  "Gold ask 50,020: a 50,000 buy limit waits; a market buy lifts 50,020.")

C(6, "Stop loss", "A stop-loss order remains passive until:",
  ["The broker feels like it", "The trigger price is breached, after which it becomes active", "KYC is renewed", "SPAN is recalculated overnight only"],
  1, "Stops limit damage if price goes against you. Trailing stops ratchet only in the favourable direction.",
  "Long gold at 50,000 with sell stop trigger 49,400: if traded last is 49,390 the stop activates.")

C(6, "Compulsory gold", "Gold futures are a classic example of:",
  ["Cash-settled index options", "Compulsory delivery contracts", "Both-option maize only", "Unregulated forwards"],
  1, "Open gold positions into expiry are meant to be physically settled through accredited vaults, not optionally abandoned.",
  "Stay short 1 kg gold to expiry → you must deliver eligible gold or default.")

C(6, "Lot size", "Lot size is:",
  ["Always 1 gram", "The minimum tradable/deliverable quantity of the contract", "The tick size", "The option strike"],
  1, "P/L and margins scale with lots. Cash-settled contracts still define a notional quantity.",
  "Zinc 5,000 kg lot with Re 1/kg move = Rs 5,000 per lot.")

C(6, "FPI energy", "FPI participation is primarily seen in cash-settled:",
  ["Turmeric options on goods", "Non-agri such as crude oil and natural gas (and related indices)", "Only electricity in mandis", "Only eNWRs"],
  1, "Sensitive agri is ring-fenced. Energy cash-settled contracts fit the FPI pathway.",
  "An FPI book is more likely in MCX crude than in a small agri options-on-goods name.")

C(6, "PMS goods", "If a PMS comes into physical possession of goods for a client it must:",
  ["Store forever as a proprietary asset", "Dispose of them at the earliest within agreed timelines", "Deliver to SEBI’s office", "Convert them to EGRs compulsorily the same minute"],
  1, "PMS is an investment service, not a trading house sitting on metal. Client agreement and risk disclosure are mandatory.",
  "If a silver future devolves to delivery in a PMS, the manager liquidates the metal per mandate rather than running a vault business.")

C(6, "Cat III AIF", "Category III AIF commodity participation requires:",
  ["No investor communication", "Existing-investor approval and an exit route for dissenters (as prescribed)", "RBI banking licence", "A seat on the exchange board"],
  1, "SEBI widened products but protected old investors who did not sign up for commodity risk.",
  "A 2018 Cat III fund adding gold futures in 2020 needed consent/exit mechanics.")

C(6, "Algo LFA", "Algos at or below 10 orders per second are treated as:",
  ["Always illegal", "Low-frequency and generally without the HFT-style unique-ID registration burden", "PCMs", "Warehouse RPs"],
  1, ">10 OPS high-frequency algos need registration through the broker and a unique exchange ID.",
  "A simple time-sliced 2 OPS gold TWAP is LFA; a 50 OPS sniper is HFT.")

C(6, "IM ballpark", "Under ordinary conditions, many commodity contracts have initial margin around 4% and ELM around:",
  ["50%", "1%", "25%", "0%"],
  1, "VaR IM (~4%) + ELM (~1%) is the textbook ‘about 5%’ starting point before special/tender/lean add-ons.",
  "Rs 50 lakh gold notional × 5% ≈ Rs 2.5 lakh core margin.")

C(6, "Member vs client OI", "Member-level numeric open-position limits are normally about:",
  ["Equal to one client", "10 times the client-level numeric limit", "1000 times", "Zero"],
  1, "Stops a member warehouse of clients from becoming a hidden corner while still allowing a franchise.",
  "Client cap 1,000 lots → member cap ~10,000 lots in that illustration.")

C(8, "Spot vs futures jurisdiction", "Spot trade in agricultural commodities is primarily a:",
  ["Union List/SEBI exclusive subject", "State List subject, while commodity derivatives as securities are Union/SEBI", "Municipal tax only", "IRDAI subject"],
  1, "This split is why mandis and APMC rules can differ by state even though MCX/NCDEX rules are national.",
  "A state can redesign mandi fees; it cannot rewrite SEBI gold futures law.")

C(8, "FMC", "The Forward Markets Commission:",
  ["Still regulates gold futures in 2026", "Was the erstwhile commodity-futures regulator merged into SEBI on 28 September 2015", "Is a warehouse repository", "Collects GST"],
  1, "FCRA repeal + FMC merger created one securities-market regulator for equity and commodity derivatives.",
  "Pre-2015 pepper circulars were FMC; post-2015 they are SEBI.")

C(8, "Broker regs", "Stock-broker registration and conduct in the commodity segment are under:",
  ["Only the Stamp Act", "SEBI (Stock Brokers) Regulations", "Only the Factories Act", "Only WDRA bye-laws"],
  1, "Net worth, membership categories and the code of conduct live here after FCRA’s repeal.",
  "A commodity TM must hold a SEBI broker registration, not an FMC licence.")

C(8, "SRO", "Exchanges act as self-regulatory organisations when they:",
  ["Print currency", "Set member eligibility, inspect members and levy penalties inside SEBI’s framework", "Appoint the Finance Minister", "Fix MSP"],
  1, "SEBI Act asks SEBI to promote SROs. Front-line policing is the exchange; appellate/oversight is SEBI.",
  "NCDEX can suspend a member for margin default under bye-laws, subject to SEBI norms.")

C(8, "ULIP", "Unit-linked insurance policies are:",
  ["Included as securities under SCRA just like MF units", "Excluded from SCRA’s securities definition (unlike MF/CIS units)", "Commodity futures", "eNWRs"],
  1, "The exam likes this exception: MF units are securities; ULIPs are insurance products outside that list.",
  "A ULIP with a gold fund is still an IRDAI policy, not an MCX contract.")

C(8, "MF 2019", "SEBI circulars of May 2019 are important because they:",
  ["Banned all gold ETFs", "Allowed Mutual Funds and PMS into commodity markets with restrictions", "Reintroduced FCRA", "Made CTT zero"],
  1, "Powers came from SEBI Act + SCRA. Restrictions (no net short, no sensitive agri, etc.) still apply.",
  "Hybrid funds adding gold futures after 2019 rely on that circular.")

C(8, "Supersede board", "If needed, the Central Government/SEBI can:",
  ["Never touch exchange boards", "Supersede the governing body of a recognised stock exchange", "Only change tick size", "Only collect CTT"],
  1, "Nuclear governance option under SCRA when an exchange acts against public interest.",
  "A captured exchange board ignoring investor safety can be superseded.")

C(8, "Options in goods legal", "Options in goods are inside SCRA’s securities definition, which:",
  ["Keeps them outside SEBI", "Brings commodity options on physical goods inside SEBI’s jurisdiction", "Converts them into deposits", "Makes them American-style automatically"],
  1, "Distinct from options on futures (financial derivatives on a futures underlying).",
  "A maize goods option is a security under s.2(h), hence a SEBI product.")

C(8, "Periodical returns", "Under SCRA, periodical returns from stock exchanges can be called by:",
  ["Any Twitter user", "The Central Government (powers exercisable in the SEBI framework)", "Only WSPs", "Only FPOs"],
  1, "Transparency tool alongside inspections and bye-law approvals.",
  "SEBI can demand turnover, default and surveillance returns from MCX.")

C(8, "Good delivery guarantee", "SECC amendments emphasise that exchanges/CCs must guarantee settlement including:",
  ["Only cash MTM, never metal", "Good delivery of the commodity where applicable", "Only option premium", "Only CTT"],
  1, "Investors rely on the CCP not merely for rupees but for quality-certified goods.",
  "If a seller fails, the CC’s guarantee chain (margins, SGF) is meant to make the buyer whole.")

C(10, "Churning", "A broker must not encourage trades solely to:",
  ["Hedge a genuine exposure", "Generate brokerage/commission", "Meet KYC", "Issue RDD"],
  1, "Suitability beats product-push. False or misleading advice to induce trades is prohibited.",
  "Ten round-trips in natural gas in an hour for a conservative hedger is classic churning.")

C(10, "Small investors", "Brokers must faithfully seek best available price and must not refuse clients merely because of:",
  ["Default history", "Low volume / small ticket size", "Missing PAN", "Unsigned RDD"],
  1, "Defaults, missing KYC or refused RDD are valid refusal grounds; snobbery about lot size is not.",
  "A 1-lot gold hedge from a small jeweller must be accepted if otherwise eligible.")

C(10, "Principal vs agent", "When dealing with a client the broker must disclose whether it is acting as:",
  ["WDRA or FCI", "Principal or agent", "SEBI or RBI", "Assayer or transporter"],
  1, "Conflicts must be told; client interest cannot be treated as inferior.",
  "If the desk is filling you from its proprietary book, that principal capacity should be clear.")

C(10, "Risk categories", "Clients are commonly bucketed as low/medium/high risk using:",
  ["Only their zodiac sign", "Location, business, volumes, payment manner and financial status; high-risk names get enhanced monitoring", "Only the last trade’s tick", "Only CTT paid"],
  1, "Default history pushes monitoring up. This is KYC/AML, not a credit score for fun.",
  "A high-turnover, cash-intensive, non-face-to-face client is not ‘low risk’.")

C(10, "Dormant", "Sudden activity in a long-dormant account is a classic trigger for:",
  ["Automatic unlimited leverage", "Enhanced due diligence / possible STR", "Waiver of RDD", "Free options"],
  1, "Together with unexplained inter-account transfers and cloned-parameter accounts.",
  "An account quiet for 3 years that suddenly day-trades 200 crude lots needs a look.")

C(10, "ODR types", "SMARTODR can take up:",
  ["Only criminal insider-trading prosecutions in sessions court", "Service issues, trade disputes, fee disputes and specified compliance/ethics complaints in the MII framework", "Only monsoon insurance", "Only income-tax appeals"],
  1, "It is the securities-market digital dispute rail connected to SCORES, with conciliation then arbitration.",
  "Unauthorised crude trades in your account are an ODR trade dispute.")

C(10, "Member rights", "Members may refuse transactions if the client has:",
  ["Asked for a contract note", "Prior defaults or margin shortfalls", "Signed the RDD", "A PAN"],
  1, "They may also ask AML documents and extra margin by profile. They can decline a client who will not sign RDD.",
  "A client who bounced MTM twice last month can be locked from new gold risk.")

C(10, "Client GST", "When a client is on the selling side of physical delivery, the client must:",
  ["Never raise tax invoices", "Raise GST invoices / fulfil tax delivery obligations as required", "Pay CTT to WDRA", "Cancel UCC"],
  1, "Exchange settlement at FSP does not erase the client’s GST paperwork, especially inter-state.",
  "Delivering zinc to a tagged buyer in another state is a taxable supply by the client.")

C(10, "Advertisement", "Public advertising of brokerage business is:",
  ["Always allowed in any form", "Restricted unless permitted by the stock exchange", "Mandatory hourly on TV", "Only via dabba shops"],
  1, "Stops misleading ‘guaranteed commodity returns’ campaigns.",
  "A ‘double your money in crude’ hoarding without exchange permission is offside.")

C(10, "Associated persons", "Associated persons of SEBI-registered intermediaries who deal with clients must be:",
  ["Unqualified volunteers", "Qualified/certified as required (NISM etc.)", "Only farmers", "Exempt from UCC"],
  1, "This exam itself is the knowledge benchmark for approved users/sales personnel in commodity derivatives.",
  "A dealer punching gold orders needs the Series XVI certificate, not just a cousin in the mandi.")


def rs(n, d=0):
    v = round(float(n), d)
    if d == 0:
        v = int(round(v))
        return f"Rs {v:,}"
    return f"Rs {v:,.{d}f}"


def uniq_options(correct, others, formatter=None):
    fmt = formatter or (lambda x: x if isinstance(x, str) else str(x))
    items = [correct] + list(others)
    labels = []
    seen = set()
    for it in items:
        lab = fmt(it) if not isinstance(it, str) else it
        if lab in seen:
            continue
        seen.add(lab)
        labels.append(lab)
    i = 1
    while len(labels) < 4:
        extra = fmt(correct + i) if not isinstance(correct, str) else f"{correct} ({i})"
        if extra not in seen:
            labels.append(extra)
            seen.add(extra)
        i += 1
    labels = labels[:4]
    # shuffle deterministically later; keep correct at 0 for now
    return labels, 0


def shuffle_opts(options, answer, salt):
    paired = list(enumerate(options))
    r = Rng(sum(ord(ch) for ch in salt) + 17)
    for i in range(len(paired) - 1, 0, -1):
        j = r.randint(0, i)
        paired[i], paired[j] = paired[j], paired[i]
    new_opts = [p[1] for p in paired]
    new_ans = [p[0] for p in paired].index(answer)
    return new_opts, new_ans


class Rng:
    def __init__(self, seed):
        self.n = seed % (2**31 - 1)

    def next(self):
        self.n = (1103515245 * self.n + 12345) & 0x7FFFFFFF
        return self.n

    def choice(self, seq):
        return seq[self.next() % len(seq)]

    def randint(self, a, b):
        return a + self.next() % (b - a + 1)


def numericals_for_set(set_id):
    """Unique numericals for one paper, tagged by chapter."""
    r = Rng(1600 + set_id * 97)
    out = []

    def add(ch, topic, q, correct, wrongs, expl, example, fmt=None):
        opts, ans = uniq_options(correct, wrongs, fmt)
        opts, ans = shuffle_opts(opts, ans, f"{set_id}-{topic}-{q[:40]}")
        out.append(Q(ch, topic, q, opts, ans, expl, example))

    # --- Ch2 index numericals ---
    idx = r.choice([1000, 1080, 1125, 1200, 1275, 1340, 1410, 1550]) + set_id
    lots = [400, 450, 500, 550, 600][set_id - 1]
    val = idx * lots
    add(2, "Index contract value",
        f"A commodity index is at {idx} and the lot size is {lots} units. What is the contract value?",
        val, [idx + lots, idx * 100, lots * 1000],
        f"Contract value = index level × lot size = {idx} × {lots} = {val:,}. SEBI’s design keeps start-date value at least around Rs 5 lakh.",
        f"If the index later moves to {idx + 50}, value becomes {(idx + 50) * lots:,}.",
        lambda x: rs(x))

    tick = 0.25
    tval = lots * tick
    add(2, "Index tick value",
        f"Index futures lot size is {lots} units and tick size is Rs {tick:.2f}. Tick value per contract is:",
        tval, [tick, lots, lots * 0.05],
        f"Tick value = lot size × tick = {lots} × {tick} = Rs {tval:.2f}.",
        "A 4-tick move is therefore Rs " + f"{4 * tval:.2f} per lot.",
        lambda x: rs(x, 2) if isinstance(x, float) and not float(x).is_integer() else rs(x))

    # client OI floor illustration
    oi = r.choice([5500, 7200, 9000, 14000, 22000, 31000]) + set_id * 150
    five = 0.05 * oi
    client_lim = max(five, 1000)
    add(2, "Index position limit",
        f"Open interest in a commodity index future is {oi:,} lots. Client-level limit is 5% of OI or 1,000 lots, whichever is higher. The client limit is:",
        int(client_lim), [int(five) if five != client_lim else 1000, 15 * oi // 100, 2000],
        f"5% of {oi:,} = {five:,.0f}. Compare with the 1,000-lot floor. Limit = max({five:,.0f}, 1,000) = {int(client_lim):,}.",
        "Member limit would be max(15% of OI, 10,000 lots).",
        lambda x: f"{int(x):,} lots")

    # --- Ch3 futures P/L, tick, carry, fair value ---
    for k in range(3):
        entry = r.choice([45000, 48000, 50000, 52000, 55000, 61000, 72000]) + set_id * 40 + k
        move = r.choice([-4000, -2500, -1200, -800, 900, 1500, 2200, 3500, 5000])
        exitp = entry + move
        long = (k % 2 == 0)
        lot, quot = 1000, 10  # gold 1 kg quoted per 10 g
        mult = lot / quot
        pl = (exitp - entry) * mult if long else (entry - exitp) * mult
        side = "buys (goes long)" if long else "sells (goes short)"
        add(3, "Futures profit/loss" if pl >= 0 else "Futures loss",
            f"A trader {side} one gold futures contract of 1 kg, quoted per 10 grams, at {rs(entry)}. The price moves to {rs(exitp)}. Net P/L on the contract is (profit positive, loss negative):",
            int(pl), [int(-pl), int(move), int(move * 100), int((exitp - entry) * 10)],
            f"{'Long' if long else 'Short'} P/L = ({'exit − entry' if long else 'entry − exit'}) × (lot/quotation) = ({exitp if long else entry} − {entry if long else exitp}) × {int(mult)} = {rs(pl)}.",
            f"Each Rs 1 move per 10 g on a 1 kg contract is Rs 100. A Rs {abs(move):,} move is therefore Rs {abs(move)*100:,} per kg.",
            lambda x: rs(x))

    # tick gold
    # tick gold only in set 1; other sets use a unique metal example
    if set_id == 1:
        add(3, "Tick value",
            "Gold futures: lot 1 kg (1,000 g), quotation per 10 g, tick Rs 1 per 10 g. Tick value per contract is:",
            100, [1, 10, 1000],
            "Tick value = (lot/quotation factor) × tick = (1000/10) × 1 = Rs 100.",
            "Zinc example in the workbook style: 5,000 kg lot, quote per kg, tick Rs 0.05 → tick value Rs 250.",
            lambda x: rs(x))
    else:
        glot = 1000
        gtick = set_id  # Rs 1,2,3,4
        add(3, "Tick value",
            f"Gold futures: lot 1 kg (1,000 g), quotation per 10 g, tick Rs {gtick} per 10 g. Tick value per contract is:",
            glot / 10 * gtick, [gtick, 10 * gtick, 1000],
            f"Tick value = (1000/10) × {gtick} = Rs {int(glot/10*gtick)}.",
            "If tick were Re 1, tick value would be Rs 100 per kg lot.",
            lambda x: rs(x))

    zlot = r.choice([4000, 5000, 6500, 10000]) + set_id * 100
    ztick = r.choice([0.05, 0.10, 0.25, 0.50])
    zv = zlot * ztick
    add(3, "Tick value",
        f"A base-metal future has lot size {zlot:,} kg, is quoted per kg, and tick size is Rs {ztick:.2f}. Tick value is:",
        zv, [ztick, zlot, zlot / 10],
        f"Tick value = {zlot:,} × {ztick} = {rs(zv)}.",
        f"A 6-tick favourable move earns {rs(6 * zv)} per lot.",
        lambda x: rs(x))

    # simple cost of carry months
    spot = r.choice([80000, 100000, 120000, 125000, 150000]) + set_id * 250
    rate = r.choice([0.09, 0.10, 0.12, 0.15])
    months = r.choice([2, 3, 4, 6])
    carry = spot * rate * (months / 12)
    fut = spot + carry
    add(3, "Cost of carry",
        f"Spot price of gold is {rs(spot)} per 10 g. Cost of carry is {rate*100:.0f}% per annum. Fair  {months}-month futures price using simple carry F = S + S×r×t is:",
        fut, [spot, carry, spot * (1 + rate)],
        f"C = {spot:,} × {rate:.2f} × {months}/12 = {rs(carry)}. F = S + C = {rs(fut)}.",
        "Workbook gold: 1,20,000 at 12% for 4 months → carry 4,800 → F = 1,24,800.",
        lambda x: rs(x))

    # 90/365 storage + interest
    s2 = r.choice([2000, 2500, 3000, 4000, 5000]) + set_id * 15
    ir = r.choice([0.06, 0.07, 0.08])
    stc = r.choice([0.01, 0.02, 0.015])
    days = r.choice([90, 60, 120, 180])
    fin = s2 * ir * (days / 365)
    sto = s2 * stc * (days / 365)
    coc = fin + sto
    fv = s2 + coc
    add(3, "Cost of carry",
        f"Spot {rs(s2)}, interest {ir*100:.0f}% p.a., storage {stc*100:.1f}% p.a., holding {days} days (365-day year). Total cost of carry is approximately:",
        round(coc, 2), [round(fin, 2), round(sto, 2), round(s2 * ir, 2)],
        f"Finance = {s2}×{ir}×{days}/365 = {fin:.2f}. Storage = {s2}×{stc}×{days}/365 = {sto:.2f}. Carry = {coc:.2f}. Fair value would be {fv:.2f}.",
        "Workbook: 2,500 at 6% + 1% storage for 90 days → carry 43.14, fair 2,543.14.",
        lambda x: rs(x, 2))

    add(3, "Fair futures value",
        f"Using the previous style of inputs, fair futures value = spot + carry. Spot {rs(s2)} and carry {rs(round(coc,2),2)} give fair value:",
        round(fv, 2), [s2, round(coc, 2), round(s2 - coc, 2)],
        f"Fair value = {s2} + {coc:.2f} = {fv:.2f}.",
        "If the market future is below this, prefer buying futures rather than buying spot and storing.",
        lambda x: rs(x, 2))

    # monthly compounding
    s3 = r.choice([40000, 50000, 55000, 60000]) + set_id * 80
    r3 = 0.12
    m = 12
    n = 4 / 12
    f3 = s3 * (1 + r3 / m) ** (m * n)
    add(3, "Fair futures value",
        f"Gold spot {rs(s3)} per 10 g. Financing 12% p.a. compounded monthly. Fair value of a 4-month future is closest to:",
        round(f3), [round(s3 * (1.12) ** (4 / 12)), round(s3 * 1.12), round(s3 * math.exp(0.12 * 4 / 12))],
        f"F = S(1+r/m)^(m n) = {s3}×(1.01)^4 = {s3}×{1.01**4:.6f} ≈ {round(f3):,}.",
        "Workbook: 50,000 → Rs 52,030. Continuous compounding on the same data is about Rs 52,040.",
        lambda x: rs(x))

    # semi annual
    s4 = r.choice([30000, 38000, 42000, 48000]) + set_id * 90
    f4 = s4 * (1 + 0.12 / 2) ** (2 * 1)
    add(3, "Fair futures value",
        f"Spot {rs(s4)}, 12% p.a. compounded semi-annually. Fair value of a 1-year future is closest to:",
        round(f4), [round(s4 * 1.12), round(s4 * (1.03) ** 4), round(s4 * math.exp(0.12))],
        f"F = {s4}×(1.06)^2 = {s4}×1.1236 ≈ {round(f4):,}.",
        "38000 × 1.1236 = 42,697 (workbook-style 42,696.80).",
        lambda x: rs(x))

    # continuous
    s5 = r.choice([50000, 52000, 45000]) + set_id * 70
    f5 = s5 * math.exp(0.12 * 4 / 12)
    add(3, "Fair futures value",
        f"Spot {rs(s5)}, 12% p.a. continuously compounded. 4-month fair futures price is closest to:",
        round(f5), [round(s5 * (1.01) ** 4), round(s5 * 1.04), round(s5 * math.exp(0.12))],
        f"F = S e^(r n) = {s5} × e^0.04 ≈ {s5} × 1.04081 ≈ {round(f5):,}.",
        "Workbook 50,000 continuous 4-month = Rs 52,040.",
        lambda x: rs(x))

    # convenience yield
    s6 = r.choice([6000, 6500, 7000])
    c6 = r.choice([400, 500, 600])
    y6 = r.choice([200, 300, 350])
    f6 = s6 + c6 - y6
    add(3, "Fair futures value",
        f"Spot {rs(s6)}, cost of carry {rs(c6)}, convenience yield {rs(y6)}. Futures price F = S + C − Y is:",
        f6, [s6 + c6, s6 - y6, s6 + y6],
        f"F = {s6} + {c6} − {y6} = {f6}. High convenience yield reduces the futures premium and can even create backwardation.",
        "Guar seed farmer example: convenience of holding inventory can exceed storage cost.",
        lambda x: rs(x))

    # --- Ch4 options numericals ---
    call_pairs = [
        (1280, 1170, 200),
        (1350, 1250, 180),
        (50000, 48000, 500),
        (51200, 50000, 700),
        (49800, 50500, 420),
        (2100, 2000, 150),
        (7200, 7000, 260),
    ]
    for i in range(2):
        S, K, prem0 = call_pairs[(set_id + i * 2) % len(call_pairs)]
        S += set_id * 3 + i
        K += set_id * 2
        prem = prem0 + set_id * 5 + i * 7
        iv = max(S - K, 0)
        if prem < iv + 10:
            prem = iv + 40 + set_id
        tv = prem - iv
        add(4, "Option intrinsic value",
            f"Call option: spot/underlying {rs(S)}, strike {rs(K)}, premium {rs(prem)}. Intrinsic value is:",
            iv, [max(K - S, 0), prem, tv],
            f"Call IV = max(S−K, 0) = max({S}−{K}, 0) = {iv}. Time value = premium − IV = {prem} − {iv} = {tv}.",
            "Workbook style: S 1280, K 1170, PM 200 → IV 110, TV 90.",
            lambda x: rs(x))
        add(4, "Option time value",
            f"Using the same call (S {rs(S)}, K {rs(K)}, premium {rs(prem)}), time value is:",
            tv, [iv, prem, max(K - S, 0)],
            f"TV = {prem} − {iv} = {tv}. ATM/OTM calls have IV 0 so entire premium is time value, which decays to 0 at expiry.",
            "If this call expires with S still equal to today’s S, remaining TV becomes 0 and only IV (if any) is paid.",
            lambda x: rs(x))

    put_pairs = [(45000, 48000), (47000, 50000), (51000, 50000), (49000, 52000), (1280, 1350)]
    S, K = put_pairs[set_id % 5]
    S += set_id * 40
    K += set_id * 25
    put_iv = max(K - S, 0)
    prem = put_iv + 200 + set_id * 35
    add(4, "Option intrinsic value",
        f"Put option: underlying {rs(S)}, strike {rs(K)}, premium {rs(prem)}. Intrinsic value is:",
        put_iv, [max(S - K, 0), prem, prem - put_iv],
        f"Put IV = max(K−S, 0) = {put_iv}. Time value = {prem - put_iv}.",
        "If gold is 50,000 and you own a 48,000 put, IV is 0 (OTM).",
        lambda x: rs(x))

    be = [(48000, 500), (50000, 650), (2100, 90), (7200, 180), (1250, 75)][set_id - 1]
    K, p = be
    add(4, "Call breakeven",
        f"A call buyer pays premium {rs(p)} with strike {rs(K)}. The breakeven underlying price at expiry is:",
        K + p, [K - p, K, p],
        f"Call breakeven = strike + premium = {K} + {p} = {K + p}. Above this, the long call is in net profit. The short call’s breakeven is the same price.",
        "Gold strike 48,000 + premium 500 → BE 48,500. At 50,000 the buyer nets 1,500.",
        lambda x: rs(x))
    add(4, "Put breakeven",
        f"A put buyer pays premium {rs(p)} with strike {rs(K)}. The breakeven underlying price at expiry is:",
        K - p, [K + p, K, p],
        f"Put breakeven = strike − premium = {K} − {p} = {K - p}. Below this, the long put is in net profit.",
        "Strike 48,000, premium 500 → BE 47,500. If expiry is 50,000 the put expires and the buyer loses only 500.",
        lambda x: rs(x))

    # net payoff long call
    ST = K + r.choice([1500, 2000, 2500, -2000])
    gross = max(ST - K, 0)
    net = gross - p
    add(4, "Call breakeven",
        f"Long call strike {rs(K)}, premium {rs(p)}, settlement {rs(ST)}. Net P/L of the buyer is:",
        net, [gross, -p, ST - K - 2 * p],
        f"Exercise value = max({ST}−{K}, 0) = {gross}. Net = {gross} − {p} = {net}.",
        "Unlimited upside, loss cannot exceed premium.",
        lambda x: rs(net) if x == net else rs(x))

    # --- Ch5 hedge, basis, arb, spread ---
    for _ in range(2):
        rho = round(r.choice([0.76, 0.80, 0.90, 0.93, 0.85]) - set_id * 0.01, 2)
        ss = r.choice([3.56, 7.60, 4.20, 5.00, 6.40])
        sf = r.choice([3.63, 8.35, 4.50, 5.50, 6.10])
        hr = rho * (ss / sf)
        add(5, "Hedge ratio",
            f"Correlation between spot and futures is {rho:.2f}. SD of spot changes is {ss:.2f} and of futures changes is {sf:.2f}. Hedge ratio is closest to:",
            round(hr, 3), [round(rho * sf / ss, 3), round(ss / sf, 3), round(rho, 3)],
            f"HR = ρ × (σs/σf) = {rho:.2f} × ({ss:.2f}/{sf:.2f}) = {hr:.3f}.",
            "Workbook: 0.93 × 3.56/3.63 = 0.912.",
            lambda x: f"{x:.3f}" if isinstance(x, float) else str(x))

    qty = r.choice([1800, 2400, 3600, 50, 80]) + set_id * 10
    if qty > 200:
        lot = r.choice([10, 20, 50, 100])
        unit = "kg"
    else:
        lot = 5
        unit = "MT"
    hr2 = r.choice([0.90, 0.912, 0.80, 0.75])
    nct = (qty * hr2) / lot
    add(5, "Hedge ratio",
        f"Physical exposure is {qty} {unit}, futures lot size is {lot} {unit}, hedge ratio is {hr2}. Optimal number of futures contracts is closest to:",
        round(nct), [round(qty / lot), round(qty * hr2), round(lot / hr2)],
        f"Contracts = (quantity × HR) / lot = ({qty} × {hr2}) / {lot} = {nct:.2f} → {round(nct)} contracts.",
        "Smriti-style: 2000 kg, lot 10 kg, HR 0.90 → 180 lots, not 200.",
        lambda x: f"{int(x)} contracts" if float(x).is_integer() or abs(x - round(x)) < 1e-6 else f"{x}")

    pairs = [(5100, 5300), (48000, 50000), (1200, 1150), (72000, 70100), (4050, 4180)]
    sp, fp = pairs[(set_id + r.randint(0, 4)) % 5]
    sp += set_id * 5
    fp += set_id * 8
    basis = sp - fp
    add(5, "Basis",
        f"Spot is {rs(sp)} and futures is {rs(fp)}. Basis (spot − futures) is:",
        basis, [fp - sp, sp + fp, fp],
        f"Basis = {sp} − {fp} = {basis}. Negative basis is contango; positive is backwardation.",
        "If basis moves from −50 to −40 it has strengthened (become less negative).",
        lambda x: rs(x))

    b1 = [-50, -40, 20, 15, -25][set_id - 1]
    b2 = [-40, -30, 12, 8, -8][set_id - 1]
    if b2 == b1:
        b2 = b1 + 10
    stronger = b2 > b1
    add(5, "Basis",
        f"Basis changes from {b1} to {b2}. This is described as:",
        "Strengthening of basis" if stronger else "Weakening of basis",
        ["Convergence to option premium", "A change in tick size", "Strengthening of basis" if not stronger else "Weakening of basis"],
        "Strengthening = basis more positive or less negative. Weakening = less positive or more negative. Long hedgers like weakening; short hedgers like strengthening.",
        f"Contango basis −50 to −40 is strengthening toward zero as expiry nears.",
        None)

    # cash and carry
    spot = [50000, 40000, 40500, 61200, 38800][set_id - 1]
    carry_amt = [700, 800, 1000, 550, 920][set_id - 1]
    fut = spot + carry_amt + [500, 800, -400, -200, 350][set_id - 1]
    fair = spot + carry_amt
    edge = fut - fair
    if edge > 0:
        action = "Cash-and-carry: buy spot, sell futures"
        wrongs = ["Reverse cash-and-carry: sell spot, buy futures", "Buy only calls", "Do nothing; prices are exactly fair"]
    else:
        action = "Reverse cash-and-carry: sell spot, buy futures"
        wrongs = ["Cash-and-carry: buy spot, sell futures", "Sell only puts", "Short the index only"]
    add(5, "Arbitrage/spread calculations",
        f"Spot {rs(spot)}, cost of carry {rs(carry_amt)} so fair future is {rs(fair)}. Actual future trades at {rs(fut)}. The arbitrage is:",
        action, wrongs,
        f"Fair = {fair:,}. Traded F = {fut:,}. If F > fair, buy cheap spot and sell rich futures (cash-and-carry). If F < fair, sell spot and buy futures (reverse).",
        "Workbook: spot 50,000 + carry 700 = 50,700 but July future 51,200 → lock Rs 500.")

    # spread P/L
    n1, n2 = 4500 + set_id * 120, 5050 + set_id * 90
    later_n1, later_n2 = n1 + 80 + set_id * 10, n2 - 40 + set_id * 15
    # buy near sell far
    pl = (later_n1 - n1) + (n2 - later_n2)
    add(5, "Arbitrage/spread calculations",
        f"A trader buys the near-month at {rs(n1)} and sells the far-month at {rs(n2)} (buy-spread). Later the months are {rs(later_n1)} and {rs(later_n2)}. Combined P/L per unit is:",
        pl, [-pl, later_n1 - n1, n2 - later_n2],
        f"Near-month long P/L = {later_n1}−{n1} = {later_n1-n1}. Far-month short P/L = {n2}−{later_n2} = {n2-later_n2}. Total = {pl}.",
        "You profit when the spread (far−near) narrows after you bought the near/sold the far.",
        lambda x: rs(x))

    # jeweller long hedge offset
    buy_f = r.choice([50400, 50000, 49600, 51250, 48780]) + set_id * 35
    later_f = buy_f + 800 + set_id * 120
    extra_spot = later_f - buy_f  # designed to offset
    add(5, "Arbitrage/spread calculations",
        f"A jeweller buys gold futures at {rs(buy_f)} to hedge a future purchase. Futures later trade at {rs(later_f)} and are squared. Futures profit per 10 g is:",
        later_f - buy_f, [buy_f, later_f, -(later_f - buy_f)],
        f"Long futures profit = {later_f} − {buy_f} = {later_f-buy_f} per 10 g. This is meant to offset the extra amount paid in the spot market.",
        "Workbook jeweller: buy 50,400, sell 52,000 → Rs 1,600/10 g, matching the extra spot cost.",
        lambda x: rs(x))

    # --- Ch7 margins / MTM / penalty ---
    price = r.choice([49200, 50350, 51800, 47640, 55120]) + set_id * 15
    close = price + r.choice([70, 95, 140, -110, -85, 45])
    short_pl = (price - close) * 100  # per kg gold
    add(7, "Margin-related calculations",
        f"A trader is short 1 kg gold futures (quoted per 10 g) at {rs(price)}. DSP closes at {rs(close)}. MTM P/L of the short on the lot is (profit positive, loss negative):",
        int(short_pl), [int(-short_pl), int(close - price), int((close - price) * 10)],
        f"Short P/L = (entry − DSP) × 100 = ({price} − {close}) × 100 = {rs(short_pl)}. A negative figure is T+1 pay-in by the short.",
        "Workbook: short 50,000, close 50,100 → short P/L = −Rs 10,000 per kg, paid on T+1.",
        lambda x: rs(x))

    notional = r.choice([2100000, 3360000, 4725000, 6150000, 8800000]) + set_id * 25000
    im_pct = r.choice([0.04, 0.05, 0.06])
    elm_pct = 0.01
    im = notional * im_pct
    elm = notional * elm_pct
    tot = im + elm
    add(7, "Margin-related calculations",
        f"Contract value is {rs(notional)}. Initial margin {im_pct*100:.0f}% and ELM 1% on this notional. Total of IM + ELM is:",
        tot, [im, elm, notional * 0.2],
        f"IM = {im_pct}×{notional:,} = {rs(im)}. ELM = 1% = {rs(elm)}. Sum = {rs(tot)}. Tender/special/lean margins may still add.",
        "Rs 50 lakh gold × (4%+1%) = Rs 2.5 lakh core margin.",
        lambda x: rs(x))

    add(7, "Margin-related calculations",
        f"On {rs(notional)} notional, 1% Extreme Loss Margin equals:",
        elm, [im, tot, notional * 0.001],
        f"ELM = 0.01 × {notional:,} = {rs(elm)}, usually on gross open position, on top of SPAN/VaR IM.",
        "ELM is the ‘outside VaR’ cushion, often ~1%.",
        lambda x: rs(x))

    fsp = r.choice([4200, 5100, 8750, 12600, 24800, 51200]) + set_id * 25
    agri = r.choice([True, False])
    pct = 0.04 if agri else 0.03
    pen = fsp * pct
    add(7, "Margin-related calculations",
        f"Seller fails to deliver a {'agri' if agri else 'non-agri'} futures that settles at {rs(fsp)} (per quoted unit). Statutory default penalty rate (excluding replacement cost) is:",
        round(pen, 2), [fsp * (0.03 if agri else 0.04), fsp * 0.0175, fsp * 0.01],
        f"{'Agri 4%' if agri else 'Non-agri 3%'} of FSP = {pct:.0%} × {fsp} = {pen:.2f} per quoted unit, plus replacement cost. Sharing: ≥1.75% SGF, ≤0.25% CC, remainder to buyer.",
        "On a 1,000-unit agri lot the 4% slice is much larger than a normal IM day.",
        lambda x: rs(x, 2))

    # gold purity premium
    rate = r.choice([24600, 25100, 48750, 50300, 61800, 72150]) + set_id * 50
    prem_g = rate * 999 / 995
    add(7, "Margin-related calculations",
        f"Gold contract is priced on 0.995 purity at {rs(rate)} per 10 g. 0.999 purity is delivered. Amount payable per 10 g is closest to:",
        round(prem_g, 2), [rate, rate * 995 / 999, rate * 0.999],
        f"Payable = {rate} × 999/995 = {prem_g:.2f}.",
        "Workbook: 25,000 × 999/995 = 25,100.50.",
        lambda x: rs(x, 2))

    # peak / snapshot conceptual-numerical hybrid
    pos = r.choice([8, 12, 18, 24, 30]) + set_id
    peak = pos + r.choice([4, 7, 9, 11, 14])
    add(7, "Margin-related calculations",
        f"A client’s end-of-day gold futures position is {pos} lots but the intra-day peak snapshot is {peak} lots. Peak-margin rules require collection of full IM+ELM on:",
        f"{peak} lots (intra-day peak), not merely EOD {pos} lots",
        [f"Only {pos} lots at EOD", "Only option premium", "Zero lots if hedged"],
        "Since 2020, brokers must margin the peak intra-day exposure from exchange snapshots (typically four), not only the closing position.",
        "Intraday scalping 40 lots and finishing flat still needed margin at the 40-lot snapshot.")

    # --- Ch9 CTT ---
    sell_val = r.choice([4980000, 5125000, 3750000, 6400000, 8250000]) + set_id * 35000 + r.randint(1, 9) * 1000
    ctt = sell_val * 0.0001  # 0.01%
    add(9, "Margin-related calculations",
        f"A trader sells gold futures with contract value {rs(sell_val)}. CTT at 0.01% payable by the seller is:",
        round(ctt, 2), [sell_val * 0.0005, sell_val * 0.002 / 100, 18],
        f"CTT = 0.01% × {sell_val:,} = {ctt:.2f}. Unprocessed agri would be exempt.",
        "Workbook: 49,80,000 × 0.01% = Rs 498.",
        lambda x: rs(x, 2))

    prem_opt = r.choice([18000, 26500, 42000, 56000, 73500, 88000]) + set_id * 250
    ctt_o = prem_opt * 0.0005
    add(9, "Call breakeven",
        f"Seller of a commodity option receives premium {rs(prem_opt)}. CTT at 0.05% on premium is:",
        round(ctt_o, 2), [prem_opt * 0.0001, prem_opt * 0.00125, prem_opt * 0.18],
        f"Option-sale CTT = 0.05% × {prem_opt:,} = {ctt_o:.2f}, paid by the seller (writer).",
        "Exercise CTT is different: 0.0001% (delivery) or 0.125% (cash) on the purchaser.",
        lambda x: rs(x, 2))

    stamp = sell_val * 0.00002
    add(9, "Margin-related calculations",
        f"Stamp duty at Rs 2 per lakh (0.002%) on transaction value {rs(sell_val)} is:",
        round(stamp, 2), [sell_val * 0.00015 / 100, 2, sell_val * 0.01],
        f"0.002% × {sell_val:,} = {stamp:.2f}. Uniform from 1 July 2020 via the exchange.",
        "Rs 1 lakh notional → Rs 2 stamp.",
        lambda x: rs(x, 2))

    return out


USED_CONCEPTUAL = set()


def take_unique(pool, n, set_id, chapter):
    items = [x for x in pool if x["chapter"] == chapter]
    unused = [x for x in items if x["q"] not in USED_CONCEPTUAL]
    picked = []
    for x in unused:
        if len(picked) == n:
            break
        picked.append(x)
        USED_CONCEPTUAL.add(x["q"])
    return [dict(x) for x in picked]


def filler_numerical(set_id, ch, k):
    r = Rng(9000 + set_id * 80 + ch * 11 + k)
    if ch in (1, 8, 10, 6):
        notional = 100000 * r.choice([8, 12, 15, 20, 25, 40, 49, 60]) + set_id * 10000 + k * 25000
        rate = r.choice([0.0001, 0.00002, 0.00015 / 100 * 100])  # keep simple below
        kind = r.choice(["ctt", "stamp", "sebi", "gst"])
        if kind == "ctt":
            val = notional * 0.0001
            return Q(ch if ch in (6, 9) else 6, "Margin-related calculations",
                     f"Sale value of a metal futures trade is {rs(notional)}. CTT at 0.01% on the seller is:",
                     [rs(val, 2), rs(notional * 0.0005, 2), rs(notional * 0.002, 2), rs(18)],
                     0,
                     f"CTT = 0.01% × {notional:,} = {val:.2f}. Unprocessed agri contracts are exempt; metals are not.",
                     "Gold sale of Rs 49,80,000 attracts CTT of Rs 498.")
        if kind == "stamp":
            val = notional * 0.00002
            return Q(6, "Margin-related calculations",
                     f"Stamp duty at 0.002% (Rs 2 / lakh) on {rs(notional)} is:",
                     [rs(val, 2), rs(2), rs(notional * 0.0001, 2), rs(notional * 0.01, 2)],
                     0,
                     f"0.002% × {notional:,} = {val:.2f}. Uniform stamp duty applies from 1 July 2020.",
                     "Rs 1 lakh notional → Rs 2 stamp duty.")
        if kind == "sebi":
            val = notional * 0.0000015
            return Q(6, "Margin-related calculations",
                     f"SEBI turnover fee at Rs 15 per crore (0.00015%) on non-agri turnover {rs(notional)} is closest to:",
                     [rs(val, 2), rs(notional * 0.0001, 2), rs(1), rs(15)],
                     0,
                     f"Fee = 0.00015% × {notional:,} = {val:.2f}. Agri fee is Rs 1/crore, with the rest going to a farmer/FPO fund.",
                     "Rs 1 crore gold turnover → Rs 15 SEBI fee.")
        brk = r.choice([500, 800, 1000, 1200, 1500]) + k
        gst = brk * 0.18
        return Q(6, "Margin-related calculations",
                 f"Brokerage on a commodity trade is {rs(brk)}. GST at 18% on brokerage is:",
                 [rs(gst, 2), rs(brk * 0.05, 2), rs(brk * 0.12, 2), rs(brk)],
                 0,
                 f"GST = 18% × {brk} = {gst:.2f}. This is over and above GST on physical delivery of goods.",
                 "Rs 1,000 brokerage → Rs 180 GST.")
    # default futures-style filler
    entry = 40000 + set_id * 1500 + k * 250
    move = r.choice([120, 250, 400, -180, -300])
    pl = move * 100
    return Q(3, "Futures profit/loss" if pl >= 0 else "Futures loss",
             f"Long 1 kg gold (quote per 10 g) from {rs(entry)} to {rs(entry+move)}. Net P/L is:",
             [rs(pl), rs(-pl), rs(move), rs(pl / 10)],
             0,
             f"P/L = {move} × 100 = {rs(pl)} because 1 kg = 100 units of 10 g.",
             "A Rs 1 rise per 10 g = Rs 100 on the 1 kg lot.")


def needed_conceptual(set_id, nums):
    """How many conceptual per chapter after assigning numericals."""
    n_by = {c: 0 for c in range(1, 11)}
    for q in nums:
        n_by[q["chapter"]] += 1
    plan = {}
    for ch, w in WEIGHTS.items():
        plan[ch] = max(0, w - n_by[ch])
        # if numericals overshot, drop extras later
    return plan, n_by


def build_set(set_id):
    nums = numericals_for_set(set_id)
    selected_nums = []
    count = {c: 0 for c in range(1, 11)}
    for q in nums:
        if count[q["chapter"]] < WEIGHTS[q["chapter"]]:
            q = dict(q)
            opts, ans = shuffle_opts(q["options"], q["answer"], f"num-{set_id}-{q['q'][:50]}")
            q["options"], q["answer"] = opts, ans
            selected_nums.append(q)
            count[q["chapter"]] += 1
    paper = list(selected_nums)
    kfill = 0
    for ch, w in WEIGHTS.items():
        need = w - count[ch]
        if need <= 0:
            continue
        got = take_unique(CONCEPTUAL, need, set_id, ch)
        for item in got:
            opts, ans = shuffle_opts(item["options"], item["answer"], f"con-{set_id}-{item['q'][:50]}")
            item["options"], item["answer"] = opts, ans
        paper.extend(got)
        count[ch] += len(got)
        while count[ch] < w:
            kfill += 1
            fill = filler_numerical(set_id, ch, kfill)
            fill["chapter"] = ch
            fill["chapterName"] = CHAPTERS[ch]
            opts, ans = shuffle_opts(fill["options"], fill["answer"], f"fill-{set_id}-{kfill}-{ch}")
            fill["options"], fill["answer"] = opts, ans
            paper.append(fill)
            count[ch] += 1
    if len(paper) != 100:
        raise SystemExit(f"Set {set_id} has {len(paper)} questions: { {c: sum(1 for x in paper if x['chapter']==c) for c in range(1,11)} }")
    # order: mix but stable — sort by chapter then reshuffle within chapter using set_id
    grouped = {c: [x for x in paper if x["chapter"] == c] for c in range(1, 11)}
    ordered = []
    for c in range(1, 11):
        g = grouped[c]
        r = Rng(set_id * 50 + c)
        for i in range(len(g) - 1, 0, -1):
            j = r.randint(0, i)
            g[i], g[j] = g[j], g[i]
        ordered.extend(g)
    # light interleave so the paper is not strictly chapter-sorted like a textbook
    r = Rng(set_id * 13 + 7)
    blocks = [ordered[i:i + 5] for i in range(0, 100, 5)]
    for i in range(len(blocks) - 1, 0, -1):
        j = r.randint(0, i)
        blocks[i], blocks[j] = blocks[j], blocks[i]
    final = [q for b in blocks for q in b]
    return final[:100]


def main():
    global USED_CONCEPTUAL
    USED_CONCEPTUAL = set()
    counts = {c: sum(1 for x in CONCEPTUAL if x["chapter"] == c) for c in range(1, 11)}
    print("Conceptual by chapter:", counts, "total", sum(counts.values()))
    sets = {}
    for s in range(1, 6):
        paper = build_set(s)
        # verify weights
        w = {c: sum(1 for x in paper if x["chapter"] == c) for c in range(1, 11)}
        assert w == WEIGHTS, w
        sets[str(s)] = paper
        print(f"Set {s} OK", w)
    out = Path(__file__).parent / "js" / "questions.js"
    out.parent.mkdir(exist_ok=True)
    payload = json.dumps(sets, ensure_ascii=False)
    out.write_text("window.QUESTION_SETS = " + payload + ";\n", encoding="utf-8")
    print("Wrote", out, "bytes", out.stat().st_size)


if __name__ == "__main__":
    main()

