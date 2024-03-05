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

![first_img](https://media.discordapp.net/attachments/826419939924639784/1214242351388819556/image.png?ex=65f86650&is=65e5f150&hm=b7c23eba011ffd077c46ee1e075df2fb34280ec8ad9aea3b3750fe1f77c3e3dc&=&format=webp&quality=lossless&width=842&height=474)
![second_img](https://media.discordapp.net/attachments/826419939924639784/1214242394237571092/image.png?ex=65f8665a&is=65e5f15a&hm=c386f072713fa4684e19e0eaaf79ead3a2c364be4c1d5c5bd8158559e2fc63d4&=&format=webp&quality=lossless&width=842&height=474)
![third_img](https://media.discordapp.net/attachments/826419939924639784/1214242415997620314/image.png?ex=65f8665f&is=65e5f15f&hm=5f4a56fe5153c354a4ca535362bba80186aefee2c35265a8eccffda39be0ce0f&=&format=webp&quality=lossless&width=842&height=474)
![fourth_img](https://media.discordapp.net/attachments/826419939924639784/1214242436377878568/image.png?ex=65f86664&is=65e5f164&hm=7f403809fa19cd609271bc46b7498b5eea5128999ee2dc9cbf484c4c45e8e471&=&format=webp&quality=lossless&width=842&height=474)
