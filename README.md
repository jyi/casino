# Casino

## 1. Environments & Setup

- Ubuntu 18.04
- Python 3.6
- Java 1.7
- [Defects4j](https://github.com/rjust/defects4j) 1.2.0

```shell
pip install -r requirements.txt
```


## 2. Run


Run casino for TBar
```
casino.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> -T <timeout> --use-pass-test --tbar-mode --use-exp-alpha -- python3 script/d4j_run_test.py <path_to_tbar>/buggy
```

Run casino for Recoder
```
casino.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> -T <timeout> --use-pass-test --recoder-mode --use-exp-alpha -- python3 script/d4j_run_test.py <path_to_recoder>/buggy
```

Example:
```shell
python3 /root/casino/casino.py -o /root/alpha-repair/out/Chart-1-casino-0 -t 180000 -w /root/alpha-repair/d4j/Chart-1 -p /root/alpha-repair -m guided -T 18000 --use-pass-test --recoder-mode --use-simulation-mode /root/alpha-repair/sim/Chart-1/Chart-1-sim.json --use-exp-alpha --seed 1812569871 -- python3 /root/casino/script/d4j_run_test.py /root/alpha-repair/buggy
```

## 3. Options
* `-o <output_dir>`: output directory (`--outdir`)
* `-w <path_to_inputs>`: directory to input json file and patched sources (`--workdir`)
* `-t <millisecond>`: timeout for single test (`--timeout`)
* `-m <mode>`: mode (`--mode`)
    - guided, seapr, genprog
    - recoder, tbar, fixminer : these are option when using original tool's algorithm.
* `-E <iteration>`: iteration limit (`--cycle-limit`)
* `-T <second>`: time limit (`--time-limit`)
* `--use-pattern`: In `seapr` mode, use `SeAPR++`.
* `--use-full-validation` : Use full validation matrix for `seapr`.
* `--seed <int>`: Use seed for random
* `--ignore-compile-error`: Do not update result for non-compilable patch candidates
* `--count-compile-fail`: Do not count iteration for non-compilable patch candidates
* `--not-use-<guide/epsilon>`: Do not use vertical/horizontal search
- `--tbar-mode`: required for template-based Java APR tools(TBar, AVATAR, FixMiner, KPar)
- `--recoder-mode`: required for learning-based APR tools(Recoder, AlphaRepair)
* `--fixminer-mode`: required for fixminer


## 4. Experiments
Necessary resources for replication are in [experiments](./experiments/) folder.

## 5. Project Structure
```
.
├── experiment
├── docs
├── casino.py
├── core.py
├── msv.py
├── select_patch.py
├── run_test.py
├── condition.py
├── msv_result_handler.py
├── plot.py
├── requirements.txt
├── .gitignore
├── README.md
```

* experiment: directory for experiment.
* docs: supplementary.
* casino.py: Entry point, read config files.
* core.py: Most of data structures are defined.
* msv.py: Main loop of Casino.
* select_patch.py: Algorithms to select patch from patch space.
* run_test.py: Run test and get result.
* condition.py: Need for condition synthesis, for `prophet`.
* msv_result_handler.py: Update data after each iteration.
* plot.py: Generate plot from outputs. Only for result analysis.
