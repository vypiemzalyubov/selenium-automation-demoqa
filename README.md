# Selenium Automation DEMOQA

Automation of [DEMOQA](https://demoqa.com/) site testing using Selenium and Page Object Model

## Project Structure:
```
selenium-automation-demoqa/
├─ .github/
│  ├─ workflows/
│  │  ├─ run_tests.yml
├── locators
│   ├── alerts_frame_windows_locators.py
│   ├── elements_page_locators.py
│   ├── form_page_locators.py
|   ├── interactions_page_locators.py
│   └── widgets_page_locators.py
├── models
│   ├── models.py
├── pages
│   ├── alerts_frame_windows_page.py
│   ├── base_page.py
│   ├── elements_page.py
│   ├── form_page.py
│   ├── interactions_page.py
│   └── widgets_page.py
├── tests
│   ├── __init__.py
│   ├── alerts_frame_windows_test.py
│   ├── conftest.py
│   ├── elements_test.py
│   ├── form_test.py
│   ├── interactions_test.py
│   └── widgets_test.py
├── utils
│   ├── driver
│   │   ├── driver.py
│   │   ├── options.py
│   ├── generator.py
│   ├── logger.py
│   ├── routes.py
│   └── settings.py
├── env.example
├── .flake8
├── .gitignore
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt
```

## Getting Started
```bash
# Clone repository
git clone https://github.com/vypiemzalyubov/selenium-automation-demoqa.git

# Install virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Viewing reports
- Install [**Allure**](https://docs.qameta.io/allure/#_get_started) from the official website
- Generate Allure report
  
  ```bash
  allure serve
  ```

## Running in Docker

```bash
# Build an image named "image-selenium"
docker build --no-cache -t image-selenium .

# Starts the container, bind mount a volume and automatically deletes on exit
docker run --rm --name selenium-runner -v /selenium-automation-demoqa/docker-results/:/allure-results/ image-selenium
```

## Github workflow
- Go to [**"Run workflow"**](https://github.com/vypiemzalyubov/selenium-automation-demoqa/actions/workflows/run_tests.yml) in GitHub Actions

  ```yml
  # Options in workflow
    - chrome
    - firefox
  ```
- View [**Allure test results**](https://vypiemzalyubov.github.io/selenium-automation-demoqa/) after completing the GitHub Actions workflow
