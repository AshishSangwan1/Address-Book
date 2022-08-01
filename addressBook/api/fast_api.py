from fastapi import FastAPI
from typing import List

from api.model import AddressCordinates, UpdateAddressCordinates
from starlette.responses import RedirectResponse, JSONResponse

from utils import *

app = FastAPI()


@app.get("/")
async def docs():
    return RedirectResponse("/docs")


@app.post("/update/")
def update(data: List[UpdateAddressCordinates]):
    update_list = []
    for d in data:
        longitude = d.longitude
        lattitude = d.lattitude
        new_longitude = d.new_longitude
        new_lattitude = d.new_lattitude
        update_list.append({"longitude": longitude, "lattitude": lattitude, 'new_longitude': new_longitude,
                            'new_lattitude': new_lattitude})
    try:
        return JSONResponse(content=update_address(update_list), status_code=200)
    except Exception as e:
        JSONResponse(content=e, status_code=500)


@app.post("/create/")
async def create_record(data: List[AddressCordinates]):
    create_list = []
    for d in data:
        longitude = d.longitude
        lattitude = d.lattitude
        create_list.append({"longitude": longitude, "lattitude": lattitude})
    try:
        return JSONResponse(content=create_address(create_list), status_code=200)
    except Exception as e:
        JSONResponse(content=e, status_code=500)


@app.post("/delete/")
async def delete_record(data: List[AddressCordinates]):
    delete_list = []
    for d in data:
        longitude = d.longitude
        lattitude = d.lattitude
        delete_list.append({"longitude": longitude, "lattitude": lattitude})
    try:
        return JSONResponse(content=delete_address(delete_list), status_code=200)
    except Exception as e:
        JSONResponse(content=e, status_code=500)


@app.post("/fetch_record/")
async def fetch_record(data: AddressCordinates, distence: float):
    longitude = data.longitude
    lattitude = data.lattitude
    try:
        return JSONResponse(content=fetch_addresses({"longitude": longitude, "lattitude": lattitude}, distence), status_code=200)
    except Exception as e:
        JSONResponse(content=e, status_code=500)
