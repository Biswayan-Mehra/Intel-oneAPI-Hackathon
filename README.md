# Intel-oneAPI-Hackathon #

## Project Title - Advanced Prosthetic Arm


## Overview ##

The goal of this project is to build a prototype of a prosthetic arm that can be controlled using advanced algorithms, with a focus on showcasing the use of Intel's oneAPI toolkit. We have developed a mechanical arm model by 3D printing it that will allow the user to perform the desired action using the signals provied by the brain.

The prosthetic arm will be equipped with sensors that can detect EEG signals from the brain. The transmitted signals will be processed using signal processing techniques to generate commands that will be processed by the raspberry pi and the designated movement will take place like grasping, pointing, releasing.

The microcontroller software will be optimized for performance using Intel's oneAPI toolkit, and the arm movements will be programmed using servo motors and other components. For a variety of hardware platforms, developers can write high-performance programs using the toolkit's libraries, compilers, and other tools.

The code used to develop the software interface and to control the prosthetic arm is shared above in the repository.


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

![WhatsApp Image 2023-03-22 at 20 25 04](https://user-images.githubusercontent.com/108832092/226945619-c46db4d9-8ddf-4b12-b073-fab33d913ff6.jpg)![3d palm (1)](https://user-images.githubusercontent.com/108832092/226949969-0f975b8a-c520-4858-8f4b-444e74b52aa1.jpg)


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


## Our Team ##

Our team comprised of Developers with expertise in the Internet of Things, software development, design, and mechanical engineering were involved in our project. We as a team collaborated closely to create a prototype of the prosthetic arm, design and implement the software interface, and test the apparatus to make sure it is secure and useful for people who have lost their arms.

- IoT and Hardware development - @chris-x0
- Software development - @Biswayan-Mehra
- 3D designing and Mechanics- @Alan7149
- rendering and editing - @

## Conclusion ##

In conclusion, creating a prosthetic arm for an Intel oneAPI Hackathon with a focus on code sharing using cutting-edge algorithms and Intel's oneAPI toolkit is an exciting project that can advance the field of prosthetics and machine learning. The project will involve creating a prototype of the prosthetic arm, putting it into use, creating a software interface, and sharing the source code to promote cooperation and knowledge sharing. It will require a team of experts with a focus on open-source software. The team will be able to create a high-performance prosthetic arm that reacts precisely and quickly to user commands thanks to the use of EEG signals and the Intel oneAPI toolkit.

## External Links ##

> [Medium](https://medium.com/@alanbabu_1572/real-life-applications-of-our-prosthetic-arm-technology-672516dcf83c)
> [Youtube]()


