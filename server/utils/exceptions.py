from fastapi import HTTPException, status


######################### Sign Up exceptions #########################
def e_user_already_exists():
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="User Already Exists"
    )
    return exception


######################### Log In exceptions #########################
def e_invalid_credentials():
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
    )
    return exception


def e_user_not_found():
    exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
    )
    return exception


def e_user_not_verified():
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Account not verified"
    )
    return exception


def e_user_already_verified():
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Account already verified"
    )
    return exception


######################### Password reset exceptions #########################
def e_otp_not_expired(wait_time):
    exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f"Please wait {wait_time} seconds before generating another OTP",
    )
    return exception


def e_otp_expired():
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"OTP Expired",
    )
    return exception


def e_otp_mistmached():
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"OTP Mismatched",
    )
    return exception


def e_generate_otp_first():
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Generate OTP for reset token",
    )
    return exception


######################### Token Exceptions #########################
def e_invalid_token():
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
    )
    return exception


def e_expired_token():
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired Token"
    )
    return exception
