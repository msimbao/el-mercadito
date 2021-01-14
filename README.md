# el-mercadito
A Digital Information Marketplace For Alight's Pedacito De La Tierra Shelters. This was a project made during the Mac Explore Challenge where teams were asked to build a possible solution for alights case study on helping families on the move better deal ncreased restrictions at the border.

The front facing part of the project is free to view at: [El-Mercadito](https://el-mercadito.glitch.me/)

![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/3.png)

## Description

Covid 19 and the Migration Protection Protocols have increased the hardships of families on the move, by augmenting immigration procedures’ delays and incertitude, while reducing safe shelters at the Mexican side of the US border.

Thanks to Alight and their partners such as the Catholic sisters, these vulnerable families are offered the protection they deserve: Pedacito de la Tierra, a place to rest and make decisions, a place to build community and restore their well being.

Building on this existing infrastructure and addressing the practical needs of these families, we are pleased to introduce an empowering platform: El Mercadito, an online and secure market place and message board, where families can share their needs, seek answers and propose their services, and be connected to shelters and support resources both locally and regionally.


### Measuring Impact

The simple way we tried to measure impact was by directly allowing users to tell us how useful the platform has been for them and what area of their life the information has played a positive role in.

We also collect usage statistics based on who needs information and who is offering information and hope to say that if the platform is growing then more and more people are finding it to be useful for their needs.

These are not perfect metrics but we hope they can give us some light into the impact the platform is having.

These are collected via sms commands explained in the usage section.

![Metrics](https://github.com/msimbao/el-mercadito/raw/main/Images/Screen Shot 2021-01-14 at 10.48.18 AM.png)
![Metrics](https://github.com/msimbao/el-mercadito/raw/main/Images/Screen Shot 2021-01-14 at 10.48.30 AM.png)

### Infrastructure

This system was built using Twilio as a communication API and Firebase as a cloud database. Entry is through two pathways, messaging or calling. if you message, you can leave feedback, get latest posts or make a post. If you call, you can make a post as a recording that will be transcribed by a moderator or by the google translate API. Translation is also available for sms messages through the google translate API. 

Below is an image showing the basic infrasturcture of the project, and the firebase and Twilio consoles.

![Dashboard](https://github.com/msimbao/el-mercadito/raw/main/Images/8.png)

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Executing program

* Install and initialize Ngrok

```
pip install ngrok

ngrok http 5000
```

* Open a new Twilio Account and configure the webhook for receiveing calls and messages using the ngrok url and these instructions:

*[Video To connect Code to Twilio API for Recieving Calls](https://www.youtube.com/watch?v=-AChTCBoTUM)

*[Video To connect Code to Twilio API for Recieving Calls](https://www.youtube.com/watch?time_continue=102&v=cZeCz_QOoXw&feature=emb_title)

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

