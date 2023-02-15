# AlphaRepair

## Environments & Setup
* Ubuntu 20.04
* Python 3.8
* Java 1.7
* [Defects4j](https://github.com/rjust/defects4j) 1.2.0

```shell
pip install -r requirements-ubuntu2004.txt
```

## Run Casino
* Use `script/casino-run.py`

1. Generate patch candidiates

    ```
    python3 script/casino-run.py gen
    ```
2. Run casino

    ```
    python3 script/casino-run.py casino <id>
    ```
    Output will be in `out-<id>` directory.
