# MagTag_Power_Outage_Counter
Used to track how often the neighborhood power goes down. 

In my neighborhood, the power goes out when the wind blows. Each year there are probably 20 power outages. At least one a month. I wanted to keep track of the number of breaks in power. 

![Alt MagTag showing the number of power outages](magtag.png)

# Materials
- Adafruit MagTag
- Adafruit IO account (username and key)

# Code and use
The main file is code.py and will launch each time the power returns. The code will connect to your wifi and then contact Adafruit IO where it stores the current count. Once it grabs the current count, it adds one and displays the current count. 

You will also need to include secrets.py for everything to work. This is where you keep your wifi information and the Adafruit IO info. 

If you haven't done much with the MagTag or CircuitPython, the idea of using the 'lib' library folder may be a bit new. You will also need to have this folder and include a few extra files. These libraries make using the MagTag 'easier', but they are a little awkward. 

# Why connect to Wifi and grab a variable from Adafruit IO? 
Mainly because I couldn't easily find a way to store or write a value to ram. 
