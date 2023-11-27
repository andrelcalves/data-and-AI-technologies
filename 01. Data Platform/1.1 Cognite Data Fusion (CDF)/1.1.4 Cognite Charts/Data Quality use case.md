1.  Create a new chart.
2.  Find and visualize the following time series data: 
    Temperature In: TIT202-21, unit is °C.
    Temperature Out: TIT201-20, unit is °C.
3.  Calculate ∆ Temp using the Subtraction function:
    (Temp In) - (Temp Out) = ∆ Temp, unit is °C.
4.  Calculate Temp In: Gaps detection to check for gaps of 2 minutes or more.
    (Temp In) -> (Gaps detection, threshold) = Temp In: Gaps detection.
    Set the Time Threshold parameter to 2 minutes: 0 days 00:02:00.
5.  Calculate Temp In: Rolling stdev time ∆ to measure the amount of variation or dispersion in the frequency of time series data points.
    (Temp In) -> (Rolling stdev of time delta) = Temp In: Rolling stdev time ∆.
    Use the default function parameters.
6.  Repeat steps 4 and 5 for Temperature Out. 
    You can simply duplicate the Temp In: Gaps detection and Temp In: Rolling stdev time calculations, Rename them and change the Source value.