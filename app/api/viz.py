from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px

router = APIRouter()

reddits = {'learnSQL', 'MovieSuggestions', 'dating_advice', 'philosophy', 'worldnews', 'tifu', 'patientgamers',
           'explainlikeimfive', 'OutOfTheLoop', 'books', 'ProRevenge', 'TellMeAFact', 'bestoflegaladvice',
           'talesfromtechsupport', 'TalesFromRetail', 'britishproblems', 'whowouldwin', 'WritingPrompts', 'AskMen',
           'AskWomen', 'askscience', 'newreddits', 'HailCorporate', 'boringdystopia', 'bestof', 'KarmaCourt',
           'AmItheAsshole', 'RedditWritesSeinfeld', 'nosleep', 'pcmasterrace', 'learnpython', 'politics',
           'LifeProTips', 'Jokes', 'gaming'}


# types of visualizations to create - using Logistic Regression
# 1. Number of posts from each subreddit used for training model

# 2. Subreddit + Avg. Length of Post for each (for prediction 5)

# 3. PDP Plot of Top 5 subreddits - to see how close to being put in other subreddits
# Isolate vs Interact (PDP plot types) - Using LR cant use this

@router.get('/viz_trained')
async def viz(subreddit):
    """ Various Visualizations for the DS build """

    # def trained_on():
    # shows the number of tweets in each subreddit to learn off of
    fig = px.scatter(df, x=reddits, y=len(get_data(reddit, n=300)))
    fig.show()
    return fig.to_json()


# @router.get('/viz_trained')
# async def viz(subreddit):
#     def avg_len():
#         training = get_data(reddits, n=300)
#         for reddit in reddits:
#             lengths = []
#             _ = avg(len(training.Post))
#             lengths.append(_)
#
#         return lengths
#         # now make visualization using lengths list

# @router.get('/viz/{reddits}')
# async def viz(reddits: str):
#     """
#     Visualize state unemployment rate from [Federal Reserve Economic Data](https://fred.stlouisfed.org/) 📈
#
#     ### Path Parameter
#     `statecode`: The [USPS 2 letter abbreviation](https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations#Table)
#     (case insensitive) for any of the 50 states or the District of Columbia.
#
#     ### Response
#     JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
#     """
#
#     # Validate the state code
#     statecodes = {
#         'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
#         'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut',
#         'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida',
#         'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
#         'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky',
#         'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
#         'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
#         'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
#         'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire',
#         'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
#         'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
#         'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
#         'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
#         'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
#         'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
#         'WI': 'Wisconsin', 'WY': 'Wyoming'
#     }
#     statecode = statecode.upper()
#     if statecode not in statecodes:
#         raise HTTPException(status_code=404, detail=f'State code {statecode} not found')
#
#     # Get the state's unemployment rate data from FRED
#     url = f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={statecode}UR'
#     df = pd.read_csv(url, parse_dates=['DATE'])
#     df.columns = ['Date', 'Percent']
#
#     # Make Plotly figure
#     statename = statecodes[statecode]
#     fig = px.line(df, x='Date', y='Percent', title=f'{statename} Unemployment Rate')
#
#     # Return Plotly figure as JSON string
#     return fig.to_json()
