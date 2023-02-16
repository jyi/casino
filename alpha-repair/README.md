# AlphaRepair

## Patch Generation

0. Set environment

You need to install java, defects4j, [anaconda](https://www.anaconda.com/).

Then, run

```
conda env create -f data/env.yaml
conda activate recoder
```

1. Generate patch candidates

    For Chart-1,

    ```
    python3 experiment.py --bug_id Chart-1 --output_folder d4j --skip_v --re_rank --beam_width 5 --top_n_locations 40
    ```

