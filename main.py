from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi import status

app = FastAPI()

data = []

@app.get('/')
def home():
    return {"message": "Server Started Successfully"}

@app.post('/todos', status_code=status.HTTP_201_CREATED)
async def add_todo(req: Request):
    try:
        # Access the body from the Request
        task = await req.json()

        # Added Required data to the resource(task)
        task["id"] = len(data) + 1
        task["done"] = False

        # Saving the task
        data.append(task)
        print(data)

        # return {"message": "Created successly"}
        return task
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": str(e)})

@app.get('/todos', status_code=status.HTTP_204_NO_CONTENT)
def get_todos():
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=data
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.get('/todos/{id}')
def get_todo(id: int):
    try: 
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=data[id - 1]
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    