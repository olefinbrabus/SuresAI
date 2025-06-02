FROM python:3.11

WORKDIR super_resolution/

COPY . .

RUN pip install -e .

ENTRYPOINT ["super_resolution.py"]