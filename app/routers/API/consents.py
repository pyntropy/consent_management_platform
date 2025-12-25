from fastapi import APIRouter


router = APIRouter(
    prefix="/consents", tags=["Consents"]
)


@router.post("")
def add_consent():
    pass


@router.get("")
def get_consents():
    return {"consents": "consents"}