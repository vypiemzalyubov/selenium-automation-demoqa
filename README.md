# Selenium Automation DEMOQA

## Project Structure:
```
selenium-automation-demoqa/
├── locators
│   ├── alerts_frame_windows_locators.py
│   ├── elements_page_locators.py
│   ├── form_page_locators.py
│   └── widgets_page_locators.py
├── models
│   ├── models.py
├── pages
│   ├── alerts_frame_windows_page.py
│   ├── base_page.py
│   ├── elements_page.py
│   ├── form_page.py
│   └── widgets_page.py
├── tests
│   ├── __init__.py
│   ├── alerts_frame_windows_test.py
│   ├── elements_test.py
│   ├── form_test.py
│   └── widgets_test.py
├── utils
│   ├── generator.py
│   ├── logger.py
│   ├── routes.py
│   └── settings.py
├── env.example
├── .gitignore
├── LICENSE
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt
```

## Running in Docker

```bash
# Build an image named "selenium-runner"
docker build -t selenium-runner .

# Starts the container, bind mount a volume and automatically deletes on exit
docker run --rm -v /selenium-automation-demoqa/docker-results/:/allure-results/ selenium-runner

# Running with Docker Compose
docker-compose up --build
```
