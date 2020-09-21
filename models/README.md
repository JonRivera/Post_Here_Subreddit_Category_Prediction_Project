# How to use models

I am assuming you are in app/api/

```
with open("../../models/mvp_log_pipe", "rb") as file:
    model = pickle.load(file)
```

At this point you have the model saved into a variable so now to make predictions you do this

```
model.predict(["A string of text goes here"])
```

It is imperitive that you but the post in a list as shown above. Unfortunately predict returns an array so we must index to get just the string. So really it's

```
model.predict(["text"])[0]
```

Now you should hava subreddit name