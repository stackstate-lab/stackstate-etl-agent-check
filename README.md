# StackState ETL Agent Check

Exposes the [StackState ETL framework](https://github.com/stackstate-lab/stackstate-etl) as a custom agent check. 
The framework makes 3rd-party data extract, transform and load into the 4T model simpler by using low-code yaml
templates.

See [StackState ETL documentation](https://stackstate-lab.github.io/stackstate-etl/) for more information.

## Installation

From the StackState Agent 2 linux machine, run

```bash 
curl -L https://github.com/stackstate-lab/stackstate-etl-agent-check/releases/download/v0.1.0/stackstate-etl-agent-check-py27-0.1.0.tar.gz -o stackstate-etl-agent-check.tar.gz
tar -xvf stackstate-etl-agent-check.tar.gz
./install.sh
```


## Development

StackState ETL Agent is developed in Python 3, and is transpiled to Python 2.7 during build.

---
## Prerequisites:

- Python v.3.7+. See [Python installation guide](https://docs.python-guide.org/starting/installation/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://www.docker.com/get-started)
- [Custom Synchronization StackPack](https://docs.stackstate.com/stackpacks/integrations/customsync)
---

## Setup local code repository


The poetry install command creates a virtual environment and downloads the required dependencies.

Install the [stsdev](https://github.com/stackstate-lab/stslab-dev) tool into the virtual environment.

```bash 
python -m pip install https://github.com/stackstate-lab/stslab-dev/releases/download/v0.0.6/stslab_dev-0.0.6-py3-none-any.whl
```

Finalize the downloading of the StackState Agent dependencies using `stsdev`

```bash
stsdev update
```
## Prepare local `.env` file

The `.env` file is used by `stsdev` to prepare and run the StackState Agent Docker image. Remember to change the
StackState url and api key for your environment.

```bash

cat <<EOF > ./.env
#STSDEV_IMAGE_EXT=tests/resources/docker/agent_dockerfile
STS_URL=https://xxx.stackstate.io/receiver/stsAgent
STS_API_KEY=xxx
STSDEV_ADDITIONAL_COMMANDS=/etc/stackstate-agent/share/install.sh
STSDEV_ADDITIONAL_COMMANDS_FG=true
EXCLUDE_LIBS=charset-normalizer,stackstate-etl,stackstate-etl-agent-check
EOF
```
## Preparing Agent check conf.yaml

```
cp ./tests/resources/conf.d/etl.d/conf.yaml.example ./tests/resources/conf.d/etl.d/conf.yaml
```
---
## Running in Intellij

Setup the module sdk to point to the virtual python environment created by Poetry.
Default on macos is `~/Library/Caches/pypoetry/virtualenvs`

Create a python test run config for `tests/test_etl_check.py`

You can now run the integration from the test.

---
## Running using `stsdev`

```bash

stsdev agent check etl 
```

## Running StackState Agent to send data to StackState

```bash

stsdev agent run
```

---
## Using as a module in other custom agent checks.

It may be desired to create you own custom agent check that

StackState Agent 2 supports python 2.7.  StackState ETL Agent Check is transpiled to python 2.7 code.

From a shell on the agent machine run,

```bash 
/opt/stackstate-agent/embedded/bin/pip install https://github.com/stackstate-lab/stackstate-etl-agent-check/releases/download/v0.0.1/stackstate-etl-agent-check-py27-0.1.0.tar.gz
```


---
## Quick-Start for `stsdev`

`stsdev` is a tool to aid with the development StackState Agent integrations.

### Managing dependencies

[Poetry](https://python-poetry.org/) is used as the packaging and dependency management system.

Dependencies for your project can be managed through `poetry add` or `poetry add -D` for development dependency.

```console
$ poetry add PyYAML
```
### Code styling and linting

```console
$ stsdev code-style
```

### Build the project
To build the project,
```console
$ stsdev build --no-run-tests
```
This will automatically run code formatting, linting, tests and finally the build.

### Unit Testing
To run tests in the project,
```console
$ stsdev test
```
This will automatically run code formatting, linting, and tests.

### Dry-run a check

A check can be dry-run inside the StackState Agent by running

```console
$ stsdev agent check etl
```
Before running the command, remember to copy the example conf `tests/resources/conf.d/etl.d/conf.yaml.example` to
`tests/resources/conf.d/etl.d/conf.yaml`.


### Running checks in the Agent

Starts the StackState Agent in the foreground using the test configuration `tests/resources/conf.d`

```console
$ stsdev agent run
```

### Packaging checks

```console
$  stsdev package --no-run-tests
```
This will automatically run code formatting, linting, tests and finally the packaging.
A zip file is created in the `dist` directory.  Copy this to the host running the agent and unzip it.
Run the `install.sh`.

