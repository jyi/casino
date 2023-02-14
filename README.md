# SimAPR

SimAPR is a replay-based patch-scheduling simulation system. Using SimAPR, researchers can easily and quickly evaluate the performance of a patch-scheduling algorithm. Currently, we provide the following three scheduling algorithms. 

1. The original scheduling algorithms of the following six APR tools: TBar, Avatar, FixMiner, KPar, Recoder and AlphaRepair  
2. GenProg-SL:
3. SeAPR:
4. Casino:
  

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
casino.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> --use-pass-test --tbar-mode -- python3 script/d4j_run_test.py <path_to_tbar>/buggy
```

Run casino for Recoder
```
casino.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> --use-pass-test --recoder-mode -- python3 script/d4j_run_test.py <path_to_recoder>/buggy
```

Run casino for Prophet

```
casino.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> --use-pass-test -p <path_to_tool> -- <test_script> <arguments>
```

## 3. Mode
* guided: Casino
* seapr: using SeAPR algorithm

* prophet: Prophet algorithm for C
* spr: SPR algorithm for C
* tbar: TBar algorithm for Java
* recoder: Recoder algorithm for Java

* random: complete random
* original: run original program for Java

## 4. Options
* `-o <output_dir>`: output directory (`--outdir`)
* `-w <path_to_inputs>`: directory to input json file and patched sources (`--workdir`)
* `-t <millisecond>`: timeout for single test (`--timeout`)
* `-m <mode>`: mode (`--mode`)
* `-p <path_to_tool>`: path to each tool, required for `prophet` (`--msv-path`)
* `-E <iteration>`: iteration limit (`--cycle-limit`)
* `-T <second>`: time limit (`--time-limit`)
* `-c <correct_patch_id>`: id of correct patch, for debugging and `--finish-correct-patch` option (`--correct-patch`)
* `--finish-correct-patch`: finish if it reaches correct patch
* `--tbar-mode`: required for template-based Java APR tools(TBar, AVATAR, FixMiner, KPar)
- `--recoder-mode`: required for learning-based APR tools(Recoder, AlphaRepair)
* `--use-pattern`: In `seapr` mode, use `SeAPR++`.
* `--use-full-validation` : Use full validation matrix for `seapr`.
* `--seed <int>`: Use seed for random
* `--ignore-compile-error`: Do not update result for non-compilable patch candidates
* `--count-compile-fail`: Do not count iteration for non-compilable patch candidates
* `--not-use-<guide/epsilon>`: Do not use vertical/horizontal search
* `--fixminer-mode`: required for fixminer

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
