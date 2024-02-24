import streamlit as st
import psycopg2


# Function to connect to PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname=os.getenv("PG_DB_NAME"),
        user=os.getenv("PG_DB_USER"),
        password=os.getenv("PG_DB_PASS"),
        host=os.getenv("PG_DB_HOST"),
        port=10511
    )
    return conn


# Function to fetch data from the company_scores table
def fetch_company_scores():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.company_scores")
    rows = cur.fetchall()
    conn.close()
    return rows


# Function to map scores to color codes
def map_score_to_color(score):
    if score == 1:
        return "#FF0000"  # Red
    elif score == 2:
        return "#FF4500"  # Orange
    elif score == 3:
        return "#FFFF00"  # Yellow
    elif score == 4:
        return "#9ACD32"  # Yellow-Green
    elif score == 5:
        return "#008000"  # Green
    else:
        return "#000000"  # Black (default)


# Function to display Streamlit app
def main():
    st.title("Company Scores")

    # Fetch data from the database
    data = fetch_company_scores()

    # Display data in a table
    st.write("## Company Scores Table")
    st.write("(Scores are color-coded)")
    st.write(
        "| Ticker | Cash to Market Cap | PE | P/FCF | ROE | ROIC | Capital Spread | Debt to Equity | Interest Coverage | Cash to Debt Liabilities | PB | Payout Ratio | Cash Dividend Yield | Total Shareholder Yield | MOS DDM No Dividend Increase | MOS DDM With Dividend Increase | MOS DDM With Dividend Increase Buybacks | Final Score |")
    st.write(
        "| ------ | ------------------ | -- | ----- | --- | ---- | -------------- | --------------- | ----------------- | ------------------------ | -- | ------------- | ------------------ | ----------------------- | -------------------------- | ------------------------------- | ------------------------------------- | ------------ |")
    for row in data:
        ticker = row[1]
        scores = row[2:-1]  # Exclude the ID and Final Score
        final_score = row[-1]

        # Color-code the scores
        scores_with_colors = [f'<span style="color:{map_score_to_color(score)}">{score}</span>' for score in scores]
        final_score_color = f'<span style="color:{map_score_to_color(final_score)}">{final_score}</span>'

        # Display the row in the table
        st.write(f"| {ticker} | {' | '.join(scores_with_colors)} | {final_score_color} |")


if __name__ == "__main__":
    main()
