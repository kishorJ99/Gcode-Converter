# Gcode-Converter
## How to Run
1. `cd` into the repo/folder
2. Run the command below
```bash
python gcodeTo3DPCode.py test.gcode config.json
# python gcodeTo3DPCode.py <input gCode file> <config file>
```
3. See your output in `output.txt`

## How to Config

| Config Value  | Comments      |
| ------------- | ------------- |
| startOn       | Contains an array of array that each define perimeters that must be found on a line to insert the start commands on. |
| stopOn        | Contains an array of array that each define perimeters that must be found on a line to insert the stop commands on. |
| startCommand  | Array of start commands to insert | 
| stopCommand   | Array of stop commands to insert | 

```json
{
    "startOn": [["G1", "E"]],
    "stopOn" : [["G0"], ["G1", "F1000"]],
    "startCommand" : ["start1"],
    "stopCommand" : ["stop1"]

}
```
