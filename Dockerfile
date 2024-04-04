FROM python:3.11
WORKDIR /src
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update && apt-get install -y google-chrome-stable
COPY . .
CMD ["pytest", "--headless=true"]