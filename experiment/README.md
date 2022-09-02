# Experiment

## TBar, Avatar, kPar and Fixminer
* ```d4j_<tool>.py```: list of versions that have correct patch or plausible patches
* ```correct-<tool>.csv```: list of correct patches
* ```seeds.py```: list of seeds for out experiment

## Recoder and AlphaRepair

 * Recoder and AlphaRepair are learning-based APR tools. They require GPU to generate patches. 
 If you are using docker, you need to run it in separate docker container with `--gpus=all` options. 

## Reproduce Casino
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

# Versions

## Versions for correct patches
Versions that could find correct patches reported by each paper. Note that we exclude versions whose correct patch is found at over 10,000 iterations.

Note: If the version is multi-fault, we divide it into multiple versions with single-fault manually. (e.g. Chart_14, Chart_14002, Chart_14003, Chart_14004)
### TBar
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 4, 8, 9, 11, 14, 19, 20, 24|9|
|Closure|2, 21, 38, 46, 62, 63, 73, 86|8|
|Lang|10, 33, 47, 57, 59|5|
|Math|4, 5, 11, 22, 30, 34, 35, 57, 58, 65, 70, 75, 77, 79, 80, 89|16|
|Mockito|38|1|
|Time|7|1|
|total||40|

### Avatar
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 4, 11, 19, 24|5|
|Closure|2, 38, 46, 62, 63, 73, 115, 126|8|
|Lang|6, 7, 10, 57, 59|5|
|Math|4, 33, 59, 85, 89|5|
|Mockito|29, 38|2|
|Time|7|1|
|total||26|

### kPar
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 4, 7|3|
|Closure|2, 38, 62, 63, 73|5|
|Lang|59|1|
|Math|15, 33, 58, 70, 75, 85, 89|7|
|Mockito|38|1|
|Time|7|1|
|total||18|

### Fixminer
We exclude Chart_24, since its correct patch is in sub-template.
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 4, 11, 19|4|
|Closure|10, 38, 62, 63, 73|5|
|Lang|57, 59|2|
|Math|22, 30, 34, 35, 57, 70, 75, 79, 82|9|
|Mockito|29, 38|2|
|Time||0|
|total||22|

### Recoder

|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 3, 8, 9, 11, 20, 24, 26 |8|
|Closure|2, 14, 21, 33, 46, 57, 62, 63, 73, 86, 92, 93, 104, 109, 115, 118 |16|
|Lang|6, 26, 51, 55, 57, 59 |6|
|Math|5, 27, 30, 33, 34, 41, 50, 57, 65, 70, 75, 94, 96, 98, 105 |15|
|Mockito|38|1|
|Time|7|1|
|total||47|

### AlphaRepair

|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 8, 9, 11, 24, |5|
|Closure|21, 46, 57, 73, 86, 92, 93, 115|8|
|Lang|4, 29, 33, 61 |4|
|Math|30, 41, 50, 57, 59, 63, 65, 70, 75, 90, 94, 96, 98 |13|
|Mockito|29|1|
|Time|7|1|
|total||32|

## Versions for plausible patches
We use versions that could generate correct patch and version that could generate plausible patches in 10,000 iterations, reported by [On the Efficiency of Test Suite based Program Repair](https://anilkoyuncu.github.io/papers/ICSE2020.pdf).
### TBar
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 19, 20, 24, 25, 26|16|
|Closure|2, 12, 21, 22, 38, 46, 62, 63, 66, 73, 86, 107, 109, 126, 133|15|
|Lang|10, 13, 18, 20, 22, 24, 27, 33, 39, 41, 43, 44, 45, 47, 51, 57, 58, 59, 60, 63|20|
|Math|2, 4, 5, 6, 8, 11, 15, 22, 30, 34, 35, 50, 57, 58, 62, 63, 65, 70, 75, 77, 79, 80, 81, 82, 84, 85, 88, 89, 95, 96|30|
|Mockito|38|1|
|Time|7|1|
|total||83|

### Avatar
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 4, 5, 7, 11, 13, 14, 15, 19, 24, 25, 26|12|
|Closure|2, 12, 21, 22, 38, 45, 46, 48, 62, 63, 66, 73, 108, 115, 126|15|
|Lang|6, 7, 10, 13, 20, 22, 27, 39, 51, 57, 58, 59, 63|13|
|Math|2, 4, 6, 33, 49, 50, 57, 59, 62, 78, 80, 81, 82, 84, 85, 88, 89, 95, 104|19|
|Mockito|29, 38|2|
|Time|7|1|
|total||62|

### kPar
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 3, 4, 5, 7, 12, 13, 14, 15, 17, 19, 25, 26|13|
|Closure|2, 35, 38, 40, 46, 62, 63, 73, 109, 115, 126, 129|12|
|Lang|7, 10, 16, 18, 20, 21, 24, 27, 41, 43, 44, 45, 51, 53, 57, 58, 59, 63|18|
|Math|2, 7, 8, 15, 33, 40, 42, 43, 49, 50, 58, 62, 63, 70, 75, 80, 81, 82, 84, 85, 88, 89, 104|23|
|Mockito|38|1|
|Time|7|1|
|total||68|

### Fixminer
|Project|Versions|Total|
|:---:|:---|:---:|
|Chart|1, 3, 4, 7, 11, 12, 13, 14, 15, 17, 19, 25|12|
|Closure|10, 19, 38, 62, 63, 73, 129|7|
|Lang|57, 59, 63|3|
|Math|20, 22, 30, 33, 34, 35, 50, 57, 63, 70, 75, 79, 82, 84|14|
|Mockito|29, 38|2|
|Time|11, 19|2|
|total||40|
