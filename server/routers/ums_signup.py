from fastapi import APIRouter, Header, status
from ..models import user as user_models
from ..utils import db, exceptions, jwt as jwt_utils, user as user_utils


router = APIRouter(prefix="/api/ums")

# signup
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: user_models.NewUser):

    # Creating new user
    new_user = user_utils.create_new_user(**user.dict())

    # Check if user already exists in a db
    if new_user in db.users:
        raise exceptions.getUserException()

    else:
        db.users.append(new_user)

    return {
        "users": db.users,
        "message": "user added successfully",
        "token": jwt_utils.create_access_token(
            userid=new_user["uid"], email=user.email, role="admin"
        ),
    }


# login
@router.post("/validate-token")
async def signin(token: str = Header()):
    try:
        payload = jwt_utils.validate_access_token(access_token=token)
        return payload
    except Exception as e:
        raise e
