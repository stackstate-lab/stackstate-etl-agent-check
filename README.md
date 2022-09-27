# StackState ETL Agent Check

Exposes the [StackState ETL framework](https://github.com/stackstate-lab/stackstate-etl) as a custom agent check. 
The framework makes 3rd-party data extract, transform and load into the 4T model simpler by using low-code yaml
templates.

See [StackState ETL documentation](https://stackstate-lab.github.io/stackstate-etl/) for more information.

## Installation

From the StackState Agent 2 linux machine.

### As an Agent Check on StackState Agent

```bash 
curl -L https://github.com/stackstate-lab/stackstate-etl-agent-check/releases/download/v0.2.0/sts_etl_check-0.2.0.zip -o sts_etl_check.zip
tar -xvf sts_etl_check.zip
./install.sh
```

### As a Python package on StackState Agent

```bash

sudo -H -u stackstate-agent bash -c "/opt/stackstate-agent/embedded/bin/pip install https://github.com/stackstate-lab/stackstate-etl-agent-check/releases/download/v0.2.0/stackstate-etl-agent-check-py27-0.2.0.tar.gz
```

## Development

This project is generated using [Yeoman](https://yeoman.io/) and the [StackState Generator](https://github.com/stackstate-lab/generator-stackstate-lab)

StackState ETL Agent Check is developed in Python 3, and is transpiled to Python 2.7 for deployment to the StackState Agent v2 environment.

---
### Prerequisites:

- Python v.3.9.x See [Python installation guide](https://docs.python-guide.org/starting/installation/)
- [PDM](https://pdm.fming.dev/latest/#recommended-installation-method)
- [Docker](https://www.docker.com/get-started)
---

### Setup local code repository

```bash 
git clone git@github.com:stackstate-lab/stackstate-etl-agent-check.git
cd stackstate-etl-agent-check
pdm install 
```

The `pdm install` command sets up all the projects required dependencies using [PEP 582](https://peps.python.org/pep-0582/) instead of virtual environments.


### Prepare local _.sts.env_ file

The `.sts.env` file is used to run the StackState Agent container. Remember to change the StackState url and api key for your environment.

```bash

cat <<EOF > ./.sts.env
STS_URL=https://xxx.stackstate.io/receiver/stsAgent
STS_API_KEY=xxx
EOF
```

### Preparing Agent check conf.yaml

```
cp ./src/data/conf.d/etl.d/conf.yaml.example ./src/data/conf.d/etl.d/conf.yaml
```
---

### Code styling and linting


- [Black](https://black.readthedocs.io/en/stable/) for formatting
- [isort](https://pycqa.github.io/isort/) to sort imports
- [Flakehell](https://flakehell.readthedocs.io/) for linting
- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking

```bash
pdm format
```

### Running unit tests

```bash
pdm test
```

### Build

The build will transpile the custom agent check to Python 2.7 and creates and install shell script packaged into
the `dist/etl-agent-check-0.1.0.zip`

```bash
pdm build
```

### Building a StackState Agent container

You have the ability to customize the StackState Agent using the [Dockerfile](./tasks/dev-agent/Dockerfile).

For installing os packages or other tools at runtime, you could define an `install.sh` file in the `tests/resources/share/` directory that is run every time the container is started.

```bash
pdm cleanAgent
pdm buildAgent
```

### Running your custom agent check

A check can be dry-run inside the StackState Agent container by running:

```bash
pdm check
```

### Starting the StackState Agent to send data to StackState server

Starts the StackState Agent in the foreground using the configuration `src/data/conf.d/` directory.

```bash
pdm serve
```
---
