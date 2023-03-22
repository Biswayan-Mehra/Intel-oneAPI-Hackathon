# Intel-oneAPI-Hackathon #


## Overview ##

The goal of this project is to build a prototype of a prosthetic arm that can be controlled using advanced algorithms, with a focus on showcasing the use of Intel's oneAPI toolkit. The project will involve developing a mechanical arm prototype and a software interface that allows users to control the arm movements using electroencephalography (EEG) signals.

The prosthetic arm will be equipped with sensors that can detect EEG signals from the user's brain. These signals will be processed using signal processing techniques to generate commands that control the arm's movements. The arm will be designed to perform a range of basic functions, such as grasping and releasing objects, and pointing.

Intel's oneAPI toolkit will be used to optimize the performance of the software running on the microcontroller and to configure the arm movements using servo motors and other parts. The toolkit includes libraries, compilers, and other tools that enable developers to write high-performance code for a range of hardware platforms.

The code used to develop the software interface and control the prosthetic arm will be shared on a public repository such as GitHub to encourage collaboration and knowledge sharing.

The project will require a team of software developers, electrical engineers, and prosthetic arm specialists, with a focus on open-source software and code sharing. The team will need to work closely together to develop a prototype of the prosthetic arm, design and implement the software interface, and test the device to ensure it is safe and effective for use by individuals with limb loss.

In conclusion, building a prosthetic arm using advanced algorithms and Intel's oneAPI toolkit for an Intel oneAPI Hackathon with a focus on code sharing is an exciting project that can help advance the field of prosthetics and machine learning. The project requires a team of experts with a focus on open-source software, and will involve designing and implementing a prototype of the prosthetic arm, developing a software interface, and sharing the code to encourage collaboration and knowledge sharing. The use of EEG signals and the Intel oneAPI toolkit will enable the team to develop a high-performance prosthetic arm that responds accurately and quickly to user commands.


![oneAPI-base-toolkit-3d-greybkgrnd jpg rendition intel web 480 270 (Custom)](https://user-images.githubusercontent.com/91715372/226917197-3cd4f368-29aa-4010-b464-1b2c5ab6ae28.jpg)![download (Custom)](https://user-images.githubusercontent.com/91715372/226917422-baa55962-5873-4730-bcd7-1b26d3f4713f.png)![RaspberryPiTA (Small) (Custom)](https://user-images.githubusercontent.com/91715372/226916739-1e1444c9-3542-4699-a523-528eabb5d939.jpeg)


## Prerequisites ##

> ### HARDWARE- ###

| Components | Description |
| ---------- | ----------- |
| Raspberry Pi | The Raspberry Pi is a very cheap computer that runs Linux, but it also provides a set of GPIO (general purpose input/output) pins, allowing you to control electronic components for physical computing and explore the Internet of Things (IoT). |
| Servo Motors | Content Cell |
| Jumper Wires | Content Cell |

> ### SOFTWARE- ###
- software used for 3D model is [Autodesk Fusion 360](https://www.autodesk.in/).
- software used for Sclicing is [Creality Sclicer](https://www.creality.com/).
- OS on the raspberry pi [Raspbian OS](https://www.raspberrypi.com/).
- packages and modules imported from [Intel OneAPI Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/).


## The 3D Model ##

![WhatsApp Image 2023-03-22 at 20 25 04](https://user-images.githubusercontent.com/108832092/226945619-c46db4d9-8ddf-4b12-b073-fab33d913ff6.jpg)![3d palm](https://user-images.githubusercontent.com/108832092/226946628-cf15ab71-9686-4260-833b-1349b726387b.jpg)

## Working ##

The prosthetic arm works on the signals that are transmitted from the user. The signals are then processed and converted into pulses by the raspberry pi for the servos to move accordingly. 
There are a total of 5 motors to control the fingers that are made to work in a systematic manner to perform actions that can be done by a normal human hand.


![Screenshot 2023-03-22 202015](https://user-images.githubusercontent.com/108832092/226943048-13dda4df-595a-47b7-a9d8-e86a806f05a4.png)



## Algorithm ##


1. Import required libraries: "time", onedire.eneapi", "pygame".

2. Define the GPIO pins for the servos.

3. Initialize the GPIO.

4. Initialize the PWM objects for the servos and set their frequency and enable them.

5. Define a function 'set_angle' to set the angle of a servo based on the duty cycle of the PWM signal. 

6. Define the limits and initial angles for the servos.

7. Define the speed and increment for keyboard controls.

8. Initialize Pygame and set up keyboard input.

9. Enter a main loop to read keyboard input and set servo angles:



## External Links ##

> [Medium](https://medium.com/@alanbabu_1572/real-life-applications-of-our-prosthetic-arm-technology-672516dcf83c)


