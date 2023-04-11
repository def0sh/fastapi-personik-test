# Test task

### installation:

1. Go to the https://serpapi.com/ and get an API key via user interface
2. Create  .env file and write received token there
3. uvicorn src.main:app --reload
4. OpenApi in Swagger http://127.0.0.1:8000/docs

![image](https://user-images.githubusercontent.com/74783488/231267918-cd4d26c0-43ac-4b66-873d-9bb25e286493.png)


_Test query "python"_

![image](https://user-images.githubusercontent.com/74783488/231268652-3da28d5b-ddd6-422c-bd42-fcb19e8b7402.png)

### Run with Docker

1. docker build -t testpersonik:latest .
2. docker run -d -p 80:80 testpersonik:latest
3. docker logs {id}




