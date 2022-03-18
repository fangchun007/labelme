## Introduction
We implement the line width feature for the linestrip mode and leave the others the same in this branch. As a result, the output of labelme changes from
```
{
  "version": "5.0.1",
  "flags": {},
  "shapes": [
    {
      "label": "label_1",
      "points": [[x1,y1],[x2,y2],..., [xl,yl]],
      "group_id": null,
      "shape_type": "polygon",
      "flags": {},
    },
    {
      "label": "label_2",
      "points": [[x1,y1],[x2,y2],..., [xn,yn]],
      "group_id": null,
      "shape_type": "linestrip",
      "flags": {},
    }
  ],
  "imagePath": "satellite.jpg",
  "imageData": null,
  "imageHeight": 556,
  "imageWidth": 621
}
```
to
```
{
  "version": "5.0.1",
  "flags": {},
  "shapes": [
    {
      "label": "label_1",
      "points": [[x1,y1],[x2,y2],..., [xl,yl]],
      "group_id": null,
      "shape_type": "polygon",
      "flags": {},
      "line_width": 1  ## One more line
    },
    {
      "label": "label_2",
      "points": [[x1,y1],[x2,y2],..., [xn,yn]],
      "group_id": null,
      "shape_type": "linestrip",
      "flags": {},
      "line_width": 4  ## One more line
    }
  ],
  "imagePath": "satellite.jpg",
  "imageData": null,
  "imageHeight": 556,
  "imageWidth": 621
}
```


## Usage

Please refer to the commit or the file "line_width.patch" for the main modifications. Or you may do below.

```bash
# Install anaconda3 virtual environment
conda create --name labelme_dev python=3.6
conda activate labelme_dev

git clone https://github.com/fangchun007/labelme.git
cd labelme

# Install
pip install -e .
```

## Example
```
labelme sample_images --labels label_list.txt --nodata --validatelabel exact --config '{shift_auto_shape_color: -2}' --line_widths line_width_list.txt
```
