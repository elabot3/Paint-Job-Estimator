#This is a module that defines the functions that will be used in the paint job estimator. 

#Import math module for math.ceil function
import math

#Create function to validate data
def getFloatInput(sPrompt, fMinNumberAllowed):

    #Default fValue to -1 to enter loop:
    fValue = -1

    while fValue < fMinNumberAllowed:
        try:
            fValue = float(input(sPrompt))
            if fValue <  fMinNumberAllowed:
                print ("Input must be a numeric value greater or equal to:", fMinNumberAllowed)
                continue
            
        except ValueError:
                print ("Input must be a numeric value greater or equal to:", fMinNumberAllowed)
                continue
            
    return fValue

#Define functions for calculations
def getGallonsOfPaint(iSqFtWall, iFeetPerGallon):
     return math.ceil(iSqFtWall / iFeetPerGallon)
    
def getLaborHours(fHoursPerGallon, fTotalGallons):
    return fHoursPerGallon * fTotalGallons

def getLaborCost(fTotalLaborHours, fPaintingLaborChargePerHour):
    return float(fTotalLaborHours * fPaintingLaborChargePerHour)

def getPaintCost(fTotalGallons, fPaintPrice):
    return float(fTotalGallons * fPaintPrice)

#I played around with lists and dictionaries in this section of the code to assign a float value
#to the input state abbreviation. I could not figure out to how to make the code more elegant, so
#I focused on getting the right float value returned for calculations. I also wanted to showcase
#my ability to execute a list as a parameter. I'd love your feedback on how to
#make this more efficient and validate the data so that only state abbreviations can be accepted as input.
def getSalesTax(sStatePrompt, sStatelist):
        fTaxValue = input(sStatePrompt).upper()
        if fTaxValue in sStatelist:
            fState = {
            "CT": .06,
            "MA": .0625,
            "ME": .085,
            "NH": .0,
            "RI": .07,
            "VT": .06
            }
            return fState[fTaxValue]
        else:
            fTaxValue = 0.0
            return fTaxValue 
            
def getTotalTax(fSalesTaxTotal, fLaborTotalCost, fPaintTotalCost):
    return fSalesTaxTotal * (fLaborTotalCost + fPaintTotalCost)
    
def showCostEstimate(fTotalTax,fTotalLabor, fTotalPaint):
    return fTotalTax + fTotalLabor + fTotalPaint


    

