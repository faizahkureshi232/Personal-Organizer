from fastapi import APIRouter, File, UploadFile
from utils import parser, summarizer, extractor

router = APIRouter()