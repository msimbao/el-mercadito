# el-mercadito

<img src="https://cdn.glitch.com/d1bfb408-31f7-459b-bafc-b4ec0e9149e6%2FEl%20Mercadito%20graphic.png?v=1610583846301" width="300" height="300"/>

A Digital Information Marketplace For Alight's Pedacito De La Tierra Shelters. This was a project made during the Mac Explore Challenge where teams were asked to build a possible solution for alights case study on helping families on the move better deal ncreased restrictions at the border.

The front facing part of the project is free to view at: [El-Mercadito](https://el-mercadito.glitch.me/)

The Final Team Presentation is available to view here: [Team Presentation](https://drive.google.com/file/d/1Ua0eb7xrdso2DxTQuf0efCekHtPOofcD/view)

The files contained in the 'files' folder at the top of this repository are all python scripts to support the call program. If you want to look at the Javascript code for the front facing site, it can be found here: [Front Code](https://glitch.com/edit/#!/el-mercadito)

Please not that the system can be run entirely using the python scripts without the front website. The site is more of a demo for how Alight could have their own console on their current site to manage and see incoming data.

### Measuring Impact

The simple way we tried to measure impact was by directly allowing users to tell us how useful the platform has been for them and what area of their life the information has played a positive role in.

We also collect usage statistics based on who needs information and who is offering information and hope to say that if the platform is growing then more and more people are finding it to be useful for their needs.

These are not perfect metrics but we hope they can give us some light into the impact the platform is having.

These are collected via sms commands explained in the usage section.

![Metrics](https://github.com/msimbao/el-mercadito/raw/main/Images/a.png)
![Metrics](https://github.com/msimbao/el-mercadito/raw/main/Images/b.png)

### Infrastructure

This system was built using Twilio as a communication API, Firebase as a cloud database and Flask for making a server. Entry is through two pathways, messaging or calling. if you message, you can leave feedback, get latest posts or make a post. If you call, you can make a post as a recording that will be transcribed by a moderator or by the google translate API. Translation is also available for sms messages through the google translate API. 

Below is an image showing the basic infrasturcture of the project, and the firebase and Twilio consoles.

![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/8.png)

### Dependencies

* firebase_admin
* flask
* twilio

### Executing program

* Install and initialize Ngrok

```
pip install ngrok

ngrok http 5000
```

* Open a new Twilio Account and configure the webhook for receiveing calls and messages using the ngrok url and these instructions:

*[Video To connect Code to Twilio API for Recieving Calls](https://www.youtube.com/watch?v=-AChTCBoTUM)

*[Video To connect Code to Twilio API for Recieving Messages](https://www.youtube.com/watch?time_continue=102&v=cZeCz_QOoXw&feature=emb_title)

* Launch a Terminal and the recieve_call.py script. Launch another terminal to run the recieve_sms.py script

```
python receive_call.py

python receive_sms.py
```

### Usage

#### Submit A Post Via Voice

To submit a post as a recording, simply call your Twilio provided phone number (in our case, it was +13204336207)

Twilio Will greet you with message telling you that you have a trial account. Then you will be greeted by El-Mercadito's greetings in Spanish and English. You can then record your call. 

The Video Below Shows this in greater detail.

[Video Call Example](https://drive.google.com/file/d/1_qlhDhVv4N9j8cqz5YM7nRh03cxdx020/view?usp=sharing)

#### Submit A Post Via SMS

To submit a post as a message, simply send a text message to the number

It will respond to confirm that your message has been received.

![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/4.jpg)

#### Get N number of Latest Stories

To Query the database via sms, simply send a text message with the number of stories you want sent to you. The simple command is:

```
N stories

# Here N stands for the number of stories you want to recieve
```
![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/5.jpg)
![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/new6.jpg)

#### Submit Feedback

To submit negative feedback, simply sms the command shown below.

```
not useful

```

To submit positive feedback, simply sms the command shown below.

```
useful for A

# Where A is an area of your life that you have found useful information for such as education, products or services 
```

![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/7.jpg)

## Authors

Team 

* Ama Kyereme 
* Zoey Pham
* Alessandra Rosa Policarpo
* Mphatso Simbao

## Acknowledgments

Inspiration and Thanks

* Alight - Host
* Marie Deschamps - Mentor
* Macalester College - Coordinator

