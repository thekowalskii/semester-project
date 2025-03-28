from fastapi import Request, Depends, HTTPException, status, Header

from backend.config import API_KEY


def api_key(request: Request ):
    headers = request.headers

    # print(headers)

    if headers.get('x-api-key') != API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid API Key')

    return


api_key_dp = Depends(api_key)
