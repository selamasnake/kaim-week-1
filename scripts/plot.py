import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import plotly.express as px


plt.style.use("seaborn-v0_8")
plt.rcParams["figure.figsize"] = (12, 6)

class Plot:

    def plot_daily_publications(data):
        """
        Plot daily publications with a rolling mean.
        """

        # Convert to proper daily DatetimeIndex
        publications_by_day = (data['date'].dt.floor('D').value_counts().sort_index())

        # 7-day rolling mean
        daily_rolling = publications_by_day.rolling(window=7, center=True).mean()

        plt.figure(figsize=(14, 6))
        sns.lineplot(x=publications_by_day.index, y=daily_rolling, color='black')

        plt.title('Publications by Day (7-day rolling mean)')
        plt.xlabel('Day')
        plt.ylabel('Number of Publications')

        # Cleaner date axis since the dates are noisy
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_monthly_publications(data):
        """
        Plot monthly publications.
        """

        # Convert to month start timestamps
        publications_by_month = (data['date'].dt.to_period('M').dt.to_timestamp().value_counts().sort_index()
        )

        plt.figure(figsize=(14, 6))
        sns.lineplot(x=publications_by_month.index, y=publications_by_month.values, color='black')

        plt.title('Publications by Month')
        plt.xlabel('Month')
        plt.ylabel('Number of Publications')

         # Cleaner date axis since the months are noisy
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return publications_by_month

    def plot_yearly_publications(data):
        """
        Plot yearly publications.
        """

        publications_by_year = (data['date'].dt.to_period('Y').dt.to_timestamp().value_counts().sort_index())

        plt.figure(figsize=(14, 6))
        sns.lineplot(x=publications_by_year.index, y=publications_by_year.values, color='black',marker='o',markersize=6,markerfacecolor='black')

        plt.title('Publications by Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Publications')

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return publications_by_year

    def plot_hourly_publications(data):
        """
        Plot number of publications by hour of the day.
        """
        data['publication_hour'] = data['date'].dt.hour

        # Count publications per hour
        publication_by_hour = data.groupby('publication_hour').size()

        plt.figure(figsize=(12, 12))
        sns.barplot(x=publication_by_hour.index,
                    y=publication_by_hour.values,
                    palette='Blues_d')
        plt.title('Publications by Hour of Day (Local Time)')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Publications')
        plt.xticks(rotation=0)
        plt.show()

        return publication_by_hour

    def plot_stock_price(data):
        """
        Plot stock Close price and Volume.
        """

        # Extract ticker
        ticker = data['Ticker'].iloc[0]

        # --- Close Price Chart ---
        plt.figure(figsize=(10,4))
        plt.plot(data.index, data["Close"], label="Close", color="blue")
        plt.title(f"{ticker} Stock Close Price")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # --- Volume Chart ---
        plt.figure(figsize=(10,4))
        plt.plot(data.index, data["Volume"], label="Volume", color="purple")
        plt.title(f"{ticker} Daily Trading Volume")
        plt.xlabel("Date")
        plt.ylabel("Shares Traded")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_stock_mva(data):
        """
        Plot stock Close price along with all SMA columns.
        """
        ma_columns = [col for col in data.columns if col.startswith('SMA')]
        fig = px.line(
            data, 
            x=data.index, 
            y=['Close'] + ma_columns,
            title='Stock Price with Simple Moving Averages',
            labels={'value': 'Price', 'index': 'Date'}
        )
        fig.show()

    def plot_ema(data):
        """
        Plot stock Close price along with all EMA columns.
        """
        ema_columns = [col for col in data.columns if col.startswith('EMA')]
        fig = px.line(data, x=data.index, y=['Close'] + ema_columns,
            title='Stock Price with Exponential Moving Averages',
            labels={'value': 'Price', 'index': 'Date'}
        )
        fig.show()


    def plot_rsi(data):
        """
        Plot all RSI column. 
        """
        fig = px.line(
            data, 
            x=data.index, 
            y=data['RSI_14'],
            title='Relative Strength Index (RSI)',
            labels={'value': 'RSI_14', 'index': 'Date'}
        )
        fig.show()


    # --- Plot MACD ---
    def plot_macd(data):
        """
        Plot all MACD columns dynamically (MACD line, signal, histogram).
        """
        macd_columns = [col for col in data.columns if 'MACD' in col]
        fig = px.line(data, x=data.index, y=macd_columns,
            title='Moving Average Convergence Divergence (MACD)',
            labels={'value': 'Value', 'index': 'Date'}
        )
        fig.show()


