Detecting bodies of water using Python

```py
import cv2 as cv
import numpy as np
print(cv.__version__)
print(np.__version__)
```

And run with `python3 detector.py`. My output is:

```sh
3.4.2
1.15.0
```

## Todo
- Ag reservoirs vs natural - Yes he could use knowing the difference

- Does he need to know the min/max acres of water mass - No, even the really small ones "could" add some value to what he wants to build

- Do we want to know between lined and not lined reservoirs? Yes, that is very helpful info.

