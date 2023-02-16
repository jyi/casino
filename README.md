# SimAPR

SimAPR is a fuzzing-inspired patch scheduling algorithm for APR.

## 1. Environments & Setup

- Python >= 3.8
- JDK 1.8
- [Defects4j](https://github.com/rjust/defects4j) 1.2.0
- Maven

### To install patch generator
Before run SimAPR, you have to generate patch candidates. We modified 6 APR tools: ```TBar```, ```Avatar```, ```kPar```, ```Fixminer```, ```AlphaRepair``` and ```Recoder```. We removed patch validation step from these tools and directly save all patch candidates.

Note: patch generator needs a lot of disk space, to save all candidates. If you use container, we highly recommend to bind the disk or volume the disk.

To compile ```TBar```, ```Avatar```, ```kPar``` and ```Fixminer```:
```
$ cd {tool}
$ ./compile.sh
```

### TODO: Recoder and AlphaRepair
For AlphaRepair and Recoder, you need GPU to generate patch candidates.
If you want to run SimAPR in container, you need `--gpus=all` option when you create a container.

Also, you need [Anaconda](https://www.anaconda.com/).

To setup ```AlphaRepair``` and ```Recoder```:
```
$ cd recoder  # or cd alpha-repair
$ conda env new -f data/env.yaml
```

### Setup SimAPR
SimAPR is implemented in Python3. SimAPR is in ```SimAPR/``` directory. To setup SimAPR:
```
$ cd SimAPR
$ python3 -m pip install -r requirements.txt
```

## 2. How to reproduce experiment
All scripts to reproduce our experiment are already prepared in ```experiments/``` directory.

Details about our experiments are explained in ```experiments/```.

## 3. Run
This section explains details how to run our implementations.

To reproduce our experiments, we highly recommend to look section 2: How to reproduce experiment.

### Run patch generator
We modified 6 APR tools to generate and save all patch candidates.
Since each tool needs different commands to run, each tool contains their own README in their directory:
- [TBar](https://github.com/CasinoRepair/SimAPR/tree/main/TBar)
- [Avatar](https://github.com/CasinoRepair/SimAPR/tree/main/AVATAR)
- [kPar](https://github.com/CasinoRepair/SimAPR/tree/main/kPar)
- [Fixminer](https://github.com/CasinoRepair/SimAPR/tree/main/Fixminer)
- [AlphaRepair](https://github.com/CasinoRepair/SimAPR/tree/main/alpha-repair)
- [Recoder](https://github.com/CasinoRepair/SimAPR/tree/main/recoder)

### Run SimAPR
Implementation of SimAPR is in ```SimAPR/``` directory.
To run SimAPR:
```
$ cd SimAPR
$ python3 simapr.py [options] -- {test_command}
```
Details are described in ```SimAPR/```.

```{test_command}``` is the command to run test. For convenience, we prepared a script to run Defects4J tests in ```SimAPR/script/d4j_run_test.py```.