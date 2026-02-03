# P.P.B.T

This project is a low-power smart keychain that combines E-paper display technology with NFC, designed to work with minimal energy and remain readable even when completely unpowered.

The system is split into two separate modules:

-E-Paper + NFC Keychain Board

Waveshare e paper display is used, following the websites recommended parts, using a crystal oscillator for graphics and a tiny flash memory for the images!
Used an NFC tag plugin for the coil for the NFC tag which calculates the impedance of the coil!

Added extra male pins for future endeavours if i want to add things to the board?

-Solar-Powered DC-DC Booster Board (external, detachable)

Follows a old schematic for an IKEA outdoor light, repurposed with smaller parts to make it cheaper, it uses a buckboost converter to get a steady flow from the solar panel to safely charge or power anything, in my case a strip of leds i will stick on the board case!




**This separation keeps the keychain compact, efficient, and flexible.**


**E PAPER + NFC SCHEMATIC/BOARD/MODEL:**

<img width="1075" height="754" alt="image" src="https://github.com/user-attachments/assets/d3f21696-e099-4127-910e-514173eb5b1a" />


<img width="280" height="365" alt="image" src="https://github.com/user-attachments/assets/e14806a4-8123-4aff-8ddf-b7a097bd6aca" />

<img width="339" height="421" alt="image" src="https://github.com/user-attachments/assets/86a33e55-9fcc-4a89-ac2c-c5cb551560d4" />

** SOLAR POWERED PSU **

<img width="596" height="292" alt="image" src="https://github.com/user-attachments/assets/eba5c8aa-4ed8-4fe6-8c30-15a2a5da5c18" />

<img width="671" height="287" alt="image" src="https://github.com/user-attachments/assets/cdb8fd3e-9793-44c7-ac19-97b17093db4b" />

<img width="683" height="260" alt="image" src="https://github.com/user-attachments/assets/db37bce8-7957-47a5-bb57-88cbbeace659" />


The e-paper display shows text or graphics and keeps the image with zero power. Power is only needed when the display updates.
The NFC works passively, powered by the reader, allowing phones to scan the keychain even if the battery is empty.

To keep the main board simple and efficient, LED lighting is powered by a separate solar-powered DC-DC booster board. This board takes energy from a small solar panel and boosts it to drive LEDs around the keychain, without affecting the e-paper or NFC system.


CASE:

Pretty happy with the colour scheme and how it looks!

<img width="984" height="546" alt="image" src="https://github.com/user-attachments/assets/e0ce6333-20e1-468c-a974-e7c7a433927e" />

<img width="1291" height="783" alt="image" src="https://github.com/user-attachments/assets/25e6d684-cd3b-4073-aca5-eed5747e03a0" />


Main points of note:
PLA (probably)
Added tolerances for easy fitting since im hoping to use a friciton for the lid and the bottom
Added heat set insert holes
Added male header pin space for added functionality in the future
Added solar powered pcb on the underside, that will be wired to external solar panel and a led strip stuck onto the board
Added keychain hole onto the board (for coolness)

Underside:
<img width="960" height="645" alt="image" src="https://github.com/user-attachments/assets/40941c9f-d7b9-4664-8a05-c21590a920ab" />

Solar powered pcb on underside:

<img width="864" height="490" alt="image" src="https://github.com/user-attachments/assets/567f888f-54f9-46d8-b070-8b3411d12dd7" />


Under the hood:

<img width="864" height="490" alt="image" src="https://github.com/user-attachments/assets/1e87a496-569d-44a4-aee7-4fd299e75aa4" />
<img width="963" height="613" alt="image" src="https://github.com/user-attachments/assets/8e6c894d-5aee-413e-a657-5dec6d1d86f4" />


Hopefully this is good enough to protect the board!




