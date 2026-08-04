I ended up having to design a custom power distribution PCB because the Axiometa PCB did not work.

The Altium project files are in this folder, while the 8 Gerber files + drill file are in the gerber_files folder

The board, in a nutshell, pulls 5V @ 3A from an Apple USB-C charger to distribute to 4 servo motors.
It is defined for that power specification, so I would not recommend using anything besides that specific setup.

All the capacitor pairs exist to 1: serve as power reserves and 2: to filter noise, as servos are very spontaneous in their current draw.
100nF ceramics: a standard for high frequency, local filtering
22uF electrolytic calcs (using C = (I × Δt) / ΔV): .3A (stall current for my servos) * 2us (general time transient for current)/ .2 (5 percent of 5V rail) = 24uF
    **I should have used .2 V as the acceptable voltage sag, which stems from the 4.8V minimum operating voltage from the datasheet (yields 30uF)
220uF bulk: I found 10x the local cap's amount is a some kind of general rule, so I did that.

Most of the routing and other design choices are self explanatory by the schematics and pcb file. The GND via far away from everything else is for the pi4b to reference the servo GND to create accurate PWM signals.
