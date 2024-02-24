import streamlit as st
import psycopg2
import os
import pandas as pd

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
        return "background-color: #FF0000"  # Red
    elif score == 2:
        return "background-color: #FF4500"  # Orange
    elif score == 3:
        return "background-color: #FFFF00"  # Yellow
    elif score == 4:
        return "background-color: #9ACD32"  # Yellow-Green
    elif score == 5:
        return "background-color: #008000"  # Green
    else:
        return ""  # No color


# Function to display Streamlit app
def main():
    st.title("Company Scores")

    # Fetch data from the database
    data = fetch_company_scores()

    # Prepare data for DataFrame and drop ID column
    df = pd.DataFrame(data, columns=["ID", "Ticker", "Cash to Market Cap", "PE", "P/FCF", "ROE", "ROIC", "Capital Spread", 
                                      "Debt to Equity", "Interest Coverage", "Cash to Debt Liabilities", "PB", 
                                      "Payout Ratio", "Cash Dividend Yield", "Total Shareholder Yield", 
                                      "MOS DDM No Dividend Increase", "MOS DDM With Dividend Increase", 
                                      "MOS DDM With Dividend Increase Buybacks", "Final Score"])
    df.drop(columns=['ID'], inplace=True)

    # Round Final Score to two decimal places
    df["Final Score"] = df["Final Score"].round(2)

    # Apply color-coding to scores
    scores_columns = ["Cash to Market Cap", "PE", "P/FCF", "ROE", "ROIC", "Capital Spread", "Debt to Equity", 
                      "Interest Coverage", "Cash to Debt Liabilities", "PB", "Payout Ratio", "Cash Dividend Yield", 
                      "Total Shareholder Yield", "MOS DDM No Dividend Increase", "MOS DDM With Dividend Increase", 
                      "MOS DDM With Dividend Increase Buybacks", "Final Score"]

    # Display the DataFrame
    st.write("## Company Scores Table")
    st.write("(Scores are color-coded)")
    st.dataframe(df)


if __name__ == "__main__":
    main()
