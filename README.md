# Selenium Automation DEMOQA

Automation of [DEMOQA](https://demoqa.com/) site testing using Selenium and Page Object Model

## Used technologies
<p  align="center">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" title="PyCharm" alt="PyCharm">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original.svg" title="Pytest" alt="Pytest">
  <img width="5%" src="https://avatars0.githubusercontent.com/u/983927?v=3&s=400" title="Selenium" alt="Selenium">
  <img width="5%" src="https://biercoff.com/content/images/2017/08/allure-logo.png" title="Allure Report" alt="Allure Report">
  <img width="5%" src="https://avatars.githubusercontent.com/u/110818415?s=200&v=4" title="Pydantic" alt="Pydantic">
  <img width="5%" src="https://i.postimg.cc/fbsyvkVW/requests.png" title="Requests" alt="Requests">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" title="GitHub" alt="GitHub">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/githubactions/githubactions-original.svg" title="GitHub Actions" alt="GitHub Actions">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker">
  <img width="4%" src="https://docs.astral.sh/ruff/assets/bolt.svg" title="Ruff" alt="Ruff">
</p>

## Project Structure:
```
selenium-automation-demoqa/
├── .github/
│   ├── workflows
│   │   ├── run_tests.yml
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
├── ...
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
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

# Running with Docker Compose
docker-compose up
```

## GitHub workflow
- Go to [**"Run workflow"**](https://github.com/vypiemzalyubov/selenium-automation-demoqa/actions/workflows/run_tests.yml) in GitHub Actions

  ```yml
  # Options in workflow
    - chrome
    - firefox
  ```
- View [**Allure test results**](https://vypiemzalyubov.github.io/selenium-automation-demoqa/) after completing the GitHub Actions workflow

## GitLab

See this project on [**GitLab**](https://gitlab.com/vypiemzalyubov/selenium-automation-demoqa)
