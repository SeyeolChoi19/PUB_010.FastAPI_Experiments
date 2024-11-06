import uvicorn, json 

import datetime as dt 
import polars   as pl

from fastapi import FastAPI, Header 

from fastapi.encoders import jsonable_encoder 

app = FastAPI()

@app.get("/hi/{who}")
def greet(who: str = "user"):    
    return_dict = {
        "wh1" : pl.DataFrame({"new" : [1]}).to_dicts()
    }

    return json.dumps(jsonable_encoder(return_dict))

if (__name__ == "__main__"):
    uvicorn.run("basic_app:app", reload = True)
