import logging
import random

from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
import pickle

with open("models/mvp_log_pipe", "rb") as file:
    model = pickle.load(file)

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    Title: str = Field(..., example='This is a Reddit title', nullable=False)
    Post: str = Field(..., example='This is a Redd post')

    def combine(self, title, post):
        """ If we are analyzing both title and text in one variable, use this"""
        # need to change variable name if we use this
        entire_post = str(title) + ' ' + str(post)
        return entire_post

    def convert_to_string(self, text):
        converted = str(text)
        return converted

    @validator('Text')  # why write this twice? - DRY
    def text_must_be_a_string(cls, value):
        """Validate that Title is a string."""
        assert type(value) == str, f'Title == {value}, must be a string'
        return value

    @validator('Title')
    def must_have_title(cls, title):
        """ All reddit posts must have a title"""
        return cls.assertIsNotNone(title)


@router.post('/predict')
async def predict(item: Item):
    """
    Predicts what reddit to post to 🔮

    ### Request Body
    - Title: str
    - Post: str

    ### Response
    - `prediction`: List of top 5 reddits
    """
    reddit_post = item.Title + ' ' + item.Post
    prob = model.predict_proba([reddit_post])[0]
    x = list(zip(model.classes_, prob))
    y = sorted(x, key=lambda z: z[1], reverse=True)
    return {
        'predicition': [i[0] for i in y[:5]]
    }
