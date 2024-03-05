# PC-SPECS

## Description

pc-specs is a service to saving your computer specifications.

## Installing

### Requirements

* [See requirements](requirements.txt)

### Install (Linux)

1. Сlone the repository to the selected folder ```git clone https://github.com/next128/pc-specs.git``` and go to the repository folder ```cd YOUR_FOLDER/pc-specs```
2. If you don't have python virtual environment, install it in repository folder: ```python3 -m venv venv```
3. Connect venv ```source venv/bin/activate```
4. Upgrade pip ```pip install --upgrade pip```
5. Install requirements ```pip install -r requirements.txt```
6. Apply Database changes ```python3 manage.py makemigrations``` and then ```python3 manage.py migrate```

### Install (Windows)

1. Сlone the repository to the selected folder ```git clone https://github.com/next128/pc-specs.git```
2. Open YOUR_FOLDER/pc-specs in your IDE (pycharm, for example)
3. If you don't have python virtual environment, install it in repository folder: ```python -m venv venv```
4. Set new venv in IDE (Add new interpreter -> then select venv/Scripts/python.exe)
5. Upgrade pip ```pip install --upgrade pip```
6. Install requirements ```pip install -r requirements.txt```
7. Apply Database changes ```python manage.py makemigrations``` and then ```python manage.py migrate```


### Run

1. To run web-server ```python manage.py runserver```

## Screenshots

![first_img](https://media.discordapp.net/attachments/826419939924639784/1214542952618131497/image.png?ex=65f97e45&is=65e70945&hm=a6f5a264e734ae92dc87217f746dd83fc4c00644009026ee581d1099614deedc&=&format=webp&quality=lossless&width=842&height=474)
![second_img](https://media.discordapp.net/attachments/826419939924639784/1214542993193705472/image.png?ex=65f97e4e&is=65e7094e&hm=e0a81fe194d9679fb59adf5eedeba67be814987dd555596924621d7e92da19bd&=&format=webp&quality=lossless&width=842&height=474)
![third_img](https://media.discordapp.net/attachments/826419939924639784/1214543017986359336/image.png?ex=65f97e54&is=65e70954&hm=0781ccc09c0e13040f0fd34e50ee818e6fab31566caabc21ef1d52b156e4adfe&=&format=webp&quality=lossless&width=842&height=474)
![fourth_img](https://media.discordapp.net/attachments/826419939924639784/1214543194797252608/image.png?ex=65f97e7e&is=65e7097e&hm=4d6cc55fcd235f2197ab8241f25a9e90edde22fe32a801c381a4e2dec1095ca5&=&format=webp&quality=lossless&width=842&height=474)
![fifth_img](https://media.discordapp.net/attachments/826419939924639784/1214543244180987904/image.png?ex=65f97e8a&is=65e7098a&hm=35a64565ed39a2ec0e5609839ef545ee9d02a46cc69667691da413f40d961a2e&=&format=webp&quality=lossless&width=842&height=474)
