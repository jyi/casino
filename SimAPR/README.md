# SimAPR

## 1. Setup
Python >= 3.8

```
pip install -r requirements.txt
```

## 2. Run

Run SimAPR for TBar, AVATAR, KPar, FixMiner

```
python3 simpar.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> -T <timeout> --use-pass-test --tbar-mode --use-exp-alpha -- python3 script/d4j_run_test.py <path_to_tbar>/buggy
```

Run SimAPR for Recoder, AlphaRepair

```
python3 simapr.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> -T <timeout> --use-pass-test --recoder-mode --use-exp-alpha -- python3 script/d4j_run_test.py <path_to_recoder>/buggy
```
## 3. Options

* `-o <output_dir>`: output directory (`--outdir`)
* `-w <path_to_inputs>`: directory to input json file and patched sources (`--workdir`)
* `-t <millisecond>`: timeout for single test (`--timeout`)
* `-m <mode>`: mode (`--mode`)
  * guided, seapr, genprog
  * recoder, tbar, fixminer : these are option when using original tool's algorithm.
* `-E <iteration>`: iteration limit (`--cycle-limit`)
* `-T <second>`: time limit (`--time-limit`)
* `--use-pattern`: In `seapr` mode, use `SeAPR++`.
* `--use-full-validation` : Use full validation matrix for `seapr`.
* `--seed <int>`: Use seed for random
* `--ignore-compile-error`: Do not update result for non-compilable patch candidates
* `--count-compile-fail`: Do not count iteration for non-compilable patch candidates
* `--not-use-<guide/epsilon>`: Do not use vertical/horizontal search

- `--tbar-mode`: required for template-based Java APR tools(TBar, AVATAR, FixMiner, KPar)
* `--recoder-mode`: required for learning-based APR tools(Recoder, AlphaRepair)

* `--fixminer-mode`: required for fixminer


## 4. Project Structure
```
.
├── msv-search.py
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
├── cpr/
└── venv/
```

* msv-search.py: Entry point, read config files.
* core.py: Most of data structures are defined
* msv.py: Run MSV
* select_patch.py: Algorithms to select patch from patch space.
* run_test.py: Run test and get result.
* condition.py: Need by conditional patches.
* msv_result_handler.py: Update data using result, remove used patches.
* plot.py: Plot graph from result.

## 5. Extend Patch Scheduling Algorithm

You can add your own algorithm to the SimAPR by modifing [select_patch.py](./select_patch.py) file. 