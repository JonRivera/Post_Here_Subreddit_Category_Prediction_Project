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

    Title: str = Field(..., example='This is a Reddit title')
    Post: str = Field(..., example='This is a Redd post')
   
    @validator('Title')
    def title_must_be_a_string(cls, value):
        """Validate that Title is a string."""
        assert type(value) == str, f'Title == {value}, must be a string'
        return value

    @validator('Post')
    def post_must_be_a_string(cls, value):
        """Validate that post is a string."""
        assert type(value) == str, f'Title == {value}, must be a string'
        return value


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
    x = list(zip(model.classes_,prob))
    y = sorted(x, key=lambda z: z[1], reverse=True)
    return {
        'predicition': [i[0] for i in y[:5]]
    }
