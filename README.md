# 📈 Boliviano Parallel Exchange Rate Fetch

This project provides a simple **exchange rate tool** using the [Binance P2P API](https://p2p.binance.com).  
It fetches the latest **BOB/USDT exchange rate**, as well as maintain a historic csv for further analysis or plotting.

Bolivia has fallen into a deep economic struggle with low international reserves and an unstable political environment. This caused a devaluation of the currency.
The exchange rate has been fixed for the last 20 years at around 6.96 BOB per USD. This caused an imbalance on the markets as the balance of payments were not generating enough reserves to maintain the rate. In addition to this, Bolivia has a subsidy for gasoline to maintain low prices.

This led to an economic crisis where the scarcity of dollars became unsustainable. People don't have the ability to buy and sell dollars freely anymore, and there is also a scarcity of gasoline and diesel. The government maintained the fixed exchange rate model and a parallel market was born. People can buy and sell USD at higher prices via P2P platforms like Binance P2P or in person with different forex houses.  

As a boliviano myself, after being constantly asked about the evolution of the parallel rate and the latest price of the dollar, I created this small project for anyone that is curious to know the latest quote as well as have an idea of how it's behaving through time. 

I hope you find this project as interesting as it is for me. 

WGG.IJN.XTO.SMG.PSPS

---

## 🚀 Features
- Fetches the **latest BOB/USDT exchange rate** via Binance P2P API
- Maintains a historic **rate csv** which can be used for further data analysis and plotting
- Create a **HTML plotly** from the historic csv and look at how the rate is changing through time 
- You can also run a **docker container** for easier reproduction

---

## 📂 Project Structure

| File | Description |
|----------|-------------|
| `get_bob_quote.py` | # Fetch latest exchange rate
| `append_bob_quote.py` | # Fetch latest exchange rate and append to a csv file
| `plot_bob_historic.py` | # Plot csv file created with append_bob_quote.py
| `bob_usdt_chart.html` | # Inside plots directory, this will be created by plot_bob_historic.py and automatically opened on local host
| `Dockerfile` | #Use this to create a docker image and container
| `requirements.txt` | #All project dependencies and packages
| `README.md` |


---

## ⚙️ Installation (Option 1)

1. Clone the repo
   ```bash  
   git clone https://github.com/sergiobk201/get_bob_quote.git
   cd get_bob_quote
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt  
   ```

---

## ⚙️ Installation (Option 2)

1. Clone the repo
   ```bash  
   git clone https://github.com/sergiobk201/get_bob_quote.git
   cd get_bob_quote
   ```
2. Build your docker container
   ```bash
   docker build -t choose_name .
   ```
3. Run docker container and remember to host a local HTTP server 
   ```bash
   docker run -it -p 8080:8080 choose_name
   ```  
4. You can now run all the .py files like this:
   ```bash
   python get_bob_quote.py
   ```
5. If you want to get a plot with the docker container, you have to run append_bob_quote.py and plot_bob_historic.py inside terminal
6. Go to plots directory 
   ```bash
   cd plots
   ```
7. Start local HTTP server
   ```bash
   python -m http.server 8080
   ```
8. Copy the following link: [HTML Plot](http://localhost:8080/bob_usdt_chart.html) and paste it on your local machine's browser

---

## 🖥️ Usage

Run from terminal:

### Fetch latest quote
```bash
python get_bob_quote.py
```
### Maintain and update csv with latest quote
```bash
python append_bob_quote.py
```
### Plot csv file
```bash
python plot_bob_historic.py
``` 
---


