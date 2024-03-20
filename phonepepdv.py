import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.colored_header import colored_header
import plotly.express as px
import os
import json
import csv
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_dynamic_filters import DynamicFilters
img=Image.open(r"C:/Users/Dell/Downloads/phonepe-launches-upi.jpg")
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "PhonePe PulseData Visualization App by Kamatchi Thangaraj"
    }
)
colored_header(
      label="WELCOME TO THE VISUALIZATION OF THE PHONEPE PULSE DATA",
      description="""This application visulizes the PhonePe 
      Unified Payments Interface Transactions and User Data
      from the year 2018 to 2023""",
      color_name="violet-70",
      )
st.markdown("<h2 style='font-family: Calibri; font-size: 36px;'>PhonePe Pulse Data</h2>",unsafe_allow_html=True)
st.sidebar.header(":Blue[**PhonePe PulseData dashboard**]")
def main():
    import pandas as pd
    from PIL import Image
    from streamlit_extras.colored_header import colored_header
    import plotly.express as px
    import os
    import json
    import csv
    from PIL import Image
    from streamlit_option_menu import option_menu
    from streamlit_dynamic_filters import DynamicFilters
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home","DataFrames","Plotly"], 
            icons=[], menu_icon="cast", default_index=1)
    if selected=='Home':

        #This is to direct the path to get the data as states

        agg_path_transn=r"E:/DataScience/Project2-PhonePePulseData/pulse-master/data/aggregated/transaction/country/india/state/"
        agg_path_user=r"E:/DataScience/Project2-PhonePePulseData/pulse-master/data/aggregated/user/country/india/state/"
        map_path_transn=r"E:/DataScience/Project2-PhonePePulseData/pulse-master/data/map/transaction/hover/country/india/state/"
        map_path_user=r"E:/DataScience/Project2-PhonePePulseData/pulse-master/data/map/user/hover/country/india/state/"
        top_path_transn=r"E:/DataScience/Project2-PhonePePulseData/pulse-master/data/top/transaction/country/india/state/"
        top_path_user=r"E:/DataScience/Project2-PhonePePulseData/pulse-master/data/top/user/country/india/state/"
        Agg_state_list=os.listdir(agg_path_transn)
        #print(Agg_state_list)
        #Data_Extraction
        #agg_trans
        at_clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

        for i in Agg_state_list:
                p_i=agg_path_transn+i+"/"
                Agg_yr=os.listdir(p_i)
                for j in Agg_yr:
                    p_j=p_i+j+"/"
                    Agg_yr_list=os.listdir(p_j)
                    for k in Agg_yr_list:
                        p_k=p_j+k
                        Data=open(p_k,'r')
                        D=json.load(Data)
                        for z in D['data']['transactionData']:
                            Name=z['name']
                            count=z['paymentInstruments'][0]['count']
                            amount=z['paymentInstruments'][0]['amount']
                            at_clm['Transaction_type'].append(Name)
                            at_clm['Transaction_count'].append(count)
                            at_clm['Transaction_amount'].append(amount)
                            at_clm['State'].append(i)
                            at_clm['Year'].append(j)
                            at_clm['Quarter'].append(int(k.strip('.json')))
                #Succesfully created a dataframe
        Agg_Trans=pd.DataFrame(at_clm)
        #print(Agg_Trans)
        #agg_user
        au_clm={'State':[], 'Year':[],'Quarter':[],'Registered_Users':[]}

        for i in Agg_state_list:
            p_i=agg_path_user+i+"/"
            Agg_yr=os.listdir(p_i)
            for j in Agg_yr:
                p_j=p_i+j+"/"
                Agg_yr_list=os.listdir(p_j)
                for k in Agg_yr_list:
                    p_k=p_j+k
                    Data=open(p_k,'r')
                    D=json.load(Data)
                    Reg_Users= D['data']['aggregated']['registeredUsers']
                    au_clm['Registered_Users'].append(Reg_Users)
                    au_clm['State'].append(i)
                    au_clm['Year'].append(j)
                    au_clm['Quarter'].append(int(k.strip('.json')))
        #Succesfully created a dataframe
        Agg_User=pd.DataFrame(au_clm)
        #Agg_User

        #map_trans
        mt_clm={'State':[], 'Year':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

        for i in Agg_state_list:
            p_i=map_path_transn+i+"/"
            Agg_yr=os.listdir(p_i)
            for j in Agg_yr:
                p_j=p_i+j+"/"
                Agg_yr_list=os.listdir(p_j)
                for k in Agg_yr_list:
                    p_k=p_j+k
                    Data=open(p_k,'r')
                    D=json.load(Data)
                    #print(D)
                    for z in D['data']['hoverDataList']:
                        Name=z['name']
                        count=z['metric'][0]['count']
                        amount=z['metric'][0]['amount']
                        mt_clm['District'].append(Name)
                        mt_clm['Transaction_count'].append(count)
                        mt_clm['Transaction_amount'].append(amount)
                        mt_clm['State'].append(i)
                        mt_clm['Year'].append(j)
                        mt_clm['Quarter'].append(int(k.strip('.json')))
        #Succesfully created a dataframe
        Map_Trans=pd.DataFrame(mt_clm)
        #Map_Trans

        #map_user
        mu_clm={'State':[], 'Year':[],'Quarter':[],'District':[], 'Registered_Users':[],'AppOpens':[]}

        for i in Agg_state_list:
            p_i=map_path_user+i+"/"
            Agg_yr=os.listdir(p_i)
            for j in Agg_yr:
                p_j=p_i+j+"/"
                Agg_yr_list=os.listdir(p_j)
                for k in Agg_yr_list:
                    p_k=p_j+k
                    Data=open(p_k,'r')
                    D=json.load(Data)
                    #print(D)
                    for z in D["data"]["hoverData"].items():
                        Name=z[0]
                        reg_users=z[1]['registeredUsers']
                        mu_clm['District'].append(Name)
                        mu_clm['AppOpens'] = z[1]['appOpens']
                        mu_clm['Registered_Users'].append(reg_users)
                        mu_clm['State'].append(i)
                        mu_clm['Year'].append(j)
                        mu_clm['Quarter'].append(int(k.strip('.json')))
        #Succesfully created a dataframe
        Map_User=pd.DataFrame(mu_clm)
        #Map_User

        #top_trans
        tt_clm={'State':[], 'Year':[],'Quarter':[],'PinCode':[], 'Transaction_count':[], 'Transaction_amount':[]}

        for i in Agg_state_list:
            p_i=top_path_transn+i+"/"
            Agg_yr=os.listdir(p_i)
            for j in Agg_yr:
                p_j=p_i+j+"/"
                Agg_yr_list=os.listdir(p_j)
                for k in Agg_yr_list:
                    p_k=p_j+k
                    Data=open(p_k,'r')
                    D=json.load(Data)
                    #print(D)
                    for z in D['data']['pincodes']:
                        Name=z['entityName']
                        count=z['metric']['count']
                        amount=z['metric']['amount']
                        tt_clm['PinCode'].append(Name)
                        tt_clm['Transaction_count'].append(count)
                        tt_clm['Transaction_amount'].append(amount)
                        tt_clm['State'].append(i)
                        tt_clm['Year'].append(j)
                        tt_clm['Quarter'].append(int(k.strip('.json')))
        #Succesfully created a dataframe
        Top_Trans=pd.DataFrame(tt_clm)
        #Top_Trans

        #top_user
        tu_clm={'State':[], 'Year':[],'Quarter':[],'PinCode':[], 'Registered_Users':[]}

        for i in Agg_state_list:
            p_i=top_path_user+i+"/"
            Agg_yr=os.listdir(p_i)
            for j in Agg_yr:
                p_j=p_i+j+"/"
                Agg_yr_list=os.listdir(p_j)
                for k in Agg_yr_list:
                    p_k=p_j+k
                    Data=open(p_k,'r')
                    D=json.load(Data)
                    #print(D)
                    for z in D['data']['pincodes']:
                        Name=z['name']
                        count=z['registeredUsers']
                        tu_clm['PinCode'].append(Name)
                        tu_clm['Registered_Users'].append(count)
                        tu_clm['State'].append(i)
                        tu_clm['Year'].append(j)
                        tu_clm['Quarter'].append(int(k.strip('.json')))
        #Succesfully created a dataframe
        Top_User=pd.DataFrame(tu_clm)
        #Top_User

        #Connecting MSSQL server
        import mysql.connector
        connection=mysql.connector.connect(host="localhost", user="root", password="12345",database="project_2")
        mycursor=connection.cursor()
        if connection:
            #creating tables if they are not there already
            query="""create table if not exists Agg_Trans(State varchar(200),
            Year varchar(4),Quarter varchar(1),
            Transaction_type varchar(400),Transaction_count varchar(400),  
            Transaction_amount varchar(400))"""
            mycursor.execute(query)
            connection.commit()
            query="""create table if not exists Agg_User(State varchar(200),
            Year varchar(4),Quarter varchar(1),
            Registered_Users varchar(200),District varchar(400),PinCode varchar(6))"""
            mycursor.execute(query)
            connection.commit()
            query="""create table if not exists Map_Trans(State varchar(200),
            Year varchar(4),Quarter varchar(1),District varchar(400),
            Transaction_type varchar(400),Transaction_count varchar(400),  
            Transaction_amount varchar(400))"""
            mycursor.execute(query)
            connection.commit()
            query="""create table if not exists Map_User(State varchar(200),
            Year varchar(4),Quarter varchar(1),District varchar(400), 
            Registered_Users varchar(200),AppOpens varchar(200)
            )"""
            mycursor.execute(query)
            connection.commit()
            query="""create table if not exists Top_Trans(State varchar(200),
            Year varchar(4),Quarter varchar(1),
            PinCode varchar(6),Transaction_count varchar(400),  
            Transaction_amount varchar(400))"""
            mycursor.execute(query)
            connection.commit()
            query="""create table if not exists Top_User(State varchar(200),
            Year varchar(4),Quarter varchar(1),PinCode varchar(6),
            Registered_Users varchar(200))"""
            mycursor.execute(query)
            connection.commit()

            #Inserting table data
            atrows=[]
            for index in Agg_Trans.index:
                row=tuple(Agg_Trans.loc[index].values)
                row=tuple(str(d) for d in row)
                atrows.append(row)
            #print(atrows)
            query="""insert into Agg_Trans values (%s,%s,%s,%s,%s,%s)"""
            mycursor.executemany(query,atrows)
            connection.commit()
            aurows=[]
            for index in Agg_User.index:
                row=tuple(Agg_User.loc[index].values)
                row=tuple(str(d) for d in row)
                aurows.append(row)
            #print(aurows)
            mtrows=[]
            for index in Map_Trans.index:
                row=tuple(Map_Trans.loc[index].values)
                row=tuple(str(d) for d in row)
                mtrows.append(row)
            #print(mtrows)
            query="""insert into Map_Trans values (%s,%s,%s,%s,%s,%s)"""
            mycursor.executemany(query,mtrows)
            connection.commit()
            murows=[]
            for index in Map_User.index:
                row=tuple(Map_User.loc[index].values)
                row=tuple(str(d) for d in row)
                murows.append(row)
            #print(murows)
            query="""insert into Map_User values (%s,%s,%s,%s,%s,%s)"""
            mycursor.executemany(query,murows)
            connection.commit()
            ttrows=[]
            for index in Top_Trans.index:
                row=tuple(Top_Trans.loc[index].values)
                row=tuple(str(d) for d in row)
                ttrows.append(row)
            #print(ttrows)
            query="""insert into Top_Trans values (%s,%s,%s,%s,%s,%s)"""
            mycursor.executemany(query,ttrows)
            connection.commit()
            turows=[]
            for index in Top_User.index:
                row=tuple(Top_User.loc[index].values)
                row=tuple(str(d) for d in row)
                turows.append(row)
            #print(turows)
            query="""insert into Top_User values (%s,%s,%s,%s,%s)"""
            mycursor.executemany(query,turows)
            connection.commit()
    
                    
    if selected=='DataFrames':
            import mysql.connector
            connection=mysql.connector.connect(host="localhost", user="root", password="12345",database="project_2")
            mycursor=connection.cursor()
            Data=["Select",
                    "1. List of top ten states in India with the highest number of transactions in the last quarter:",
                    "2. The average number of transactions per year per state:",
                    "3. Which district has the lowest number of registered users and its appopen count?",
                    "4. Of the Southern States which state showed a drastic increase in the number of users from 2022 to 2023?",
                    "5. Which state in North-East has the maximum number of transactions in the year 2023?",
                    "6. The highest number of transactions year for every state",
                    "7. Which state showed a downward trend in number of transactions in the last year?",
                    "8. Which district in India has the highest number of registered users and the number of appopens in it in the year 2023?",
                    "9. Which transaction type has the highest amount in transaction in every state in every year?",
                    "10. The top performing state in terms of number of appopens in the last quarter:"]
            
            content_selection=st.selectbox("Select a view",Data)
            if content_selection=="1. List of top ten states in India with the highest number of transactions in the last quarter:":
                query="""with cte1 as 
                (select *,ROW_NUMBER() OVER (PARTITION BY State ORDER BY Year DESC,Quarter DESC) as rownum1
                    from  `project_2`.`agg_trans`)
                    , cte2 as (
                    select 
                    State,Year,Quarter,Transaction_count
                    from 
                    cte1 
                    where rownum1=1 
                    order by 
                    Transaction_count DESC)
                    select * from cte2 limit 10"""
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.dataframe(data)
            if content_selection=="2. The average number of transactions per year per state:":
                query="""with cte1 as 
                (select State,Year,
                SUM(Transaction_count) as net_trans, 
                Count(Quarter)  as count from `project_2`.`agg_trans` group by State,Year )
                select State,Year,(net_trans/count) as avg_transaction_count from cte1"""
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="3. Which district has the lowest number of registered users and its appopen count?":
                query="""with cte1 as 
                (select *
                from `project_2`.`map_user` order by Registered_Users desc )
                select District from cte1 limit 1"""
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="4. Of the Southern States which state showed a drastic increase in the number of users from 2022 to 2023?":
                query="""with cte1 as 
                (select *,
                sum(Registered_Users) over (partition by State,Year) as total_users_by_yr 
                            from `project_2`.`agg_user`
                            where State in ('maharashtra','goa','karnataka', 'kerala','tamil-nadu', 'telangana',
                            'andaman-&-nicobar-islands', 'andhra-pradesh','dadra-&-nagar-haveli-&-daman-&-diu','puducherry')),
                cte2 as
                (select *, 
                case when Year='2022'
                then Registered_Users end as RU1,
                case when Year='2023'
                then Registered_Users end as RU2 from cte1),
                cte3 as (
                select *,
                ROW_NUMBER() OVER (PARTITION BY State ORDER BY Year DESC) as rownum,
                case when RU2>RU1 
                then RU2-RU1 
                else null
                end
                as diff 
                from cte2
                )
                select State from cte3 where rownum=1 order by diff desc limit 1"""
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="5. Which state in North-East has the maximum number of transactions in the year 2023?":
                query="""with cte1 as 
                (select *,
                sum(Transaction_count) over (partition by State,Year) as total_trans_by_yr,
                ROW_NUMBER() OVER (PARTITION BY State ORDER BY Year DESC) as rownum
                from `project_2`.`agg_trans`
                    where State in ('manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha','sikkim','tripura','assam')
                            and Year='2023')
                select State from cte1 
                where rownum=1 
                order by total_trans_by_yr desc
                limit 1"""
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="6. The highest number of transactions year for every state":
                query="""with cte1 as 
                (select *,sum(Transaction_count) over (partition by State,Year) as total_trans_by_yr 
                from `project_2`.`agg_trans`) 
                ,cte2 as (
                select *, ROW_NUMBER() OVER (PARTITION BY State order by (total_trans_by_yr) Desc) as rownum
                            from cte1)
                select State,Year from cte2 where rownum=1
                """
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="7. Which state showed a downward trend in number of transactions in the last two years?":
                query="""with cte1 as 
                (select distinct State,Year,
                sum(Transaction_count) over (partition by State,Year) as total_trans_by_yr
                from `project_2`.`agg_trans`
                            )
                ,cte2 as (
                    select State,Year,total_trans_by_yr,
                    ROW_NUMBER() OVER (PARTITION BY State ORDER BY Year DESC) as rownum
                    from cte1)
                ,cte3 as (
                Select *, 
                case when rownum=1 then total_trans_by_yr else null end as tc1,
                case when rownum=2 then total_trans_by_yr else null end as tc2 
                from cte2),
                cte4 as (
                select *,
                    FIRST_VALUE (tc2) OVER (PARTITION BY State order by tc2 desc) as 2022trans,
                    FIRST_VALUE (tc1) OVER (PARTITION BY State order by tc1 desc) as 2023trans
                    from cte3
                )
                select distinct State from cte4 where 2022trans>2023trans
                """
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="8. Which district in India has the highest number of registered users and the number of appopens in it in the year 2023?":
                query="""with cte1 as 
                (select *,
                sum(Registered_Users) over (partition by State,District,Year) as total_users_by_dist,
                sum(Appopens) over (partition by State,District,Year) as total_appopens_by_dist,
                ROW_NUMBER() OVER (PARTITION BY Year ORDER BY Year DESC) as rownum
                from `project_2`.`map_user`
                                        )
                    select State,Year,District,total_users_by_dist as user_count,
                    total_appopens_by_dist as Appopens
                    from cte1 where rownum=1 and Year='2023'
                """
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="9. Which transaction type has the highest amount in transaction in every state in every year?":
                query="""with cte1 as 
                (select *,
                sum(Transaction_count) over (partition by State,Year,Transaction_type) as total_count_by_type
                from `project_2`.`agg_trans`
                            ),
                cte2 as(
                    select State,Year,Transaction_type,total_count_by_type,
                    ROW_NUMBER() OVER (PARTITION BY State,Year ORDER BY total_count_by_type DESC) as rownum
                    from cte1)
                select * from cte2 where rownum=1
                """
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            if content_selection=="10. The top performing state in terms of number of appopens in the last quarter:":
                query="""with cte1 as 
                (select *,
                sum(AppOpens) over (partition by State,Year,Quarter) as total_Appopens_by_yr
                from `project_2`.`map_user`
                            ),
                cte2 as (
                    select *, 
                        ROW_NUMBER() OVER (PARTITION BY State ORDER BY Year desc,Quarter Desc,AppOpens DESC) as rownum from cte1),
                cte3 as (
                select * from cte2
                where rownum=1 order by AppOpens desc )
                select State from cte3 limit 1
                """
                mycursor.execute(query)
                result=mycursor.fetchall()
                for data in result:
                    st.table(data)
            
    if selected=='Plotly':
        import mysql.connector
        connection=mysql.connector.connect(host="localhost", user="root", password="12345",database="project_2")
        mycursor=connection.cursor()
        if connection:
        #insights into the data
            Years=[]
            Quarter= ['1','2','3','4']
            query="Select distinct Year from `project_2`.`agg_trans`"
            mycursor.execute(query)
            result=mycursor.fetchall()
            for data in result:
                Years.append(data)
            year_list=[item for sublist in Years for item in sublist]
            with st.sidebar:

                year = option_menu("Year", year_list, 
                icons=[], menu_icon="cast", default_index=1)
                year
                
                query1=f"""with cte1 as 
                (select distinct * from agg_trans)
                select State,sum(Transaction_amount) over (partition by State,Year) as Total 
                from cte1 """
                mycursor.execute(query1)
                import pandas as pd
                import plotly.express as px

                df = pd.DataFrame(mycursor.fetchall(), columns=['State','Total_Amount'])
                fig = px.choropleth(
                    df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='Total_Amount',
                    color_continuous_scale='Reds'
                )

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
                st.plotly_chart(fig,use_container_width=False)
                import plotly.express as px
                import plotly.io as pio
                import pandas as pd
                pio.templates.default = "simple_white"

                px.defaults.template = "ggplot2"
                px.defaults.color_continuous_scale = px.colors.sequential.Blackbody
                px.defaults.width = 200
                px.defaults.height = 400
                df_sub = pd.read_csv(r"E:/GUVI/Code/agg_trans.csv")
                fig = px.scatter(df_sub, x="State", y="Transactions_Count",color="Total_Amount", width=1500,height=1000)
                fig.show()
                st.markdown("### :violet[State]")
                query2=f"""with cte1 as (select distinct * from agg_trans)
                select State,Year,sum(Transaction_amount) over (partition by State,Year) as Total,
                sum(Transaction_count) over (partition by State,Year) as Transactions_Count from cte1 
                where Year = '{year}'"""
                mycursor.execute(query2)
                import pandas as pd
                import plotly.express as px
                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year','Transactions_Count','Total_Amount'])
                file_path="E:/GUVI/Code/agg_trans.csv"
                df.to_csv(file_path,index=False)
                df_sub = pd.read_csv(r"E:/GUVI/Code/agg_trans.csv")
                fig1 = px.density_heatmap(df_sub, x="State", y="Transactions_Count",z="Total_Amount",hover_name ="State",
                                        width=1300,height=1200,color_continuous_scale ='Greens')
                fig1.show()
                st.plotly_chart(fig1,use_container_width=False)
            with st.sidebar: 
                selected_state = option_menu("State", ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'], 
                icons=[], menu_icon="cast", default_index=1)
                selected_state   
                quarter = option_menu("Quarter",Quarter, 
                icons=[], menu_icon="cast", default_index=1)
                quarter
                query3=f"""with cte1 as (select distinct * from agg_trans)
                select Year,Quarter,Transaction_count,Transaction_amount 
                from agg_trans where State = '{selected_state}'"""
                mycursor.execute(query3)
                import pandas as pd
                import plotly.express as px
                df = pd.DataFrame(mycursor.fetchall(), columns=['Year','Quarter','Transactions_Count','Transaction_amount'])
                file_path="E:/GUVI/Code/agg_trans_state.csv"
                df.to_csv(file_path,index=False)
                df_sub = pd.read_csv(r"E:/GUVI/Code/agg_trans_state.csv")
                fig1 = px.density_heatmap(df_sub, x="Quarter", y="Transactions_Count",z="Transaction_amount",hover_name ="Quarter",
                                        width=1300,height=1200,color_continuous_scale ='Greens')
                fig1.show()
                st.plotly_chart(fig1,use_container_width=False)
main()
