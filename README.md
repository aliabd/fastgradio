[![PyPI version](https://badge.fury.io/py/fastgradio.svg)](https://badge.fury.io/py/fastgradio)
# fastgradio
`fastgradio` is a python library to quickly build and share gradio interfaces of your trained fastai models. 

To use it simply 
```python

pip install fastgradio 

```
Then 

```python

from fastgradio import Demo 
Demo(learner).launch()
```

This will create an interface like the one below: 

<img src="https://i.ibb.co/NjSG5xv/dog-interface.gif"/>

For more info on usage, check the [example notebook](https://github.com/aliabd/fastgradio/blob/main/examples/Using%20fastgradio%20with%20Vision.ipynb)

*Note: We are working on expanding this to support all data types in fastai. Currently only supports image-to-label interfaces. PRs are welcome!*
