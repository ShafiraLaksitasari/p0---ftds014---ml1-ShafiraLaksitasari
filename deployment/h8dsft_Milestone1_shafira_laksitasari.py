import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import streamlit as st

page = st.sidebar.radio('Select Page', ['Top 5 states with Highest Emmision','Air Quality Index (AQI) Progress','Air Quality Index (AQI) Limits','Monthly Air Quality Index (AQI) per State', 'Monthly Air Quality Index (AQI) per Emission','Significant development of AQI Emissions'])

o3 = pd.read_csv('csv/o3.csv')
pm10 = pd.read_csv('csv/pm10.csv')
state = pd.read_csv('csv/state.csv')
mv = ['NaN']
pm25 = pd.read_csv('csv/pm25.csv', na_values = mv)

# Data Cleaning

# O3
o3 = o3.merge(state[['state_name','longitude']], on=['state_name'], how='inner')
o3 = o3.merge(state[['state_name','latitude']], on=['state_name'], how='inner')
o3 = o3[['state_name', 'date_local', 'longitude', 'latitude','aqi_o3']]
o3.date_local = pd.to_datetime(o3.date_local)

# PM10
pm10 = pm10.merge(state[['state_name','longitude']], on=['state_name'], how='inner')
pm10 = pm10.merge(state[['state_name','latitude']], on=['state_name'], how='inner')
pm10 = pm10[['state_name', 'date_local', 'longitude', 'latitude','aqi_pm10']]
pm10.date_local = pd.to_datetime(pm10.date_local)

#P M2.5
pm25 = pm25.merge(state[['state_name','longitude']], on=['state_name'], how='inner')
pm25 = pm25.merge(state[['state_name','latitude']], on=['state_name'], how='inner')
pm25 = pm25[['state_name', 'date_local', 'longitude', 'latitude','aqi_pm25']]
pm25.date_local = pd.to_datetime(pm25.date_local)
pm25 = pm25.dropna(axis=0)

st.header('Air Quality Index (AQI) - 2021')

# Separating Period
o3['week'] = pd.to_datetime(o3['date_local']).dt.isocalendar().week 
o3['month'] = pd.to_datetime(o3['date_local']).dt.month
o3['year'] = pd.to_datetime(o3['date_local']).dt.year

pm10['week'] = pd.to_datetime(pm10['date_local']).dt.isocalendar().week 
pm10['month'] = pd.to_datetime(pm10['date_local']).dt.month
pm10['year'] = pd.to_datetime(pm10['date_local']).dt.year

pm25['week'] = pd.to_datetime(pm25['date_local']).dt.isocalendar().week 
pm25['month'] = pd.to_datetime(pm25['date_local']).dt.month
pm25['year'] = pd.to_datetime(pm25['date_local']).dt.year

o3 = o3[['state_name', 'date_local', 'week','month','year','longitude', 'latitude','aqi_o3']]
pm10 = pm10[['state_name', 'date_local', 'week','month','year','longitude', 'latitude','aqi_pm10']]
pm25 = pm25[['state_name', 'date_local', 'week','month','year','longitude', 'latitude','aqi_pm25']]

# Merged the Table because it seems necessary
merged_em = o3.merge(pm10, on=['state_name','date_local','longitude','latitude'], how='inner')
merged_em = merged_em.merge(pm25, on=['state_name','date_local','longitude','latitude'], how='inner')
daily_merged_em = merged_em.groupby(by='date_local').mean()

#outlier
o3_q3, o3_q1 = np.percentile(o3['aqi_o3'], [75 ,25])
o3_iqr = o3_q3 - o3_q1
max_o3_iqr = o3_q3 + 1.5 * o3_iqr
min_o3_iqr = o3_q1 - 1.5 * o3_iqr
o3.drop(o3[o3['aqi_o3'] > max_o3_iqr].index, inplace = True)
o3.drop(o3[o3['aqi_o3'] < min_o3_iqr].index, inplace = True)
pm10_q3, pm10_q1 = np.percentile(pm10['aqi_pm10'], [75 ,25])
pm10_iqr = pm10_q3 - pm10_q1
max_pm10_iqr = pm10_q3 + 1.5 * pm10_iqr
min_pm10_iqr = pm10_q1 - 1.5 * pm10_iqr
pm10.drop(pm10[pm10['aqi_pm10'] > max_pm10_iqr].index, inplace = True)
pm25_q3, pm25_q1 = np.percentile(pm25['aqi_pm25'], [75 ,25])
pm25_iqr = pm25_q3 - pm25_q1
max_pm25_iqr = pm25_q3 + 1.5 * pm25_iqr
min_pm25_iqr = pm25_q1 - 1.5 * pm25_iqr
pm25.drop(pm25[pm25['aqi_pm25'] > max_pm25_iqr].index, inplace = True)


# Image
# st.image('https://www.epa.gov/sites/all/themes/epa/img/epa-standard-og.jpg', width=1000)

#Column in main Chart
# col_em_daily, col_em_weekly, col_em_monthly = st.columns(3)
# with col_em_daily:
#     #Daily Chart
#     st.subheader('US daily Air Quality Index in 2021')
#     number1_chart  = pd.DataFrame(data = [daily_merged_em['aqi_o3'], daily_merged_em['aqi_pm10'], daily_merged_em['aqi_pm25']]).T
#     st.line_chart(data=number1_chart, width=0, height=0, use_container_width=True)
# with col_em_weekly:
#     st.subheader('US Weekly Air Quality Index in 2021')
#     weekly_merged_em = merged_em.groupby(by='week').mean()
#     number2_chart  = pd.DataFrame(data = [weekly_merged_em['aqi_o3'], weekly_merged_em['aqi_pm10'], weekly_merged_em['aqi_pm25']]).T
#     st.line_chart(data=number2_chart, width=0, height=0, use_container_width=True)
# with col_em_monthly:
#     st.subheader('US Monthly Air Quality Index in 2021')
#     monthly_merged_em = merged_em.groupby(by='month').mean()
#     number3_chart  = pd.DataFrame(data = [monthly_merged_em['aqi_o3'], monthly_merged_em['aqi_pm10'], monthly_merged_em['aqi_pm25']]).T
#     st.line_chart(data=number3_chart, width=0, height=0, use_container_width=True)

# --------------

if page =='Top 5 states with Highest Emmision':
    st.header('Top 5 states with Highest Emmision')
    #State Rank
    highest_AQI_overall_per_state = pd.DataFrame(o3.groupby(by='state_name')['aqi_o3'].mean())
    hoa10ps = pd.DataFrame(pm10.groupby(by='state_name')['aqi_pm10'].mean())
    hoa25ps = pd.DataFrame(pm25.groupby(by='state_name')['aqi_pm25'].mean())
    highest_AQI_overall_per_state['aqi_pm10'] = hoa10ps['aqi_pm10']
    highest_AQI_overall_per_state['aqi_pm25'] = hoa25ps['aqi_pm25']

    # col_em_daily, col_em_weekly, col_em_monthly = st.columns(3)
    # with col_em_daily:
    #     #Daily Chart
    #     st.subheader('Top 5 states with Ozone Emission')
    #     x0 = pd.DataFrame(highest_AQI_overall_per_state['aqi_o3']).sort_values(by = 'aqi_o3', ascending=False).iloc[:,0].head()
    #     st.bar_chart(x0)
    # with col_em_weekly:
    #     st.subheader('Top 5 states with Particulate Matter 10 Emission')
    #     y0 = pd.DataFrame(highest_AQI_overall_per_state['aqi_pm10']).sort_values(by = 'aqi_pm10', ascending=False).iloc[:,0].head()
    #     st.bar_chart(y0)
    # with col_em_monthly:
    #     st.subheader('Top 5 states with Particulate Matter 2.5 Emission')
    #     z0 = pd.DataFrame(highest_AQI_overall_per_state['aqi_pm25']).sort_values(by = 'aqi_pm25', ascending=False).iloc[:,0].head()
    #     st.bar_chart(z0)
    st.subheader('Top 5 states with Ozone Emission')
    x0 = pd.DataFrame(highest_AQI_overall_per_state['aqi_o3']).sort_values(by = 'aqi_o3', ascending=False).iloc[:,0].head()
    st.bar_chart(x0)
    st.subheader('Top 5 states with Particulate Matter 10 Emission')
    y0 = pd.DataFrame(highest_AQI_overall_per_state['aqi_pm10']).sort_values(by = 'aqi_pm10', ascending=False).iloc[:,0].head()
    st.bar_chart(y0)
    st.subheader('Top 5 states with Particulate Matter 2.5 Emission')
    z0 = pd.DataFrame(highest_AQI_overall_per_state['aqi_pm25']).sort_values(by = 'aqi_pm25', ascending=False).iloc[:,0].head()
    st.bar_chart(z0)

elif page == 'Air Quality Index (AQI) Progress':
    st.header('Air Quality Index (AQI) Progress')
    #Daily Chart
    st.subheader('US daily Air Quality Index in 2021')
    number1_chart  = pd.DataFrame(data = [daily_merged_em['aqi_o3'], daily_merged_em['aqi_pm10'], daily_merged_em['aqi_pm25']]).T
    st.line_chart(data=number1_chart, width=0, height=0, use_container_width=True)

    # Weekly Chart
    st.subheader('US Weekly Air Quality Index in 2021')
    weekly_merged_em = merged_em.groupby(by='week').mean()
    number2_chart  = pd.DataFrame(data = [weekly_merged_em['aqi_o3'], weekly_merged_em['aqi_pm10'], weekly_merged_em['aqi_pm25']]).T
    st.line_chart(data=number2_chart, width=0, height=0, use_container_width=True)

    # Monthly Chart
    st.subheader('US Monthly Air Quality Index in 2021')
    monthly_merged_em = merged_em.groupby(by='month').mean()
    number3_chart  = pd.DataFrame(data = [monthly_merged_em['aqi_o3'], monthly_merged_em['aqi_pm10'], monthly_merged_em['aqi_pm25']]).T
    st.line_chart(data=number3_chart, width=0, height=0, use_container_width=True)

elif page == 'Air Quality Index (AQI) Limits':

    st.header('Air Quality Index (AQI) Limits')
    st.image('csv/o3_ct.png')
    st.subheader('Ozone (O3)')
    st.write('- The O3 consider Low in US if the O3 less than ',o3_q1)
    st.write('- The O3 consider medium in US if the O3 in between ',o3_q1,' and ', o3_q3)
    st.write('- The O3 consider High in US if the O3 more than ',o3_q3)

    st.subheader('Particulate Matter 10 (PM10)')
    st.image('csv/pm10_ct.png')
    st.write('- The PM10 consider Low in US if the PM10 less than ',pm10_q1)
    st.write('- The PM10 consider medium in US if the PM10 in between ',pm10_q1,' and ', pm10_q3)
    st.write('- The PM10 consider High in US if the PM10 more than ',pm10_q3)

    st.subheader('Particulate Matter 2.5 (PM2.5)')
    st.image('csv/pm25_ct.png')
    st.write('- The PM2.5 consider Low in US if the PM2.5 less than ',pm25_q1)
    st.write('- The PM2.5 consider medium in US if the PM2.5 in between ',pm25_q1,' and ', pm25_q3)
    st.write('- The PM2.5 consider High in US if the PM2.5 more than ',pm25_q3)

elif page == 'Monthly Air Quality Index (AQI) per State':   
    st.header('Monthly Air Quality Index (AQI) Average in each State')
    # st.subheader('See US Air Quality Index in 2021')
    st.map(o3)

    o3_mean_monthly = o3.groupby(['state_name','year','month'], as_index=False).mean()
    o3_mean_monthly = o3_mean_monthly.drop(['week'], axis=1)

    pm10_mean_monthly = pm10.groupby(['state_name','year','month'], as_index=False).mean()
    pm10_mean_monthly = pm10_mean_monthly.drop(['week'], axis=1)

    pm25_mean_monthly = pm25.groupby(['state_name','year','month'], as_index=False).mean()
    pm25_mean_monthly = pm25_mean_monthly.drop(['week'], axis=1)

    def category(score) :
        if score < 51:
            return 'Good'
        elif score < 101:
            return 'Moderate'
        elif score < 151:
            return 'Unhealthy for Specific Group'
        elif score < 201:
            return 'Unhealthy'
        elif score < 301:
            return 'Very Unhealthy'
        elif score < 500:
            return 'Hazardous'
        else:
            '-'

    o3_aqi_category = []
    for em in range(len(o3_mean_monthly )):
        o3_category_scan = category(o3_mean_monthly.loc[em,'aqi_o3'])
        o3_aqi_category.append(o3_category_scan)
    o3_mean_monthly ['aqi_o3_category'] = o3_aqi_category

    pm10_aqi_category = []
    for em in range(len(pm10_mean_monthly )):
        pm10_category_scan = category(pm10_mean_monthly .loc[em,'aqi_pm10'])
        pm10_aqi_category.append(pm10_category_scan)
    pm10_mean_monthly ['aqi_pm10_category'] = pm10_aqi_category

    pm25_aqi_category = []
    for em in range(len(pm25_mean_monthly )):
        pm25_category_scan = category(pm25_mean_monthly .loc[em,'aqi_pm25'])
        pm25_aqi_category.append(pm25_category_scan)
    pm25_mean_monthly ['aqi_pm25_category'] = pm25_aqi_category

    selected = st.selectbox('Select Month : ', options=o3['month'].unique())
    st.subheader('Ozone (O3)')
    st.image(f'csv/o3_{selected}.png')
    st.subheader('Particulate Matter 10 (PM10)')
    st.image(f'csv/pm10_{selected}.png')
    st.subheader('Particulate Matter 2.5 (PM2.5)')
    st.image(f'csv/pm25_{selected}.png')

elif page == 'Monthly Air Quality Index (AQI) per Emission':
    st.header('Monthly Air Quality Index (AQI) Average in each Emission')
    st.write('Air Quality Index (AQI) Average in Entire Year')

    aqi_o3_perem_monthly = o3.groupby(by='month')['aqi_o3'].mean()
    aqi_pm10_perem_monthly = pm10.groupby(by='month')['aqi_pm10'].mean()
    aqi_pm25_perem_monthly = pm25.groupby(by='month')['aqi_pm25'].mean()
    aqi_monthly_mean_per_em = pd.DataFrame(data = [aqi_o3_perem_monthly, aqi_pm10_perem_monthly, aqi_pm25_perem_monthly]).T

    ever_aqi_monthly = st.slider('Choose moth : ',1,12,1)
    filtered_monthly = aqi_monthly_mean_per_em[aqi_monthly_mean_per_em.index == ever_aqi_monthly]
    st.bar_chart(filtered_monthly)
    st.write('Description')
    aqi_monthly_mean_per_em[(aqi_monthly_mean_per_em.index == ever_aqi_monthly)]

    st.header('Critical emission Rank in 2021')
    st.write('Based on average of daily AQI')
    aqi_overal_mean_per_em = pd.DataFrame(columns=["emission","overal_mean"], data=[['O3', o3['aqi_o3'].mean()],['PM10',pm10['aqi_pm10'].mean()], ['PM2.5',pm25['aqi_pm25'].mean()]])
    aqi_overal_mean_per_em.set_index('emission', inplace = True)
    st.bar_chart(aqi_overal_mean_per_em)

elif page == 'Significant development of AQI Emissions':
    st.header('Significant development of AQI Emissions')
    st.write('Air Quality Index (AQI) difference in early and last year')

    st.subheader('Ozone Significance different in January and December')
    st.image('csv/497fb64e-3291-41e8-8b40-f8332e1d4075.png')
    O3daily_Dec = pd.DataFrame(o3[(o3['month'] == 12)]['aqi_o3'])
    o3_test = pd.DataFrame(o3.groupby(by=['month'])['aqi_o3'].mean())
    o3_0 = o3_test.iloc[0,0]
    o3_1 = o3_test.iloc[11,0]
    t_stat,p_val = stats.ttest_1samp(O3daily_Dec['aqi_o3'], o3_0)
    st.write(f'AQI Before : {o3_0}')
    st.write(f'AQI After : {o3_1}')
    if p_val < 0.05:
        st.write('There there is a significant difference.')
    else:
        st.write('There is no significant difference.')

    st.subheader('Particulate Matter 10 Significance different in January and December')
    st.image('csv/2982153e-2cf1-44b8-ad9e-7b6b69338cd3.png')
    O3daily_Dec = pd.DataFrame(o3[(o3['month'] == 12)]['aqi_o3'])
    o3_test = pd.DataFrame(o3.groupby(by=['month'])['aqi_o3'].mean())
    o3_0 = o3_test.iloc[0,0]
    o3_1 = o3_test.iloc[11,0]
    t_stat,p_val = stats.ttest_1samp(O3daily_Dec['aqi_o3'], o3_0)
    st.write(f'AQI Before : {o3_0}')
    st.write(f'AQI After : {o3_1}')
    if p_val < 0.05:
        st.write('There there is a significant difference.')
    else:
        st.write('There is no significant difference.')

    st.subheader('Particulate Matter 2.5 Significance different in January and December')
    st.image('csv/e4228332-14d7-4b49-a743-236c0f4f38b0.png')
    PM25daily_Dec = pd.DataFrame(pm25[(pm25['month'] == 12)]['aqi_pm25'])
    pm25_test = pd.DataFrame(pm25.groupby(by=['month'])['aqi_pm25'].mean())
    pm25_0 = pm25_test.iloc[0,0]
    pm25_1 = pm25_test.iloc[11,0]
    t_stat,p_val = stats.ttest_1samp(PM25daily_Dec['aqi_pm25'], pm25_0)
    st.write(f'AQI Before : {pm25_0}')
    st.write(f'AQI After : {pm25_1}')
    if p_val < 0.05:
        st.write('There there is a significant difference.')
    else:
        st.write('There is no significant difference.')






