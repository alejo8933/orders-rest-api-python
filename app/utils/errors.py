from fastapi import HTTPException

def raise_not_found(entity: str, id: int):
    raise HTTPException(status_code=404, detail=f"{entity} {id} not found")

def raise_bad_request(msg: str):
    raise HTTPException(status_code=400, detail=msg)
