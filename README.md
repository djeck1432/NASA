# NASA
 You have received a contract from NASA for software application, which will help to calculate fuel required for the flight.
 The goal of this application is to calculate fuel to launch from one planet of the Solar system, and to land on another planet of the Solar system,
 depending on the flight route.

# Menu:
1.Installation
2. <a name='example'>How to use </a>


## Installation

#### In example will be use `UNIX` (MacOs/Linux)

1. Open your terminal. 
2. Create new folder for the repo, run the next command:
```bash
mkdir nasa_project
```
3. Move to new folder, run the next command:
```bash
cd nasa_project
```
4. Create virtual enviroment, run the next command:
```bash
python3 -m virtualenv venv
```
<a name="env"></a> 
5. Activate virtual enviroment, run the next command:
```bash
source venv/bin/activate
```
6. Create folder for the app:
```bash
mkdir app
```
7. Open your `app` folder:
```bash
cd app
```
8. Run the next command for downloading `repo`:
```bash
git clone https://github.com/djeck1432/NASA.git
```
9. Install all requirement packages, run the next command:
```bash
pip3 install -r requirements.txt
```
10. Run the app:
```bash
python3 calculate_fuel.py
```


## How to use
#### Example
[](#example)
1. Run the app:
```bash
python3 calculate_fuel.py
```
2. Input a weight of equipment, as in example:
```bash
Please, input,  weight of equipment:
28801
```
3. Input gravity for launching:
```bash
Please, input, gravity for launching: 
9.807
```
4. Input gravity for landing:
```bash
Please, input, gravity for landing: 
1.62
```
5. If you would like get a result, press `r` if you would like add extra root, press `c`:
```bash
If you would like to get a result, press:  r
If you would like to continue, press:  c
r or c
```
6. Get a weight fuel:
```bash
weight_fuel
```



