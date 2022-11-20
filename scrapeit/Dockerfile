FROM python:3
WORKDIR /app

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .
 
# Run the crawler when the container launches.
CMD [ "python3", "go-spider.py" ]


# RUN scrapy crawl srPages2 -o ./ads_25pg1.csv -t csv