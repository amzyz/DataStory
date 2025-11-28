import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.write("""
# Are men really more lonely? 
## A data-driven investigation into the Male Loneliness Epidemic
#### [Youtube Link to Overview and Walkthrough](https://youtu.be/mJwZwFGt5OU)


In this data story, I will be investigating the [male loneliness epidemic](https://wou.edu/westernhowl/the-male-loneliness-epidemic/) and seeing if there are any truths to the so-called epidemic. My original, broad idea was to explore happiness (using the world happiness dataset), friendships, and close relationships in general, because of Gallup's finding that [life satisfaction is at an all-time low](https://news.gallup.com/poll/655493/new-low-satisfied-personal-life.aspx). 

As I was doing research, I was inspired by this article about [boys and friendships](https://melindawmoyer.substack.com/p/the-epidemic-of-male-loneliness) to look at interpersonal relationships and focus on connections rather than often-cited factors like income for indicators of happiness. 

In the past, I've wondered: Do men and women socialize differently? What are the differences in the different relationship styles? This [article](https://ifstudies.org/blog/male-friendships-are-not-doing-the-job) talks about the growing concern around whether boys and men confide in friends. Personally, I have had a lot of conversations with my friends about what it means to have close friendships, and I have noticed a pointed difference in the way my male friends describe their relationships to me versus how my female friends describe them to me. 

I see a lot of discourse on Twitter (now X) about how this topic is sensationalized and positioned to blame women as part of a misogynistic narrative. While this may be true, I want to analyze this from a standpoint that looks at gender differences in the realms of social interactivity, including friendships and romantic relationships. 
""") 

img_url = "https://i.imgur.com/1OgcrQJ.jpeg"  
st.image(img_url, caption="Twitter 'Discourse'")


st.write(""" This data story will take you through my research process: from the initial ideas stated, to the data I was able to find (and what I did _not_ find), and the ways in which the data reshaped my research questions as I moved forward. 

My initial research question(s): What are the biggest factors in recent years of this emerging "male loneliness epidemic"? Are there really pointed differences in how men and women interact interpersonally? 

Starting by looking at general trends of happiness, the initial phase of data analysis shows two key findings: Happiness in the United States has been on the decline since 2005, and the decline has been characterized with record-low satisfaction in 2025, yet a rise in social support.
""")

## LADDER SCORE (OVERALL HAPPINESS)

st.title("General Happiness Trends in the U.S. and Life Satisfaction")
st.subheader("They've been on the decline since 2010.")

st.write("""
First, using the World Happiness Dataset [1], I want to analyze the change in the happiness ladder score over time. _The ladder score is a measure of happiness based on responses to the Cantril Ladder question that asks respondents to think of a ladder, with the best possible life for them being a 10, and the worst possible life being a 0._ I want to see if there is a notable change in happiness over time. My data gives me various scores for the years 2005 to 2024, and I will be focusing on the United States and within that, the years 2010-2024. I chose these years because I think it would provide a more up-to-date look at the data. I also want to see if there is a notable change in the years after 2012, when popular dating apps like Tinder and Hinge were released.
""")

st.markdown("<sub>[1] Islam, S. (2023, September 9). World happiness report (till 2023). Kaggle. https://www.kaggle.com/datasets/sazidthe1/global-happiness-scores-and-factors </sub>", unsafe_allow_html=True)

happiness_data_2005 = pd.read_csv('2005happiness.csv', encoding="ISO-8859-1")
happiness_data_2005.head()
# I just want U.S. 
us_df = happiness_data_2005[happiness_data_2005["Country name"] == "United States"]
# name ladder column to match the other dataset: "ladder score"
df1 = us_df.rename(columns={"Life Ladder": "Ladder score"})
df1.head(20)

happiness_data_2024 = pd.read_csv('2024happiness.csv', encoding="ISO-8859-1")
happiness_data_2024.head()

us_df_2024 = happiness_data_2024[happiness_data_2024["Country name"] == "United States"]
us_df_2024.head()

df1_1 = df1[["year", "Ladder score", "Social support"]]
df2 = us_df_2024[["Ladder score", "Social support"]]

# Merge the two dataframes
full_df = pd.concat([df1_1, df2])
full_df["year"] = full_df["year"].fillna(2024)
# full_df.head(20)

# I want just the years 2010-2024, because the popular dating apps like Tinder and Hinge came out in 2012, so I want to see if there is
#  notable change before and after the apps came out

filter_df = full_df.loc[(full_df["year"] >= 2010) & (full_df["year"] <= 2024)]

# Display Subheader
st.subheader("On average, people would rate their lives as a 6.7 out of 10 as of 2024.")

# Plot
fig, ax = plt.subplots()
ax.plot(filter_df["year"], filter_df["Ladder score"], label="Ladder Score", color="b", marker="o", linestyle="-")
ax.set_xlabel("Year")
ax.set_ylabel("Ladder Score")
ax.set_title("Change in Ladder Score Over Time")
ax.legend()

# Show the plot in Streamlit
st.pyplot(fig)


st.write(""" Since I want to focus on interpersonal relationships and connections, I will focus on two measures in the dataset: Social support and the ladder score.
_The social support category points to "The national average of binary responses (either 0 or 1 representing No/Yes) to the question about having relatives or friends to count on in times of trouble._" """)

## SOCIAL SUPPORT GRAPH

st.subheader("Despite the decline in happiness, social support is on the rise.")
fig, ax = plt.subplots()
ax.plot(filter_df["year"], filter_df["Social support"], label="Social support", color="b", marker="o", linestyle="-")

ax.set_xlabel("Year")
ax.set_ylabel("Social Support Score")
ax.set_title("Change in Social Support Over Time")

ax.legend()

# Display the plot
st.pyplot(fig)

st.write(""" 
The amount of social support increasing was a good sign that people have support systems, which may indicate lower levels of loneliness. I approach this research with the assumption that companionship and connection are key to happiness and essentially the opposite of loneliness, so I was surprised to see that the ladder score was on the decline. So is life satisfaction, according to Gallup's Mood of the Nation poll that found that life satisfaction is at an all-time low.

""")

## LIFE SATISFACTION GRAPH

st.subheader("Life Satisfaction is at an all-time low.")

satisfaction_data = pd.read_csv('Personal_Life_Satisfaction.csv')
satisfaction_data.columns = ["Year", "Very Satisfied (%)"]

# Cleaning the dataset
satisfaction_data["Year"] = satisfaction_data["Year"].astype(int)

# plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    satisfaction_data["Year"], 
    satisfaction_data["Very Satisfied (%)"], 
    marker='o', linestyle='-', color='b', label="Very Satisfied (%)"
)


ax.set_xlabel("Year")
ax.set_ylabel("Percentage of 'Very Satisfied'")
ax.set_title("Change in Personal Life Satisfaction Over the Years")
ax.tick_params(axis='x', rotation=45) 
ax.grid(True)
ax.legend()

st.pyplot(fig)


st.write(""" I'm seeing that life satisfaction is at an all-time low this year. It peaked in 2020, which is interesting considering the pandemic. I can also see that the percentage of people who are 'very satisfied' has been steadily dropping since then. However, it is worthy to keep in mind that just because people are not "very satisfied" with their lives, does not mean they are deeply unhappy. [Gallup's poll](https://news.gallup.com/poll/655493/new-low-satisfied-personal-life.aspx) revealed that another 37% of Americans today say they are “somewhat satisfied” with their personal life, while 9% are “somewhat” dissatisfied and 8% are “very” dissatisfied[2]. """)

st.markdown("<sub>[2] Brenan, M. (2025, January 29). New low in U.S. “very satisfied” with personal life. Gallup. https://news.gallup.com/poll/655493/new-low-satisfied-personal-life.aspx </sub>", unsafe_allow_html=True)

st.subheader("Conclusions from the data so far...")

st.write(""" 
This data was a good starting point for my research, but I wanted to see if there were any gendered differences in the data. From analyzing the World Happiness Survey and Gallup's annual Mood of the Nation poll, I can see that generally, peoples' satisfaction levels have been decreasing over the years.

"In light of the emergence and popularization of the male loneliness epidemic, there has been discourse regarding its legitimacy, specifically in regards to the exclusive focus on men when it comes to discussing the general loneliness epidemic. Disparities in loneliness have been found to age, race, financial status, sexuality and disability, but, according to some critics, not for gender. The measurement of loneliness as well as the interpretation of select studies and statistics has also been cited as reasons for skepticism.[3]" """)

st.markdown("<sub>[3]Ansley, C. (n.d.). The Male Loneliness Epidemic. Western Oregon University. https://wou.edu/westernhowl/the-male-loneliness-epidemic/ </sub>", unsafe_allow_html=True)

st.write("""
Is the male loneliness epidemic just something I hear about on Twitter or is it valid that there is a gendered difference...and what can be attributed to this.. I feel like it's worth exploring. 

I found the General Social Survey, which is a large dataset that had survey responses from 1972 to 2024 that asked questions about socializing with friends, spending time at bars, calling best friends, and having a romantic partner. I had hoped to find data that was recent, but the website had a disclaimer that they had data up to 2022. That being said, I was able to find some data that was interesting and relevant to my research question.

### Questions
I want to try to answer this series of questions that relate to my original research question. 

* Is there a measurable gender difference in reported loneliness and life satisfaction?
* How are social factors like time with friends and the number of close friends different between men and women?


## Pitfalls with Cleaning and Accessing Data
The data I wanted to look at (General Social Survey Data, American Time Survey Data) did not have data in formats that were timely and publically available. I also did not find any publically available datasets about dating sites. 

"What did you expect to find, what wasn’t there? How did what you DID find change your thinking about the data? How will the realities of the data be foundational to your visualization? "

These are questions from the assignment that I will now answer. I expected to find really definable, gendered data that was RECENT that would lead me right to my answer. Alas, that did not really happen. Although there are reports out from centers like Pew Research and Gallup about men, women, and dating and socialization, this data was not publically available or in a format that I could wrangle, clean, and analyze. Even through searching on Kaggle which has mostly clean datasets from other people, I did not find anything recent- the best I could find was edited 10 years ago. The realities of the data show me that I need to narrow the scope of my question. I need to see how men and women socialize differently, and I will pivot to focus on friends and time spent with friends.

### Pivoting...
I will need to use reports that are available. I found a feature of the General Social Survey (GSS) that allows me to choose variables then tabulate them multivariably or cross-tabulate. In this stage, I'm just going to select by year from 2010 to 2022 and use relevant variables like socialization with friends and community for columns and sex (M/F) for the rows.

Also, I've noticed that some data does not really take non-binary people into account and simply uses "sex" as Male or Female. Very binary terms, which could exclude some people. But, my question is pretty binary, and so is the whole "male loneliness" characterization that I am investigating. It's not ideal, but I will be using the binary terms for the purposes of this project. Tthe question itself, and really the whole _male loneliness_ part seems to capture people who identify as men. It does not quite capture the full picture of loneliness for people who don't identify with binary terms.

### Another pitfall with data
This process was arduous, surprisingly so. I had to get creative to get this data to be usable for the purposes of this project. In the screenshot here, you can see my cross-tabulation data was not exported correctly into excel, which I could not figure out for the life of me. """)

img_url = "https://i.imgur.com/YXLHhZu.png"  
st.image(img_url, caption="Excel cell with html??")


st.write("""Because of this issue, I decided I would take the data given by the cross-tabulation function and manually insert it into a dataframe so I can create visualizations. I'm picking variables like socialization with friends, number of friends, number of times they call or visit friends, etc. in the GSS survey[3] to determine socialization levels and directly compare how men and women behave within each socialization category. The reason I am choosing these variables is because I want to see if there are any gendered differences in how people socialize. These are the columns I would filter the entire dataset down to, and I would filter the rows by gender.
""")

st.markdown("<sub>[3]Davern, M., Bautista, R., Freese, J., Herd, P., & Morgan, S. L. (2024). General Social Survey, 1972-2024 [Machine-readable data file]. NORC at the University of Chicago. https://gssdataexplorer.norc.org </sub>", unsafe_allow_html=True)


st.title("Exploring Gendered Differences in Socializing Habits")

# Socializing with Friends Section
st.header("Socializing with Friends")
st.markdown("""
### How often do men and women socialize with their friends?
Here we explore the gender differences in social interactions with friends. I used side-by-side bar charts to show 
""")

# Data: Evenings with Friends
data_friends = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "ALMOST DAILY": [860, 668, 1528],
    "SEV TIMES A WEEK": [3941, 3967, 7908],
    "SEV TIMES A MNTH": [3988, 4562, 8551],
    "ONCE A MONTH": [4369, 5037, 9406],
    "SEV TIMES A YEAR": [4079, 4106, 8186],
    "ONCE A YEAR": [1642, 1628, 3270],
    "NEVER": [1813, 2434, 4247],
    "Total": [20693, 22403, 43096]
}

crosstab_evening_socialization = pd.DataFrame(data_friends)

# Data: Spending Evenings at a Bar
data_bar = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "ALMOST DAILY": [386, 101, 487],
    "SEV TIMES A WEEK": [2118, 1050, 3168],
    "SEV TIMES A MNTH": [1866, 1361, 3227],
    "ONCE A MONTH": [2361, 2088, 4449],
    "SEV TIMES A YEAR": [2671, 2747, 5418],
    "ONCE A YEAR": [2495, 2718, 5214],
    "NEVER": [8766, 12328, 21094],
    "Total": [20663, 22394, 43057]
}

df_socbar = pd.DataFrame(data_bar)

# Function to Compute Percentages
def compute_percentage(df):
    df_percentage = df.copy()
    for col in df.columns[1:-1]:  
        df_percentage[col] = (df[col] / df["Total"]) * 100
    return df_percentage

df_friends_pct = compute_percentage(crosstab_evening_socialization)
df_bar_pct = compute_percentage(df_socbar)

def plot_graphs(df, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    df_filtered = df[df["SEX (respondents sex)"] != "Total"]
    df_filtered.set_index("SEX (respondents sex)").drop(columns=["Total"]).T.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Frequency of Activity")
    ax.legend(title="Gender")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

st.header("Socializing with Friends")
plot_graphs(df_friends_pct, "Socializing with Friends by Gender")


st.write("""The data shows that men are slightly more likely than women to socialize almost daily or several times a week. Women are slightly more likely to socialize several times a month or once a month. Women are more likely than men to report that they *never* socialize with friends.""")

# Spending Evenings at a Bar 
st.header("Spending Evenings at a Bar")
st.markdown("""
### How often do men and women spend time at bars?
This visualization explores the differences in bar-going habits by gender.
""")

plot_graphs(df_bar_pct, "Spending Evenings at a Bar by Gender")

st.write("""Men are significantly more likely to visit bars frequently (daily, weekly, or monthly). More than half of women (55%) report never going to bars, compared to 42.4% of men.

Results show that men and women have similar overall socialization patterns. The data suggests that men are more likely to visit bars more than women, although this may be due to cultural or societal factors. Women and men may like going to different social settings. For the issue of the Male Loneliness Epidemic, further analysis is needed to determine if there is a gendered difference in the number of close friends people have. I also want to look at the frequency of calling and visiting friends, because I think that is an important factor in the qualities of social connections.""")

st.title("Do Men and Women Spend Equal Amounts of Quality Time With Their Friends?")

st.write("""Next, I'll look at the frequency of which men and women call and visit their best friends. I think effort put into friendships through quality time and interaction is an important factor of the quality of socializtion, because if people are in contact with a close friend, they may not be as lonely as someone who is not. It also can say something about the support men and women give to their prospective friends, and the level of support they get back. This ties in to the idea of loneliness because it measures the amount of communication and contact through phone calls and visits.""")

# Calling Best Friend Section
st.header("How Often Do People Call Their Best Friend?")

data_bf_call = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "Daily": [69, 105, 173],
    "At least several times a week": [145, 131, 275],
    "At least once a week": [132, 111, 243],
    "At least once a month": [80, 95, 175],
    "Several times a year": [47, 34, 81],
    "Less often": [39, 13, 52],
    "Never": [29, 17, 46],
    "Total": [541, 505, 1046]
}

df_bf_call = pd.DataFrame(data_bf_call)

df_filtered = df_bf_call[df_bf_call["SEX (respondents sex)"] != "Total"]

df_percentage = df_filtered.copy()
for col in df_filtered.columns[1:-1]:  # Skip first column (gender) and last column (total)
    df_percentage[col] = (df_filtered[col] / df_filtered["Total"]) * 100

df_percentage = df_percentage.drop(columns=["Total"])


df_transposed = df_percentage.set_index("SEX (respondents sex)").T


fig, ax = plt.subplots(figsize=(10, 6))
df_transposed.plot(kind="bar", ax=ax)
ax.set_title("Frequency of Calling Best Friend by Gender (Percentage)")
ax.set_ylabel("Percentage")
ax.set_xlabel("Frequency of Calling")
ax.legend(title="Gender")
plt.xticks(rotation=45, ha="right")

st.pyplot(fig)


st.write(""" This shows that women are more likely to call their best friend daily. Men and women are nearly identical in "several times a week" and "once a week" categories, and men are slightly more likely to call "several times a year" or "less often".""")

st.header("How Often Do People Visit Their Best Friend?")

# Interaction Data
data_interaction = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "He or she lives in the same household as I do": [18, 11, 29],
    "Daily": [58, 44, 102],
    "At least several times a week": [119, 95, 214],
    "At least once a week": [133, 123, 256],
    "At least once a month": [90, 102, 192],
    "Several times a year": [82, 92, 174],
    "Less often": [55, 42, 97],
    "Never": [4, 7, 11],
    "Total": [559, 516, 1075]
}
df_interaction = pd.DataFrame(data_interaction)


df_interaction_filtered = df_interaction[df_interaction["SEX (respondents sex)"] != "Total"]

df_interaction_transposed = df_interaction_filtered.set_index("SEX (respondents sex)").drop(columns=["Total"]).T


# Plot
fig, ax = plt.subplots(figsize=(10, 6))
df_interaction_transposed.plot(kind="bar", ax=ax)
ax.set_title("Frequency of Visiting Best Friend by Gender")
ax.set_ylabel("Count")
ax.set_xlabel("Frequency of Visiting")
ax.legend(title="Gender")
plt.xticks(rotation=45, ha="right")


st.pyplot(fig)

st.write("""Men and women have similar visitation patterns with their best friends. Men are slightly more likely to visit frequently, while women are slightly more likely to visit monthly or a few times a year. This does not support the notion that men are more lonely than women if they are spending time with their friends at similar rates.""")

# NEEDY FRIEND PART

st.header("Contributions to a Needy Friend by Gender")

data_needy_frd = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "YES": [194, 255, 449],
    "NO": [479, 476, 955],
    "Total": [673, 731, 1404]
}
df_needy_frd = pd.DataFrame(data_needy_frd)

df_needy_frd_filtered = df_needy_frd[df_needy_frd["SEX (respondents sex)"] != "Total"]

df_needy_frd_transposed = df_needy_frd_filtered.set_index("SEX (respondents sex)").drop(columns=["Total"]).T

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
df_needy_frd_transposed.plot(kind="bar", ax=ax)
ax.set_title("Contributed to a Needy Friend by Gender")
ax.set_ylabel("Count")
ax.set_xlabel("Contribution Status")
ax.legend(title="Gender")
plt.xticks(rotation=45, ha="right")

st.pyplot(fig)

st.write("Women in this dataset reported helping their friends at a slightly higher rate (34.9%) than men (28.8%). Among those who did help a friend, the split is somewhat gendered (more women reported helping). A significant portion of both men and women said 'No' to helping a needy friend (~65-70%). In this dataset, it supports that more women helped out a needy friend, but I would not say it is a significant difference to draw any conclusions from. """)


st.subheader("Now, I want to look at the number of close friends and see if more men report having few close friends more than women. I'll look at the number of romantic partners, too. ")

# Number of Close Friends Section
st.header("Number of Close Friends by Gender")

data_friends_count = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "No other close friends": [107, 76, 183],
    "1": [35, 25, 60],
    "2": [46, 55, 100],
    "3": [65, 68, 133],
    "4": [57, 38, 96],
    "5": [64, 58, 122],
    "6": [34, 24, 58],
    "7": [8, 9, 16],
    "8": [19, 16, 35],
    "9": [5, 5, 10],
    "10": [57, 58, 115],
    "11": [0, 0, 0],
    "12": [14, 10, 24],
    "14": [1, 0, 1],
    "15": [15, 27, 42],
    "16": [0, 1, 1],
    "18": [2, 1, 3],
    "19": [0, 0, 0],
    "20": [21, 18, 38],
    "21": [1, 0, 1],
    "24": [0, 2, 2],
    "25": [17, 9, 26],
    "30": [6, 11, 17],
    "35": [4, 2, 6],
    "40": [2, 1, 4],
    "45": [0, 3, 3],
    "50": [13, 10, 23],
    "60": [1, 3, 5],
    "70": [0, 1, 1],
    "75": [1, 0, 1],
    "Total": [597, 532, 1129]
}

df_close_friends = pd.DataFrame(data_friends_count)

df_filtered = df_close_friends[df_close_friends["SEX (respondents sex)"] != "Total"]
df_filtered = df_filtered.set_index("SEX (respondents sex)").astype(int)

# Grouping by bins of 10 
bins = list(range(0, 81, 10))  #
bin_labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

grouped_data = {}
for gender in df_filtered.index:
    grouped_values = []
    for i in range(len(bins) - 1):
        col_range = [str(num) for num in range(bins[i], bins[i+1]) if str(num) in df_filtered.columns]
        grouped_values.append(df_filtered.loc[gender, col_range].sum())
    grouped_data[gender] = grouped_values

df_grouped = pd.DataFrame(grouped_data, index=bin_labels)


# Plot 
fig, ax = plt.subplots(figsize=(10, 6))
df_grouped.plot(kind="bar", ax=ax)
ax.set_title("Number of Close Friends by Gender (Grouped by 10s)")
ax.set_ylabel("Count")
ax.set_xlabel("Number of Close Friends (Grouped)")
ax.legend(title="Gender")
plt.xticks(rotation=45, ha="right")

st.pyplot(fig)

st.write(""" In this dataset, men are more likely than women to report having no close friends. Women in the dataset are slightly more likely than men to report having 10+ close friends. Men are more likely to fall into the "mid-range" (2-5 close friends). This data is interesting because it shows that men may be at a higher risk for isolation, and women may have broader support networks. The visualizations from the data I was able to gather may suggest that men do not have as many friends as women, which could be a harmful narrative to spread. """)


# Romantic Partner Section

st.title("Romantic Partner Status by Gender")

# Romantic Partner Data
data_romance = {
    "SEX (respondents sex)": ["MALE", "FEMALE", "Total"],
    "YES": [250, 257, 507],
    "NO": [267, 382, 649],
    "HAS SAME GENDER PARTNER": [2, 1, 3],
    "Total": [519, 640, 1159]
}

df_romance = pd.DataFrame(data_romance)


df_romance_filtered = df_romance[df_romance["SEX (respondents sex)"] != "Total"].drop(columns=["HAS SAME GENDER PARTNER"])


df_romance_transposed = df_romance_filtered.set_index("SEX (respondents sex)").drop(columns=["Total"]).T


fig, ax = plt.subplots(figsize=(10, 6))
df_romance_transposed.plot(kind="bar", ax=ax)
ax.set_title("Romantic Partner Status by Gender")
ax.set_ylabel("Count")
ax.set_xlabel("Romantic Partner Status")
ax.legend(title="Gender")
plt.xticks(rotation=45, ha="right")

st.pyplot(fig)

st.write(""" In this dataset, men are slightly more likely than women to report having a romantic partner, with *48.2% of men* reporting having a partner and *40.2% of women* reporting to have a partner. I would not say that this is a significant difference to draw any conclusions from.""")

st.subheader("Quantity does not equal quality.")
st.write("""Studies show that the sheer number of [close friends](https://libarts.source.colostate.edu/are-americans-suffering-a-friendship-crisis-study-shows-we-dont-need-more-friends-just-more-time-with-those-we-already-have/) and the presence of a [romantic partner](https://www.nathanwhudson.com/vita/pdf/Hudson%20et%20al.,%202020c.pdf) does not quite indicate the quality of ones' life and wellbeing.""")


st.write (""" As a 20-something college student AND chronically online person, I'd continue this line of questioning and research by looking at the rise of [dating apps](https://www.pewresearch.org/internet/2020/05/08/dating-and-relationships-in-the-digital-age/) and how they've shifted the way we socialize. I want to see if I can find whether or not these apps are truly successful in helping people find connections, and whether their meteoric rise since the 2010s to now correlate at all with our general unhappiness as a society. In my personal opinion and experience with talking to friends who've tried them, it feels like they've made it easier to meet people, but harder to form meaningful connections. It's definitely a topic I'd like to explore further in other iterations of this project, by scraping data from the apps themselves and collecting more survey information. """)


st.subheader("Questions to Explore in the Future (re. dating apps and romantic connections)")
st.write ("""
* What role do dating apps play in social connection, and do they correlate with lower life satisfaction?
* Are shifts in marriage rates, friendships, and personal relationships indicators of male loneliness?
* How do external factors like cultural expectations, economic conditions, and the pandemic contribute to male loneliness?
""")

st.title("Final Conclusions")
st.write("""

Socialization and quality of connections are complex. These findings cannot indicate causality between the habits of socialization to increased or decreased lonelineness, nor do they point to the idea that men are really _more_ lonely than women. While I was able to find some data that supported the idea that women may have broader friendship networks and more close friends, I was not able to find any data that directly supported the idea that men are more lonely than women or have lesser quality friendships. Women may be more likely to reach out to friends and help each other, and this could be due to social/cultural expectations. I think that this is a topic that is worth exploring further, and I would like to continue this project by looking at the role of dating apps in social connection and how they correlate with lower life satisfaction (if they do at all). 

""")

st.subheader("References")
st.write("""
Ansley, C. (n.d.). The Male Loneliness Epidemic. Western Oregon University. https://wou.edu/westernhowl/the-male-loneliness-epidemic/

Brenan, M. (2025, January 29). New low in U.S. “very satisfied” with personal life. Gallup. https://news.gallup.com/poll/655493/new-low-satisfied-personal-life.aspx 

Cox, D. (2023, March 28). Male friendships are not doing the job. Institute for Family Studies. https://ifstudies.org/blog/male-friendships-are-not-doing-the-job

Davern, M., Bautista, R., Freese, J., Herd, P., & Morgan, S. L. (2024). General Social Survey, 1972-2024 [Machine-readable data file]. NORC at the University of Chicago. https://gssdataexplorer.norc.org

Goddard, I. (2025, January 16). Men, women and Social Connections. Pew Research Center. https://www.pewresearch.org/social-trends/2025/01/16/men-women-and-social-connections/

Hudson, N. W., Lucas, R. E., & Donnellan, M. B. (2019). The highs and lows of love: Romantic Relationship Quality Moderates whether spending time with one’s partner predicts gains or losses in well-being. Personality and Social Psychology Bulletin, 46(4), 572–589. https://doi.org/10.1177/0146167219867960 

Islam, S. (2023, September 9). World happiness report (till 2023). Kaggle. https://www.kaggle.com/datasets/sazidthe1/global-happiness-scores-and-factors

Moyer, M. (2023, August 8). The epidemic of male loneliness. Now What. https://melindawmoyer.substack.com/p/the-epidemic-of-male-loneliness 

Nick, S. (2024, October 24). Friendship Crisis? Study Says It’s Quality, Not Quantity With Friendships. Source. https://libarts.source.colostate.edu/are-americans-suffering-a-friendship-crisis-study-shows-we-dont-need-more-friends-just-more-time-with-those-we-already-have/ 
""")