# NeuralPass

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

As we cannot make the automated registration system for the new user within 24 hours of hackathon. If you want to run the application yourself:-

a.create a directory of your name inside faces folder.

b.save 5 photos of your clear face (face only) inside your name folder.

c. Run train_v2.py.

d.Then run modified.py

Thank you!

# About this Project :-

Neural pass is a password manager. As it is clear from the name the main motive of the app is the securely store the multiple passwords of all accounts.

But there are already n numbers of password managers in the market so what makes our Neural Password Manager so special??
The normal password manager available in the market uses a master password. So if the master password gets cracked then everything is exposed.

So to prevent we have added 2 layers of security.

1. At 1st the user must bypass the face-scanning layer to enter our application. After face scan, the application will be person-specific i.e the password that an individual person can be stored or retrieve. It uses a deep convolutional neural network for facial recognition and eye pattern recognition.

2. Secondly, the User will set the 5digit master pin while storing the password. But the pin is entered by eye pattern i.e if the user looks left pin will be 1, right 2 blinks 3. So using this combination user can store the pin.
   Also, the eye pattern entered by the user like (left, right, blink left blink, etc) is difficult to forget than the difficult password combination used for other password manager applications.

- NOTE : The architecture.py file is used to define and load the pretrained Keras_facenet model as the model was trained on old version 
of Tensorflow. For to load the model the predefined code was used.

 # Datasets can be found [here](https://drive.google.com/drive/folders/17NL3yHbIP1SI8-0pEPRPBcA9I3_JfB6_?usp=sharing)

# Demo of the project can be found [here](https://www.youtube.com/watch?v=7NtbEQ0_PFs)

                     -------ENJOY------------
