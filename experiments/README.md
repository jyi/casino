# Experiment

## 1. Patch Generation
Scripts for patch generation are already prepared. Each tool has `<tool>.py` to generate patches.

For example, for Avatar, run `avatar/avatar.py` to generate patch candidates.

Here is the actual commands:
```
$ cd <tool>
$ python3 <tool>.py <project>
```

For example,
```
$ cd avatar
$ python3 avatar.py Chart_4
```
Note: this will consumes a lot of disk space. Make sure that you have more than 1GB of space.

## 2. Run SimAPR
Scripts for SimAPR are also already prepared. Each tool has `search-<tool>-<algorithm>.py` in their directory.
For `<algorithm>`, you can use one of the scheduling algorithms: `orig`, `simapr`, `seapr`, `genprog`.

### Original order and SeAPR
Usage:
```
$ cd <tool>
$ python3 search-<tool>-<orig|seapr>.py <project>
```
* `<project>` is the project that you want to run.

For example,
```
$ cd avatar
$ python3 search-avatar-orig.py Chart_4
```

### SimAPR and GenProg
Since `SimAPR` and `GenProg` are stochastic approach, they need seed for randomness.

Usage:
```
$ cd <tool>
$ python3 search-<tool>-<simapr|genprog>.py <project> <seed>
```
* `<project>` is the project that you want to run.
* `<seed>` is the initial seed of random. It should be integer.

For example,
```
$ cd avatar
$ python3 search-avatar-simapr.py Chart_4 12345678
```

### Ablation Study
For ablation study, we run `SimAPR` without vertical and without horizontal.

We also prepared scripts to run ablation study easily.

Usage:
```
$ cd <tool>
$ python3 search-<tool>-ablation.py <project> <vertical|horizontal> <seed>
```
* `<project>` is the project that you want to run.
* `<vertical|horizontal>`: `vertical` run SimAPR without vertical search. `horizontal` run SimAPR without horizontal search.
* `<seed>` is the initial seed of random. It should be integer.

For example,
```
$ cd avatar
$ python3 search-avatar-ablation.py Chart_4 vertical 12345678
```

## 3. Output
Outputs are saved in `<tool>/result/<project>-<algorithm>`.
In this directory, logs are saved in `msv-search.log` and final results are saved in `msv-result.json`.

`msv-result.json` is the list of the results of patches:
```
{
  "execution": 0,
  "iteration": 1,
  "time": 0.16263937950134277,
  "result": false,
  "pass_result": false,
  "output_distance": -1.0,
  "out_diff": false,
  "pass_all_neg_test": false,
  "compilable": false,
  "total_searched": 1,
  "total_passed": 0,
  "total_plausible": 0,
  "config": [
    {
      "location": "/0_0_1_0_OperatorMutator/Option.java"
    }
  ]
}
```

* `iteration` is the rank of the patch.
* `time` is the time that the patch is tried.
* `result` is the result of failing tests. If `result` is true, then this patch is HQ patch.
* `pass_result` is the result of passing tests. If `pass_result` is true, then this patch is valid patch.
* `pass_all_neg_test` is the result of all failing tests. If `pass_all_neg_test` is true, then this patch passes all failing tests.
* `compilable` is the result of compilation. If `compilable` is false, then this patch is not compilable.
* `total_searched` is the number of searched patches.
* `total_passed` is the number of HQ patches.
* `total_plausible` is the number of valid patches.
* `config` is the ID of this patch.

## 4. Simulation mode
In default, SimAPR use 'simulation' mode. Under simulation mode, SimAPR 'cache' the results of test execution and reuse it at later execution.

Our scripts save cache in `<tool>/<project>-cache.json`.
Cache file is the json object of the results of test execution:
```
"/0_0_1_0_OperatorMutator/Option.java": {
  "basic": false,
  "plausible": false,
  "pass_all_fail": false,
  "compilable": false,
  "fail_time": 0.16263937950134277,
  "pass_time": 0
}
```
The keys are patch ID. `basic` represents that this patch is HQ patch, `plausible` represents that this patch is valid patch,
`pass_all_fail` represents that this patch passes all failing tests, `compilable` represents that this patch is compilable.

`fail_time` is the time for the failing tests, and `pass_time` is the time for the passing tests.
In this case, because this patch failed failing tests, SimAPR didn't run passing tests.