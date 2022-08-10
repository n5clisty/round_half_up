# round_half_up
This code conducts round half up for a given float value.

I found sometimes just a simple code called "round(value)" in python doesn't return the value you expected. For example, if I round up a value 0.355 using "round(0.355, 2)", it gives me 0.35, which it should be 0.36 and that is the way how round half up works as we learned from school, right?

So, I made this code to do "the usual school rounding".
This code will give you 0.36 when you do the round half up 0.355, not 0.35.
