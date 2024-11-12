import aiofiles, uvicorn, base64

from fastapi import FastAPI 

app = FastAPI()

async def load_file(file_number: float):
    async with aiofiles.open(f"C:/Users/User/Desktop/(내부용)_2024 YouMake 복수구매 DIC_v.{file_number}(241010).xlsx", "rb") as file_bytes:
        file_data = base64.b64encode(await file_bytes.read()).decode()
    
    return file_data

@app.get("/retrieve_data/")
async def retrieve_data(file_number: float):
    file_data = await load_file(file_number)

    return file_data

if (__name__ == "__main__"):
    uvicorn.run("TestFastAPI:app", reload = True, port = 5002, host = "0.0.0.0")
