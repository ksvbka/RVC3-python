# bdsim models

This folder holds a number of [bdsim](https://github.com/petercorke/bdsim) models for the textbook "_Robotics, Vision & Control, edition 3 in Python_".

[bdsim](https://github.com/petercorke/bdsim) is a Python package that allows you to express block diagrams in terms of lines of code, ie. create blocks and wires, and them simulate the time response of the system.

## The files

For each bdsim model called `model` there can be many related files

| File name      |     Description                  |
| -------------- | -------------------------------- |
| model.py       | a Python+bdsim implementation of the model |
| model.bd       | a block diagram drawn with bdedit (a JSON file) |
| model-main.py  | a "main" function called by a complex bdsim model file |

## `model.py`

This is a pure Python file that uses `bdsim` classes to implement a system model in terms of
blocks and interconnections.  You run it directly from the command line
```
$ python model.py
```
or
```
$ ./model.py
```
or from inside Jupyter or IPython by
```
%run -m model
```

## `model.bd`
You can open a model file using the Qt-based graphical tool `bdedit`, from the command line, by
```
$ bdedit model.bd
```
and execute the model by pushing the run button.  This will invoke `bdrun` which will load and parse `model.bd`,
build a block diagram and execute it.


## `model-main.py`
This approach is used for a "complex" model file that contains a "Main" block.
It comprises a `bdsim` model called `model.bd` as well a Python file `model-main.py`, referenced by the "Main" block,
which sets up the Python objects required for the bdsim model, then imports that model and executes it.

You run it directly from the command line
```
$ python model-main.py
```
or
```
$ ./model-main.py
```
or from inside Jupyter or IPython by
```
%run -m model-main.py
```

Alternatively you can run the editor
```
$ bdedit model.bd
```
and press the run button which will perform the action described above.






## Installing bdsim

`bdsim` requires Python 3.8 or better, and is installed as part of the `rvc3python` install.  To install it explicitly

```
$ pip install bdsim
```

Many of these models require additional installed toolboxes, which are not a dependency of `bdsim`
```
$ pip install roboticstoolbox-python
$ pip install machinevisiontoolbox-python
```