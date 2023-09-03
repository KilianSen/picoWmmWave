# HumanStaticLitePy
Is a library used to communicate with a seeed studio 24ghz human presence sensor using (micro)python.

This has been created using [Seeed Studio Usage Protocol](https://0.0.0.0/) and trial and error.

# Installation
### PIP
```commandline
pip install HumanStaticLitePy
```
### Source
```commandline
wip
```

# Usage
```python
import HumanStaticLite

```

### API
The API is used to parse and create frames (consisting of bytes) sent by the sensor or to be sent to the sensor.


#### Parsing data
```python
from HumanStaticLite.API.Frame import Frame
from HumanStaticLite.API.ControlAndCommandWords import *

some_data_sent_by_the_sensor: bytes = b'SY000000TC' #Not real data

parsed_frame = Frame.parse(some_data_sent_by_the_sensor)
print(parsed_frame.command, parsed_frame.data, parsed_frame.raw_frame.control_word)

```
Will return `FirmwareVersionQuery, b'v1.ab', ProductInformation` (for example)

#### Sending data
```python
from HumanStaticLite.API.Frame import Frame
from HumanStaticLite.API.ControlAndCommandWords import *

data = Frame(SystemFunctionsCommandWords.ModuleReset, b'\x01')

print(data.to_bytes())
```

Will return `b'SY000000TC'` for example