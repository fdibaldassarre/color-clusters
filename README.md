# color-clusters
Find the main colors in an image.

## Requirements

- Python 3
- Numpy
- Scipy
- imageio

## Usage

```sh
./clusters.py image.png output.png number_of_clusters
```

## Examples

Input image:

![input](https://raw.githubusercontent.com/fdibaldassarre/color-clusters/master/examples/input.png)

Find 3 colors:

```sh
./clusters.py examples/image.png examples/output3.png 3
```

![input](https://raw.githubusercontent.com/fdibaldassarre/color-clusters/master/examples/output3.png)

Find 5 colors:

```sh
./clusters.py examples/image.png examples/output5.png 5
```

![input](https://raw.githubusercontent.com/fdibaldassarre/color-clusters/master/examples/output5.png)
