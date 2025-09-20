from fastapi import APIRouter, status

from schema import RequestToInsertFile, RequestToDeleteFile, ResponseForGettingFiles
from db.query import add_owner_specific_file, remove_owner_specific_file, get_owner_specific_files


router = APIRouter()


# POST /file and DELETE /file return no body. That’s OK, but you might want to return confirmation or 204.
# There’s no validation (e.g., empty name), and no 404 or conflict (409) handling. Everything returns 201/202/200 even on edge cases.
# No CORS middleware or authentication—fine for internal use/testing, but worth noting.


# POST /owners/{owner}/files
@router.post('/file', status_code=status.HTTP_201_CREATED)
def insert_or_update_files(request: RequestToInsertFile):
    add_owner_specific_file(owner=request.owner, name=request.file.name)


@router.get('/files', status_code=status.HTTP_200_OK)
def get_files(owner: str) -> ResponseForGettingFiles:
    return get_owner_specific_files(owner=owner)


# DELETE /file with a body is unusual; typical REST style uses path params:
# DELETE /owners/{owner}/files/{name}
@router.delete('/file', status_code=status.HTTP_202_ACCEPTED)
def delete_file(request: RequestToDeleteFile):
    remove_owner_specific_file(owner=request.owner, name=request.file.name)