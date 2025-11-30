from fastapi import FastAPI,APIRouter,Depends ,UploadFile,status
from fastapi.responses import JSONResponse
import os 
from helpers.config import get_settings,Settings
from controllers import DataController,ProjectController
from models.enums import ResponseSignal
import aiofiles
import logging 


logger = logging.getLogger('uvicorn.error')


data_router = APIRouter(
   prefix="/api/v1/data",
   tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str, file: UploadFile,
                       app_settings:Settings = Depends(get_settings)):
   
   data_controller =DataController()
   #valid
   is_valid,result = data_controller.validate_uploaded_file(file=file)
   
   if not is_valid:
      return JSONResponse(
         status_code=status.HTTP_400_BAD_REQUEST,
         content={
            "signal":result
         }
      )
      
   project_dir_path = ProjectController().get_project_path(project_id=project_id)
   file_path = data_controller.generate_unique_filename(
      orgi_file_name=file.filename,
      project_id=project_id
   )
   
   
   try:
      #open binary
      async with aiofiles.open(file_path,"wb") as f:  
         while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNKS_SIZE):
            await f.write(chunk)
            
   except Exception as e:
      logger.error(f'Error while uploading file: {e}')
      return JSONResponse(
         status_code=status.HTTP_400_BAD_REQUEST,
         content={
               "signal":ResponseSignal.FILE_UPLOADED_FAILED.value
            })
      
      
   return JSONResponse(
         content={
            "signal":ResponseSignal.FILE_UPLOADED_SUCCESS.value
         }
      )