# Selenium Automation DEMOQA

Automation of [DEMOQA](https://demoqa.com/) site testing using Selenium and Page Object Model

## Project Structure:
```
selenium-automation-demoqa/
├─ .github/
│  ├─ workflows/
│  │  ├─ run_tests.yml
├── locators
│   ├── ...
│   ├── elements_page_locators.py
│   ├── ...
├── models
│   ├── models.py
├── pages
│   ├── ...
│   ├── base_page.py
│   ├── elements_page.py
│   ├── ...
├── tests
│   ├── ...
│   ├── conftest.py
│   ├── elements_test.py
│   ├── ...
├── utils
│   ├── driver
│   │   ├── driver.py
│   │   ├── options.py
│   ├── generator.py
│   ├── logger.py
│   ├── routes.py
│   └── settings.py
├── env.example
├── ...
├── Dockerfile
├── ...
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

## GitLab

See this project on [**GitLab**](https://gitlab.com/vypiemzalyubov/selenium-automation-demoqa)
