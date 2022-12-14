# SAGE with minor modifications

This repository provides a slightly modified version of the [sage Python library](https://github.com/iancovert/sage) (version 0.0.4) to avoid occasional stack overflow on Windows. It is used by the [ShapleyVIC Python library](https://github.com/nliulab/ShapleyVIC) and is assigned a version number "0.0.4b1" to differentiate from the version on pip.

## Installation

```
pip install git+https://github.com/nyilin/sage
```

## Details on the modification

Only two lines of code in the script `utils.py` are modified: in lines 160 and 173 of `utils.py`, the function `np.maximum(...)` are changed to `max(...)`. This is because in Windows `np.maximum()` returns `int32` by default (instead of `int64` in other OS) and occasionally causes stack overflow.
