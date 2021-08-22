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

 - Please remove all comments before using the config below.

```json
{
    "linesToReplace": [
        {
            "lookFor": "M205", // Specify the command to look for.
            "replaceWith": ["p1 {0} {1} {1}", "p2 0.5 5.5"] 
            // Specify lines to replace the line with the target string. 
            // Each line is a string in the array. 
            // Use {} to bring perimeters from the original command. 
            // i.e in G1 0.1 2.2
            // {0} is 0.1 and {2} is 2.2.

        },
        {
            "lookFor": "G1",
            "replaceWith": ["P5 {0}"]

        }
    ]
}
```
