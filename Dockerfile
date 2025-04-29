FROM python:3.11.12-slim-bullseye
COPY ./build_api /api
RUN pip install fastapi uvicorn pandas
WORKDIR .api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]