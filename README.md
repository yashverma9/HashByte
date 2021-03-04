# HashByte
- Team Name: HashByte
- Team Members: Tanmay Shishodia, Vedant Saxena, Yash Verma
- Project Title: HashByte


Project Domain: 
Our project falls under the following domains: Deep Learning (Machine Learning), Web Development, AR

Abstract:
With our project we aim at providing a complete bundle of tech-tools for making education easier and fun in an interactive way. There are two components in our solution. Firstly, an AR application which turns any book into an interactive experience with the power of Augmented Reality, and secondly, a web application that runs along with your online-class software and helps you out with doubt clarification and detailed notes in real-time.

Introduction:
In the present times of the pandemic, online-classes have become the new reality for education. Limited duration of classes and no direct interaction with the teachers has made it very tough for students to grasp concepts and learn new things. Due to these constraints, students never have enough time to get their doubts cleared. Hence, we present our solution which not only solves the above-mentioned problems but also makes learning a fun and interactive activity.

In our AR application, the student can directly scan any page of book and view more information about those topics in forms of videos, animations, photos, definitions and related links presented in Augmented Reality. 

In our online-class assistance application, the students can open our application besides their online class and get detailed information about what the teacher is talking about in real-time. Our application identifies the topic the teacher is presently talking about and provides the assistance to the student in forms of videos, animations, photos, definitions and related links. 

Our application also provides an option to save the notes for future reference.


Approach

The approach can be divided into 2 parts based on the 2 different aspects of our solution.

In the AR application, the page scanned will be recognized by our AR model created using Unity3D and Vuforia and the topic identified will be web scraped for more information. The results of web scraping are displayed in Augmented Reality over the page currently in the camera view.

In the online-class assistance application, speech-to-text machine learning model detects the concepts the teacher is teaching presently. Then the keyword detection model identifies the topic and that topic is web scraped for more detailed information. The results are displayed on our web application besides the online-class software.  

Advantages of your Solution
- Easy to use (only involves scanning a page and opening the app beside the class)
- Provides results in real-time.
- Support for both mobile and laptops (PCs)

Pitfalls of your Solution
- Machine learning Models not identifying the topics accurately
- The AR application might not work on very small sized fonts of books

Future Scope
- Better integration with mobile version of online-class software.
- Support for chrome extensions.

Ease of Implementation
Proper training of machine learning models can make real life deployment of our project very practical. For providing real-time assistance, high speed servers and high processing power is required. Hence with availability of proper resources, our project can be implemented easily.

Tech Stack
- VueJs
- PyAudio 
- EasyOcr for Image to Text
- BeautifulSoup for Web Scraping
- Watson Speech-To-Text API
- Flask (Python3)
- Postman
- Unity3D
- Vuforia

Instructions to run application
- Back-end:
```
cd flask-backend
python3 app.py
```

- Client side:
```
cd client
npm i
npm run serve
```

For Unity:
Install the apk and run the application.
