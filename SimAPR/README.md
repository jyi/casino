# SimAPR

## 1. Setup
You need Python >= 3.8 to run SimAPR.

Install dependencies:
```
$ python3 -m pip install -r requirements.txt
```

## 2. Run

Run SimAPR for `TBar`, `Avatar`, `kPar` and `Fixminer`:

```
$ python3 simapr.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> -T <timeout> --use-pass-test --tbar-mode --use-exp-alpha -- python3 script/d4j_run_test.py <path_to_tbar>/buggy
```

Run SimAPR for `Recoder` and `AlphaRepair`:

```
$ python3 simapr.py -o <output_dir> -w <path_to_inputs> -m <mode> -t <single-test-timeout> -T <timeout> --use-pass-test --recoder-mode --use-exp-alpha -- python3 script/d4j_run_test.py <path_to_recoder>/buggy
```
### Options
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

## 4. Extend Patch Scheduling Algorithm
You can add your own algorithm to the SimAPR by modifing [select_patch.py](./select_patch.py) file.

### Template-based tools
For template-based tools, implements your own algorithm in `select_patch_tbar_mode` function.
```
def select_patch_tbar_mode(state: MSVState) -> TbarPatchInfo:
  if state.mode == MSVMode.tbar:
    return select_patch_tbar(state)
  elif state.mode==MSVMode.genprog:
    return select_patch_tbar_genprog(state)
  elif state.mode == MSVMode.seapr:
    return select_patch_tbar_seapr(state)
  else:
    if use_stochastic(state): 
      return select_patch_tbar_guided(state)
    else:
      return select_patch_tbar(state)
```
We already implements 4 algorithms: `original order`, `GenProg` family, `SeAPR` and `SimAPR`.

To implements new algorithm, parameter should be `state`, contains all global information.
Then, new algorithm should select one `TbarCaseInfo`, create `TbarPatchInfo` and return it.

For example, the header of new function should be: `def select_patch_tbar_<new_algorithm>(state: MSVState) -> TbarPatchInfo`.

### Learning-based tools
For learning-based tools, similar as template-based tools, implements new algorithm in `select_patch_recoder_mode` function.
```
def select_patch_recoder_mode(state: MSVState) -> RecoderPatchInfo:
  if state.mode == MSVMode.recoder:
    return select_patch_recoder(state)
  elif state.mode==MSVMode.genprog:
    return select_patch_recoder_genprog(state)
  elif state.mode == MSVMode.seapr:
    return select_patch_recoder_seapr(state)
  else:
    if use_stochastic(state):
      return select_patch_recoder_guided(state)
    else:
      return select_patch_recoder(state)
```
Same as template-based tools, we already implements 4 algorithms.
everything is same as template-based tools, but new function should select one `RecoderCaseInfo` instead of `TbarCaseInfo` and return `RecoderPatchInfo` instead of `TbarPatchInfo`.

Therefore, the header should be: `def select_patch_tbar_<new_algorithm>(state: MSVState) -> RecoderPatchInfo`.