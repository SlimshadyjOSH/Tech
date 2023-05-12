import pandas as pd
import streamlit as st
#import sys
#sys.path.append("c:/users/admin/new folder/lib/site-packages")
#import plotly.express as px


# read in csv file
filename = 'C:/Users/Admin/Desktop/obesity cleaned.csv'
df = pd.read_csv(filename)

# print original data
print("Original data:")
print(df)

# remove Number column
df.drop('Number', axis=1, inplace=True)

# filter for United States of America in Country column
df = df[df['Country'] == 'United States of America']

# filter for desired years in Year column
df = df[df['Year'].isin([1980, 1990, 2000, 2016])]

# filter for 'both sexes' in Sex column
df = df[df['Sex'] == 'Both sexes']

# reset index
df = df.reset_index(drop=True)

# print cleaned data
print("Cleaned data:")
print(df)

# Save the cleaned data to a new CSV file
df.to_csv("cleaned_data.csv", index=False)

# read in cleaned data
filename = "cleaned_data.csv"
df = pd.read_csv(filename)

# add CSS to change the background color of the Streamlit app to cream
st.markdown(
    """
    <style>
    body {
        background-color: #F5DEB3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# create title
st.title("Is The Consumption of High Fructose Corn Syrup (HFCS) Directly Related To The Rapid Rise of BMI In Americans?")

# Insert image
image_path = "C:/Users/Admin/Desktop/HFCStruths1.jpg"

# display the image
st.image(image_path, caption='HFCStruths1', use_column_width=True)

# what is this whole thing about?
st.markdown("*This data story aims to visualize the known data regarding the rapidly increasing rates of BMI among Americans and the consumption of HFCS to investigate if there is a direct cause and effect at play.*")

# What is BMI and what does it have to do with health?
st.title("What is BMI?")
st.write("Body Mass Index (BMI) is a person's weight in kilograms (or pounds) divided by the square of height in meters (or feet). A high BMI can indicate high body fatness. BMI screens for weight categories that may lead to health problems. If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range. If your BMI is 25.0 to 29.9, it falls within the overweight range. If your BMI is 30.0 or higher, it falls within the obese range.")

# create subtitle
st.markdown("<u><b>A look at the prevalence of obesity in the United States from 1980 to 2016 in adults over the age of 18 </b></u>.", unsafe_allow_html=True)

# create data frame
data = {'Country': ['United States of America', 'United States of America', 'United States of America', 'United States of America'],
        'Year': [1980, 1990, 2000, 2016],
        'BMI Confidence Interval': ['13.7 % [11.4-16.2]', '18.7 % [16.4-21.1]', '25.5 % [23.2-28.0]', '36.2 % [32.3-40.1]'],
        'Sex': ['Both sexes', 'Both sexes', 'Both sexes', 'Both sexes']}
df = pd.DataFrame(data)

# display table using streamlit
st.table(df)

# add hyperlink
st.markdown('<div style="text-align: center"><a href="https://apps.who.int/gho/data/node.main.A900A?lang=en" target="_blank">Source Of Data</a></div>', unsafe_allow_html=True)

# Explanation
st.write("We see that as the decades pass, the BMI confidence interval increases dramatically when comparing the years 1980 and 2016 side by side.")

# read in data from excel file
filename = r"C:\Users\Admin\Desktop\HFCS Grams.xlsx"
df = pd.read_excel(filename)

# create plot using plotly
fig = px.line(df, x="Year", y="HFCS Grams Per Capita", title="Consumption of High Fructose Corn Syrup in the United States")
fig.update_layout(xaxis={'tickangle': 90})

# display plot using streamlit
#st.plotly_chart(fig)


# add hyperlink
st.markdown('<div style="text-align:center"><a href="https://www.statista.com/statistics/328893/per-capita-consumption-of-high-fructose-corn-syrup-in-the-us/" target="_blank">Source Of Data</a></div>', unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse',False)

# Explanation of findings.
st.write(" The data shows that the consumption of HFCS from the year 2000-2019 in America has been on a decline indicating that there is no direct correlation between the rise of obesity and consumption of high fructose corn syrup. At first glance it may appear as though there is no direct cause and effect, however it is a well known fact that the consumption of excess sugar does lead to weight gain. Just becuase the consuption of HFCS has decreased does not nessarly mean it is not responsible in any way shape or form for the severe increase in Obesity. So is there any relation between the two ? ")

#Subtitle 
st.title('Visual Representation of Combined Data Sets')

# create a dataframe for interactive table
import altair as alt

# create a dataframe
data = {
    'Year': range(2000, 2017),
    'HFCS Grams Per Capita Consumed': [28350, 28214, 28350, 27488, 27034, 26717, 26218, 25356, 23904, 22544, 21594, 21183, 20775, 19822, 19686, 19278, 18779],
    'Percentage of Population': ['{:.1f}%'.format(val) for val in [25.5, 26.2, 26.9, 27.6, 28.3, 29, 29.7, 30.3, 31, 31.7, 32.3, 33, 33.6, 34.3, 34.9, 35.6, 36.2]],
    'BMI Confidence Interval': ['23.2-28.0', '23.9-28.7', '24.6-29.4', '25.3-30.1', '26.0-30.8', '26.7-31.5', '27.2-32.2', '27.9-32.9', '28.5-33.6', '29.0-34.3', '29.6-35.1', '30.1-35.9', '30.6-36.7', '31.0-37.6', '31.4-38.4', '31.9-39.3', '32.3-40.1']
}

df = pd.DataFrame(data)

# create a slider for the year
selected_year = st.slider('Select a year', 2000, 2016)

# filter the dataframe based on the selected year
filtered_df = df[df['Year'] == selected_year]

# create an Altair chart
chart = alt.Chart(filtered_df).mark_bar().encode(
    x='Year',
    y=alt.Y('HFCS Grams Per Capita Consumed', scale=alt.Scale(domain=[17000, max(df['HFCS Grams Per Capita Consumed'])])),
    color='Percentage of Population',
    tooltip=['BMI Confidence Interval','HFCS Grams Per Capita Consumed']
).properties(
    width=600,
    height=400,
    title=f'HFCS Grams Per Capita Consumed and The BMI Confidence Interval For The Year {selected_year}'
)

# display the chart
st.altair_chart(chart, use_container_width=True)

#Chart Explanation
st.write('The interactive bar chart above visualizes how as each year progresses the HFCS consumed per capita decreses all while the BMI confidence interval increases along with the percentage of the population. You can look at the the data more in detail by hovering over the chart to see the specific data points of each year.')

#Conclusion
st.title('Conclusion')
st.write('In conclusion the data shows that while the rate of obesity amoung americans has rapidly increased,the consumption of HFCS has been on a steady decline. According to "clevelandclinic.org", it has been proven that the consumption of HFCS can infact contribute to diabetes and obesity as it causes a signifcant incrase in apetite compared to regualr cane sugar. This data is a classic case of "corelation does not mean causation".There are various other triggers along with the consumption of HFCS such as diet, smoking and having a genetic predisposition to the disease that can cause obesity. It is not the consumption of high fructose corn syrup alone that causes obesity, it simply is a contributing factor.')
st.markdown('<div style="text-align: center"><a href="https://health.clevelandclinic.org/avoid-the-hidden-dangers-of-high-fructose-corn-syrup-video/#:~:text=Increases%20appetite%2C%20promotes%20obesity,liver%20disease%2C%E2%80%9D%20says%20Dr." target="_blank">Source Of Data</a></div>', unsafe_allow_html=True)




