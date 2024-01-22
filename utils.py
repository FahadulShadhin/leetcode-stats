from fastapi.responses import JSONResponse


def response(status_code: int, status: str, message: str, data: dict = None):
    content = {'status': status, 'message': message}
    if data is not None:
        content['data'] = data

    return JSONResponse(
        content=content,
        status_code=status_code,
    )
