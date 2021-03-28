# NASA
 You have received a contract from NASA for software application, which will help to calculate fuel required for the flight.
 The goal of this application is to calculate fuel to launch from one planet of the Solar system, and to land on another planet of the Solar system,
 depending on the flight route.


### 1. Installation
### 2. [How to use](#example)
### 3. [Run the tests](#tests)


## Installation

#### For an example will be using `UNIX` (MacOs/Linux)

1. Open your terminal and run the next commands.
2. Create a new folder for the repo:
```bash
mkdir nasa_project
```
3. Open the new folder:
```bash
cd nasa_project
```
4. Create a virtual environment:
```bash
python3 -m virtualenv venv
```
5. Activate a virtual environment:
```bash
source venv/bin/activate
```
8. Run the next command for downloading `repo`:
```bash
git clone https://github.com/djeck1432/NASA.git
```
9. Open the repo:
```bash
cd NASA
```
10. Install all requirement packages:
```bash
pip3 install -r requirements.txt
```
11. Run the script:
```bash
python3 calculate_fuel.py
```


## How to use
#### Example
<a name='example'> </a>
1. Run the app:
```bash
python3 calculate_fuel.py
```
2. Input a weight of equipment, as in the example:
```bash
Please, input weight of equipment:
28801
```
3. Input gravity for launching:
```bash
Please, input gravity for launching: 
9.807
```
4. Input gravity for landing:
```bash
Please, input gravity for landing: 
1.62
```
5. If you would like to get a result, press `r`, if you would like to add extra route, press `c`:
```bash
If you would like to get a result, press:  r
If you would like to continue, press:  c
r or c
```
6. Get a weight fuel:
```bash
Total weight fuel 22380 kg
```


## Run the tests
<a href='test'></a>
In terminal, in root folder, run the next command:
```bash
pytest tests.py
```
### Test data
#### Apollo 11:
  path: launch Earth, land Moon, launch Moon, land Earth
  weight of equipment: `28801` kg
  weight of fuel: `51898` kg
  arguments: `28801`, `[[:launch, 9.807], [:land, 1.62], [:launch, 1.62], [:land, 9.807]]`
#### Mission on Mars:
   path: launch Earth, land Mars, launch Mars, land Earth
   weight of equipment: `14606` kg
   weight of fuel: `33388` kg
   arguments: `14606`, `[[:launch, 9.807], [:land, 3.711], [:launch, 3.711], [:land, 9.807]]`
#### Passenger ship:
   path: launch Earth, land Moon, launch Moon, land Mars, launch Mars, land Earth
   weight of equipment: `75432` kg
   weight of fuel: `212161` kg
   arguments: `75432`, `[[:launch, 9.807], [:land, 1.62], [:launch, 1.62], [:land, 3.711], [:launch, 3.711], [:land, 9.807]]`

