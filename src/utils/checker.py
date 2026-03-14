from fastapi import APIRouter


router = APIRouter(
    tags=['Utils']
)


'''
The following code is used only for cron-job service
(Simply to awlways return 200 status code)
'''

@router.get('/')
def ping():
    return {'status': 'ok'}
