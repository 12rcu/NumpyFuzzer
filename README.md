# NumpyFuzzer

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

## Install new dependeny

```bash
source .venv/bin/activate
pip install <package>
pip freeze | tee requirements.txt
```

