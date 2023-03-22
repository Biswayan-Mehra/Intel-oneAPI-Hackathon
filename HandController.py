import RPi.GPIO as GPIO
import pygame
import time

# Define servo pins
servo_pins = [18, 19, 20, 21, 22]

# Define servo limits and initial angles
servo_limits = [(0, 180)] * 5  # (min_angle, max_angle) for each servo
servo_angles = [90] * 5  # Initial angle for each servo

# Define servo speed and increment for keyboard controls
servo_speed = 5  # Degrees per keyboard press
servo_increment = 1  # Degrees per update

# Initialize Pygame
pygame.init()

# Set up keyboard input
keys_pressed = set()

# Define Pygame window and clock
window_size = (640, 480)
window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# Setup GPIO
GPIO.setmode(GPIO.BCM)
try:
    for pin in servo_pins:
        GPIO.setup(pin, GPIO.OUT)

    # Initialize PWM objects
    pwms = {}
    for pin in servo_pins:
        pwm = GPIO.PWM(pin, 50)
        pwm.start(0)
        pwms[pin] = pwm

    # Function to set servo angle
    def set_angle(pwm, angle):
        if angle < 0 or angle > 180:
            print("Invalid angle. Angle must be between 0 and 180.")
            return
        duty_cycle = (angle / 18.0) + 2.5
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.3)
        pwm.ChangeDutyCycle(0)

    # Main loop to read keyboard input and set servo angles
    try:
        while True:
            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    keys_pressed.add(event.key)
                elif event.type == pygame.KEYUP:
                    keys_pressed.discard(event.key)

            # Update servo angles based on keyboard input
            for key in keys_pressed:
                if key == pygame.K_1:
                    servo_angles[0] = max(servo_limits[0][0], servo_angles[0] - servo_speed)
                elif key == pygame.K_2:
                    servo_angles[0] = min(servo_limits[0][1], servo_angles[0] + servo_speed)
                if key == pygame.K_3:
                    servo_angles[1] = max(servo_limits[1][0], servo_angles[1] - servo_speed)
                elif key == pygame.K_4:
                    servo_angles[1] = min(servo_limits[1][1], servo_angles[1] + servo_speed)
                if key == pygame.K_5:
                    servo_angles[2] = max(servo_limits[2][0], servo_angles[2] - servo_speed)
                elif key == pygame.K_6:
                    servo_angles[2] = min(servo_limits[2][1], servo_angles[2] + servo_speed)
                if key == pygame.K_7:
                    servo_angles[3] = max(servo_limits[3][0], servo_angles[3] - servo_speed)
                elif key == pygame.K_8:
                    servo_angles[3] = min(servo_limits[3][1], servo_angles[3] + servo_speed)
                if key == pygame.K_9:
                    servo_angles[4] = max(servo_limits[4][0], servo_angles[4] - servo_speed)
                elif key == pygame.K_0:
                    servo_angles[4] = min(servo_limits[4][1], servo_angles[4] + servo_speed)
            
            # Draw visualization of servo angles on Pygame window
            window.fill((255, 255, 255))  # White background
            finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
            for i, angle in enumerate(servo_angles):
                x = (i + 1) * window_size[0] // 6
                y = window_size[1] // 2

                y1 = window_size[1] // 2
                y2 = y1 - angle * 0.5
                length = angle

                # Draw servo arm
                pygame.draw.line(window, (0, 0, 0), (x, y1), (x, y2), 5)


                # Draw servo angle text
                font = pygame.font.Font(None, 30)
                text = font.render(str(angle) + " deg", True, (0, 0, 0))
                text_rect = text.get_rect(center=(x, y + length * 0.5 + 20))
                window.blit(text, text_rect)
            
                # Draw finger name
                finger_font = pygame.font.Font(None, 25)
                finger_text = finger_font.render(finger_names[i], True, (0, 0, 0))
                finger_text_rect = finger_text.get_rect(center=(x, y + length * 0.5 + 50))
                window.blit(finger_text, finger_text_rect)

            # Update Pygame display
            pygame.display.update()

            # Wait for next update
            clock.tick(60)  # Update at 60 FPS


            # Read keyboard input
            angles = [int(angle) for angle in servo_angles]
            
            # Set servo angles
            for pin, angle in zip(servo_pins, angles):
                set_angle(pwms[pin], angle)

    except Exception:
        pass

finally:
    GPIO.cleanup()
