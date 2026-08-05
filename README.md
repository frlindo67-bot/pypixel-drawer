# pypixel-drawer

Simple Python library for drawing pixel art using the Turtle module.

## Features

- Draw colored pixels
- Change pixel size
- Easy to use
- Beginner-friendly

## Installation

```bash
pip install pypixel-drawer
```

## Example

```python
import turtle as t
import pypixel_drawer as px

px.set_pixel_size(20)

px.pixel(0, 0, "red")
px.pixel(20, 0, "blue")
px.pixel(40, 0, "green")

t.done()
```

## License

MIT License