# SimAPR

SimAPR is a fuzzing-inspired patch scheduling algorithm for APR.

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

## Seeds
We use 50 seeds:
```
1812569871, 173066011, 3746108763, 3615336259, 2832411886, 993492328, 621082573, 119179181, 2809525537, 294562554, 343025126, 1218634673, 247518014, 1374654724, 3955729546, 1080441297, 2255798909, 1613363779, 3703518893, 322346823, 2251715956, 3197545572, 3705441198, 3770592464, 261348308, 3077341779, 319352914, 303077664, 1606862434, 992183463, 3036737114, 2593826176, 2577498044, 2421983174, 2504120438, 2071072915, 3234733127, 1994417143, 815481689, 1720353985, 3544204002, 2329962614, 2099923602, 3975296858, 327396666, 2654897829, 178583286, 4094437226, 309772218, 1337657131
```