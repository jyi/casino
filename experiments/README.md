# Experiment

## 1. Patch Generation
For the experiment, you first need to generate patches. Since patch generation method is different for each tool, you should read each tool's README.md file.

### 1.1. TBar, Avatar, kPar and Fixminer
* ```seeds.py```: list of seeds for out experiment

### 1.2. Recoder and AlphaRepair

 * Recoder and AlphaRepair are learning-based APR tools. They require GPU to generate patches. 
 If you are using docker, you need to run it in separate docker container with `--gpus=all` options. 
* If gpus are ready, install [anaconda](https://www.anaconda.com/). 
  You can setup environment by
```
$ cd recoder  # or cd alpha-repair
$ conda env new -f data/env.yaml
$ conda activate recoder # or alpha
```


## 2. Reproduce Casino
Usage: `python3 casino-reproduce.py [options] <project> <output_dir> <casino|original|seapr> <tool> <project_path> [seed]`

* `<project>`: project to run casino (e.g. `Chart_9`).
* `<output_dir>`: output directory.
* `<casino|original|seapr>`: `<casino>`: run casino algorithm. `<original>`: follow original tool. `<seapr>`: follow SeAPR++ algorithm.
* `<tool>`: tool name. must be lower case.
* `<project_path>`: path of project (e.g. `path-to-proj/Chart_9`).
* `[seed]`: seed for Casino. default is the first seed in `seeds.py`.

### options
* `--finish-correct-patch`: finish when correct patch reached.
* `--timeout <second>`: overall timeout.
* `--max-iter <iteration>`: terminates when `<iteration>` reached.


