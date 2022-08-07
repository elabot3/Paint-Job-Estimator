# Assignment: Paint Job Estimationwith Functions and Writing to a file
# Date: April 28, 2022
# Author: L
# Purpose: Estimate the cost of a paint job 

#1.Import functions module
from functions import *

#2.Define main function logic
def main():
    
    #Call functions to validate data and receive values for calculations
    fSqFtWall = getFloatInput("Enter wall space in square feet: ", .01)
    fPaintPrice = getFloatInput("Enter paint price per gallon: ", .01)
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ", .01)
    fLaborHrsPerGallon = getFloatInput("How many labor hours per gallon: ", .01)
    fPainterHrRate = getFloatInput("Labor charge per hour: ", .01)
    
    #Assign float value to sales tax and send list of sample state abbreviations as an argument
    fSalesTax = getSalesTax("State job is in: ", ["CT", "MA", "ME", "NH", "RI", "VT"])
    
    #Prompt user's for last name that will concatenate as file name
    sCustomerLastName = input("Customer Last Name: ")
    
    #Call functions to perform calculations
    iGallonsPaint = getGallonsOfPaint(fSqFtWall, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHrsPerGallon, iGallonsPaint)
    fTotalLaborCost = getLaborCost(fLaborHours, fPainterHrRate)
    fTotalPaintCost = getPaintCost(iGallonsPaint, fPaintPrice)
    fTotalTax = getTotalTax(fSalesTax, fTotalLaborCost, fTotalPaintCost)
    fShowCostEstimate = showCostEstimate(fTotalTax, fTotalLaborCost, fTotalPaintCost)
    
    #Output
    sResults = f"""
    Gallons of paint: {iGallonsPaint}
    Hours of Labor: {fLaborHours:.1f}
    Paint charges: ${fTotalPaintCost:,.2f}
    Labor charges: ${fTotalLaborCost:,.2f}
    Tax: {fSalesTax * (fTotalLaborCost + fTotalPaintCost):,.2f}
    Total cost: {fShowCostEstimate:,.2f}
    File: {sCustomerLastName}_paintJobOutput.txt was created.
    """
    print(sResults)
    
    #Write to file
    try:
        hdlOutput = open(f'{sCustomerLastName}_paintJobOutput.txt','w')
        hdlOutput.write(sResults)
        hdlOutput.close()
    except:
        print("Error occurred while saving report.")
     

main()


