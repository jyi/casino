# SimAPR

SimAPR is a replay-based patch-scheduling simulation system. Running an APR tool takes long. The patch space is large and it takes long to build and test each patched program. This makes it difficult to experiment with diverse patch schedulig algorithms. SimAPR caches information for individual patch such as time taken to run the patched program and the result of testing. This cached information is used when evaluating a patch-scheduling algorithm given to SimAPR as an input.

## 1. Environments & Setup

### Environment
- Python >= 3.8
- JDK 1.8
- [Defects4j](https://github.com/rjust/defects4j) 1.2.0
- Maven

### 1.1. To install patch generator
Before run SimAPR, you have to generate patch candidates. We modified 6 APR tools: ```TBar```, ```Avatar```, ```kPar```, ```Fixminer```, ```AlphaRepair``` and ```Recoder```. We removed patch validation step from these tools and directly save all patch candidates.

Note: patch generator needs a lot of disk space, to save all candidates. If you use container, we highly recommend to bind the disk or volume the disk.

To compile ```TBar```, ```Avatar```, ```kPar``` and ```Fixminer```:
```
$ cd {tool}
$ ./compile.sh
```

#### 1.1.1. AVATAR

Before patch generation, you should change paths in script to correct absolute path of your environment.

In `AVATAR/FLFix.sh`, you should change
  - `d4jData` to `./AVATAR/buggy` as absoulte path.
  - `d4jPath` to the path of defects4j.

### 1.2. Recoder and AlphaRepair
For AlphaRepair and Recoder, you need GPU to generate patch candidates.
If you want to run SimAPR in container, you need `--gpus=all` option when you create a container.

Also, you need to install [Anaconda](https://www.anaconda.com/).

To setup ```AlphaRepair``` and ```Recoder```:
```
$ cd recoder  # or cd alpha-repair
$ conda env create -f data/env.yaml
$ conda activate recoder # or alpha
```

#### 1.2.1. Prepare Recoder Model
For the case of ```Recoder```, you should prepare model first.
You can train model yourself or get the pre-trained model from docker image.

```
sudo docker pull zqh111/recoder:interface
```

Model is in `/root/Repair/checkpointSearch/best_model.ckpt` image.
Copy this file to this directory.

```
mkdir checkpointSearch
cp /root/Repair/checkpointSearch/best_model.ckpt ./checkpointSearch
```

### Setup SimAPR
SimAPR is implemented in Python3. SimAPR is in [SimAPR/](./SimAPR/) directory. To setup SimAPR:
```
$ cd SimAPR
$ python3 -m pip install -r requirements.txt
```

## 2. How to reproduce our experiment
All scripts to reproduce our experiment are in [experiments/](./experiments/) directory.

Details about our experiments are explained in [experiments/](./experiments/).

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
Implementation of SimAPR is in [SimAPR/](./SimAPR) directory.
To run SimAPR:
```
$ cd SimAPR
$ python3 simapr.py [options] -- {test_command}
```
Details are described in [SimAPR/](./SimAPR/README.md).

```{test_command}``` is the command to run test. For convenience, we prepared a script to run Defects4J tests in ```SimAPR/script/d4j_run_test.py```.
