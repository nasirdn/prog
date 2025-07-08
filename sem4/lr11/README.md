# ������������ ������ � 11. ��������� ������������� ������� �� FAST.API
---
1. �������� ���������.
```python
py -m venv venv
```
   ��������� ���������.
```python
.\venv\Scripts\activate
```   
2. ��������� ��������� ����������.
���:
```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/home")
def get_home():
    return {"data": "Hello world!"}
```   
```
python -m uvicorn main:app --reload
```  

���������:  
![���������1.jpg](���������1.jpg)

3. ��������� ����������.
   
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Task(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/tasks")
def get_tasks():
    task = Task(name= "Do KP(")
    return {"data" : task}
```
��������� ����������������� �� �������� http:/"������"/docs.

![���������2.jpg](���������2.jpg)

4. �������� ����������.
   
```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated

app = FastAPI()

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int

@app.post("/")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    return {"data": task}

@app.get("/home")
def get_home():
    return {"text" : "hello world"}
```
���������:  
![���������3.jpg](���������3.jpg)

������ POST:  
![���������4.jpg](���������4.jpg)

������ GET:  
![���������5.jpg](���������5.jpg)