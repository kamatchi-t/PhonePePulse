# PhonePePulse
With Financial Inclusion, at the heart of Digital revolution in the past decade in India, UPI payments are on the steady rise.
PhonePe, one of the leading Unified Payments Interfaces in India has penetrated into rural as well as Urban areas. This application gives a picture of the number of transactions, the transacted amount, the number of registered users and their app usage trends from the year 2018 till real time.

The Approach:
1. The PhonePePulse transaction data is cloned from Git Hub.
2. The extracted data is refined and stored in MySQL database as six tables.
     1.Aggregate Transactions- Table_Name:'agg_trans'
     2.Aggregate Users- Table_Name:'agg_user'
     3.Map Transactions- Table_Name:'map_trans'
     4.Map Users- Table_Name:'map_user'
     5.Top Transactions- Table_Name:'top_trans'
     6.Top User- Table_Name:'top_user'
3. The stored data can be retrieved anytime with the user queries.
4. The map of India showing the Transaction Count and Transaction Amount of all the states and union territories can be visualized here.
5. The additional plotly charts are also displayed when each state is selected.
