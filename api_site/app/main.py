from sql.sql import Database
import streamlit as st
import pandas as pd
import time

def main():
    print("App Started.")

    db = Database("mysqldb",3306,"dm","dmpass")
    #db = Database("127.0.0.1",3306,"dm","dmpass")
   
    while db.isRdy() == 0:
          print("Waiting for database to become available...")
          time.sleep(5)

    #print(db.query_products())
    # Streamlit View
    st.set_page_config(
      page_title="DMlab próba",
    )
    
    # Title
    st.markdown("<h1 style='text-align: center;'>DMlab próba feladat</h1>", unsafe_allow_html=True)
    st.markdown("***")

    df = pd.DataFrame(db.query_products())

    #streamlit
    st.dataframe(df)

if __name__ == "__main__":
    main()