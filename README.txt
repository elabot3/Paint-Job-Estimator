Paint Job with Functions and Output Files

You will be coding Chapter 5 Programming Exercise 8 Paint Job Estimator.  Refer to the book and review the requirements but Prof. Candido will add some additional requirements so make sure you read the entire assignment.  

1. In this assignment you will be asking for input for these float variables: 
Square Feet of the Wall
Paint Price
Feet per Gallon of Paint
Labor Hours per Gallon
Painting Labor charge per hour

2. Code a function called getFloatInput that receives a string as a parameter to be used as the prompt input text and it returns a float. You will be calling this function for 5 times for each of the variables listed above and assign the function’s return value and assign to each of the listed variables. For example: 
 fPaintPrice = getFloatInput(“Enter Paint Price”)

Perform data validation within the function on the inputted value using Python error handling which can be found in Blackboard.  Use Python’s loops to accomplish the sub-tasks below:
If the contents are not numeric issue a message and prompt them again until the user enters a valid number for each of the input variables.  
Make sure the inputted value are non-zero and positive values or issue an error message and ask for input again.  
Return a valid non-zero float

3. Prompt the user for the state of the job will take place in and store it in a variable. 

4. Prompt the user for the customer’s last name and store it in a variable.

5. Refer to the book for details on the calculations.  But do not use global variables nor global constants.  You will use the variables from Step 1. You must place each of assignment’s calculations into their own functions that will return the calculated value.  Do not embed the functions within another function. You will need to code the functions to receive the parameter(s) as detailed below:
main() that will contain the logic for the program
getGallonsOfPaint returns an int of how many gallons are needed for the job rounded up to the next highest gallon. The reason for this you can only buy whole gallons.  Check out the Python Math Module document in Blackboard.  This function should receive Square Feet of the Wall and Feet per Gallon of Paint variables.
getLaborHours returns the Labor Hours to paint the wall as a float. This function should receive Labor Hours per Gallon and the Total Gallons determined in the getGallonsOfPaint function variables.
getLaborCost returns the Labor Cost to paint the wall as a float. . This function should receive Labor Hours per Gallon and the Painting Labor charge per hour variables.
getPaintCost returns the Paint Cost to paint the wall as a float. This function should receive and the Total Gallons determined in the getGallonsOfPaint function and Paint Price variables.
getSalesTax that returns the tax rate for the passed in state variable as follows:
If the state is CT the tax rate is .06
If the state is MA the tax rate is .0625
If the state is ME the tax rate is .085
If the state is NH the tax rate is .0
If the state is RI the tax rate is .07
If the state is VT the tax rate is .06
None of the above tax rate is 0.
showCostEstimate takes in all the calculated values and outputs the values to the screen formatted.  You will need to determine the parameters that need to be passed to this function to accomplish the output. 

You must also add code to print all the same screen output to a file.  This created file will be named by taking the customer’s last name that you prompted and concatenates it with _PaintJobOutput.txt. For example if the customer last name that was entered is Candido then the output file you created would be Candido_PaintJobOutput.txt.  Make sure to print out to the screen a message that the file was created and you must show the file name.  See the sample output. This function returns nothing.
Make sure you use Hungarian Notation when naming the variables.
Make sure to include comments in your code.
