import logging
import random

from fastapi import APIRouter, FastAPI
import pandas as pd
from pydantic import BaseModel, Field, validator

# app = FastAPI() in main.py

log = logging.getLogger(__name__)
router = APIRouter()


class Post(BaseModel):
    """Use this data model to parse the request body JSON."""
    title: str = Field(..., example='Where is the moon?', nullable=False)
    text: str = Field(..., example='I can never see the moon during the day')
    # added upvotes so we can see if popularity of posts affects placement
    upvotes: int = Field(..., example=0)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    def long_or_nah(self, post, message=None):
        """ To use so we see if length affects placement?"""
        try:
            if len(post.text) >= 250:
                message = "This is a long post"
            else:
                message = "This is a short post"
        except Exception as e:
            message = f"Error - {e}"
        return message

    def convert_to_string(self, text):
        converted = str(text)
        return converted

    def combine(self, title, text):
        """ If we are analyzing both title and text we can use this"""
        # need to change variable name if we use this
        entire_post = str(title) + str(text)
        return entire_post

    @validator('type')
    def post_is_string(self, title, text):
        """ Makes sure that both title and text are strings"""
        if is_string(title) == True:
            if is_string(text) == True:
                return f"Both Title and Text are Strings"
            else:
                return f"{text} must be a string"
        else:
            return f"{title} must be a string"


# this is based solely off R. Herr's example
@app.post('/predict_post', method=['POST'])
def predict_post(posts: Post):
    """ Predict the subreddit based on total text in both Title and Text"""
    # making a new df so we can modify the data, if needed
    predictor = pd.DataFrame([df])
    apt_location = classifier.predict_post(predictor)
    return apt_location[0]


@router.post('/log_in', method=['POST'])
def log_in(user, password):
    """
    We're not going to need this BUT there is the getLogger in line 10
    so we might need to be able to validate it, unless that's Web
    """
    pass  # difference between router.post and app.post?


# Bryce's model that I accidentally overwrote
# class Item(BaseModel):
#     """Use this data model to parse the request body JSON."""
#
#     Title: str = Field(..., example='This is a Reddit title')
#     Post: str = Field(..., example='This is a Redd post')
#
#     @validator('Title')
#     def title_must_be_a_string(cls, value):
#         """Validate that Title is a string."""
#         assert type(value) == str, f'Title == {value}, must be a string'
#         return value
#
#     @validator('Post')
#     def post_must_be_a_string(cls, value):
#         """Validate that post is a string."""
#         assert type(value) == str, f'Title == {value}, must be a string'
#         return value

""" This part was given in the original file"""

# @router.post('/predict')
# async def predict(item: Item):
#     """
#     Make random baseline predictions for classification problem 🔮
#
#     ### Request Body
#     - `x1`: positive float
#     - `x2`: integer
#     - `x3`: string
#
#     ### Response
#     - `prediction`: boolean, at random
#     - `predict_proba`: float between 0.5 and 1.0,
#     representing the predicted class's probability
#
#     Replace the placeholder docstring and fake predictions with your own model.
#     """
#
#     X_new = item.to_df()
#     log.info(X_new)
#     y_pred = random.choice([True, False])
#     y_pred_proba = random.random() / 2 + 0.5
#     return {
#         'prediction': y_pred,
#         'probability': y_pred_proba
#     }
