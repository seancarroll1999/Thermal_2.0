# Thermal_2.0
Welcome to the new and improved Thermal 2.0, a smart thermal printer assistant built on a Raspberry pi.
To see the original version of Thermal follow the link below:
  https://github.com/seancarroll1999/Thermal
  
# What's New
-	Thermal 2.0 will be built on the new Raspberry Pi Zero 2. This capable board is small enough to fit in a single enclosure reducing the bulkiness of the original model.
-	New code, the original thermal was never finished. During development it was clear there was significant design flaws in the software architecture. Thermal 2.0 is a complete re-design of the code base with all the same great features.
-	Complete web app experience. Originally Thermal was used via an android application. This worked well for my own use however to make Thermal 2.0 more versatile, a fully hosted web application can be configured on the pi so any number of devices can connect to Thermal.
-	The original API, the original method of interaction a responsive API is still being supported, so purpose built apps and integration can be developed to incorporate Thermal into current systems or expand on the existing code.
-	Low level library, The thermal printer is connected via the GPIO pins on the PI, I have compiled the best parts of a range of Libraries to make the perfect library for this printer.
