FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN python3.11 -m pip install -r requirements.txt -t .

COPY response.html ./
COPY app.py ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
