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
Before adding new algorithm, add new `mode` to use new algorithm.
In class `MSVMode`, [core.py](./core.py), add new `mode`.
```
class MSVMode(Enum):
  prophet = 1
  guided = 2
  random = 3
  original = 4
  positive = 5
  validation = 6
  spr = 7
  seapr = 8
  tbar = 9
  recoder = 10
  genprog = 11
```
Add new mode after the `genprog`.

After that, you can add your own algorithm to the SimAPR easily by modifing [select_patch.py](./select_patch.py) file.

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
We already implemented 4 algorithms: `original tool`, `GenProg` family, `SeAPR` and `Casino`.

To implements new algorithm, parameter should be `state`, contains all global information.
Then, new algorithm should select one `TbarCaseInfo`, create `TbarPatchInfo` and return it.

For example, the header of new function should be: `def select_patch_tbar_<new_algorithm>(state: MSVState) -> TbarPatchInfo`.

Implementation of `original tool` algorithm will be a good example.
```
def select_patch_tbar(state: MSVState) -> TbarPatchInfo:
  loc = state.patch_ranking.pop(0)
  caseinfo = state.switch_case_map[loc]
  caseinfo.parent.parent.parent.case_rank_list.pop(0)
  return TbarPatchInfo(caseinfo)
```
In line 2, SimAPR gets ID of the first patch from `state.patch_ranking`. `state.patch_ranking` saves the original sequence from original tool. Note that it removes selected patch from `state.patch_ranking`.

In line 3, SimAPR gets actual location of patched file from `state.switch_case_map`. `state.switch_case_map` is the mapping of patch ID and actual location of patched file.

In line 4, SimAPR removes selected patch from the remaining patch list in method level. Actually this line is for handling SeAPR algorithm, but you should insert this line just before the return.

In line 5, create `TbarPatchInfo` and return it.

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