# Lambda Layer Pkg Builder

Docker image that will run a `pip install` on a requirements.txt file and generate a zipped artifact that can be uploaded into a lambda layer. Created to serve a need in the Big Data Technologies grad course I teach at Baruch and [this](https://towardsdatascience.com/how-to-install-python-packages-for-aws-lambda-layer-74e193c76a91) article

# Usage

Mount your current working directory with the **requirements-file** available. Simplest invocation is:

Ensure you have requirements.txt in working dir.
```bash
➜  test cat >> requirements.txt
requests==2.24.0
➜  test ls -ahl
total 8
drwxr-xr-x   3 tkarim  staff    96B Dec 21 08:34 .
drwxr-xr-x  23 tkarim  staff   736B Dec 21 08:31 ..
-rw-r--r--@  1 tkarim  staff    32B Dec 21 08:35 requirements.txt
```

Run the image from dockerhub.
```bash
➜  test docker run -v $PWD:/data mottaquikarim/pkglambdalayer:latest
Collecting requests==2.24.0
  Downloading requests-2.24.0-py2.py3-none-any.whl (61 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.11-py2.py3-none-any.whl (127 kB)
Installing collected packages: urllib3, idna, chardet, certifi, requests
Successfully installed certifi-2020.12.5 chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.11
➜  test ls -ahl
total 1792
drwxr-xr-x   5 tkarim  staff   160B Dec 21 08:36 .
drwxr-xr-x  23 tkarim  staff   736B Dec 21 08:31 ..
drwxr-xr-x  13 tkarim  staff   416B Dec 21 08:36 pkg
-rw-r--r--   1 tkarim  staff   879K Dec 21 08:36 pkg.zip
-rw-r--r--   1 tkarim  staff    17B Dec 21 08:36 requirements.txt
➜  test
```

For full set of CLI options:
```
➜  test docker run -v $PWD:/data mottaquikarim/pkglambdalayer:latest --help
usage: main.py [-h] [--requirements-file REQUIREMENTS_FILE]
               [--artifact-file ARTIFACT_FILE]

CLI tool for generating lambda layer dependencies in python

optional arguments:
  -h, --help            show this help message and exit
  --requirements-file REQUIREMENTS_FILE
                        Name of your dependencies requirements file (default:
                        requirements.txt)
  --artifact-file ARTIFACT_FILE
                        Name of your output artifact zip file (default: pkg)
```


# Build your own

```bash
➜  pkglambdalayer git:(master) make build
docker build --build-arg PYTHON_VERSION=3.9 -t pkglambdalayer:dev .
Sending build context to Docker daemon  112.6kB
Step 1/7 : ARG PYTHON_VERSION
Step 2/7 : FROM python:$PYTHON_VERSION
 ---> d1eef6fb8dbe
Step 3/7 : WORKDIR /app
 ---> Using cache
 ---> 5563b6f6ec53
Step 4/7 : COPY main.py .
 ---> Using cache
 ---> 217fd91bf5e0
Step 5/7 : ARG DATA_FILE=/data
 ---> Using cache
 ---> 4cf7c3b85cd8
Step 6/7 : WORKDIR $DATA_FILE
 ---> Using cache
 ---> 384ced341b8f
Step 7/7 : ENTRYPOINT ["python", "/app/main.py"]
 ---> Using cache
 ---> 4528ecb3d615
Successfully built 4528ecb3d615
Successfully tagged pkglambdalayer:dev
```

* `PYTHON_VERSION` defaults to latest, can be set to anything.
* `DATA_FILE` defaults to `/data`, expected working dir to mount requirements.txt file 
