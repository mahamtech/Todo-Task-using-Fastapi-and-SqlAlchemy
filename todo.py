from fastapi import APIRouter,Depends,HTTPException,status
from database import get_db
from sqlalchemy.orm import Session
from schemas import TodoCreate,Todo as TodoSchema
from model import Todo,User
from typing import List
from security import get_current_user, get_current_admin
import logging
router=APIRouter(prefix="/todos",tags=["Todos"])
@router.post("/",response_model=TodoSchema)

def create_todo(
    todo:TodoCreate,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_admin)
):
    new_todo=Todo(
        title=todo.title,
        user_id=current_user.id
    )
    logging.info(f"new task created {new_todo}")
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
#get all data
@router.get("/", response_model=List[TodoSchema])
def get_data(db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    return db.query(Todo).all()
#get only on data
@router.get("/{todo_id}")
def get_one(todo_id:int,db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    result=db.query(Todo).filter(Todo.id == todo_id).first()
    logging.info(f"get task  {result} for id : {todo_id}")
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not user found"
        )
    return result

@router.put("/{todo_id}", response_model=TodoSchema)
def update_one(todo_id:int,updated:TodoCreate,db:Session=Depends(get_db), current_user:User=Depends(get_current_admin)):
    result=db.query(Todo).filter(Todo.id == todo_id).first()
    logging.info(f"get task  {result} for id : {todo_id}")
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not user found"
        )
    for key,value in updated.dict().items():
        setattr(result,key,value)
    db.commit()
    db.refresh(result)
    return result
@router.delete("/{todo_id}")
def delete_one(todo_id:int,db:Session=Depends(get_db), current_user:User=Depends(get_current_admin)):
    result=db.query(Todo).filter(Todo.id == todo_id).first()
    logging.info(f"deleted task  {result} for id : {todo_id}")
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not user found"
        )
    db.delete(result)
    db.commit()
    return {
        "message":"succesfully deleted"
    }
              

    

