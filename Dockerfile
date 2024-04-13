# 
FROM python3.9

# 
WORKDIR code

# 
COPY .requirements.txt coderequirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r coderequirements.txt

# 
COPY .app codeapp

# 
CMD [uvicorn, app.mainapp, --host, 0.0.0.0, --port, 80]