import os
#Contact details:
sellerName  =   "sellerName"
buyerName   =   "buyerName"
sellerEmail =   "sellerEmail"
buyerEmail  =   "buyerEmail"
sellerPhone =   "sellerPhone"
buyerPhone  =   "buyerPhone"
locationName =  "locationName"
itemName = "itemName"
time        =   "time"
price       =   "$8.00"


subject = "\" Got a match! \""

messageToSeller= "\"Hey "+sellerName+"!\n "       \
                +buyerName + " matched with you for " + itemName+ " at "+ locationName + "    \
                  at " + price+".\
                contact your buyer at " + buyerPhone + " or email: " + buyerEmail + ". Thanks!\""


messageToBuyer= "\"Hey "+buyerName+"!\n "       \
                +sellerName + " matched with you for " + itemName+ " at "+ locationName + "    \
                  at " + price+".\
                contact your seller at " + sellerPhone + " or email: " + sellerEmail + ". Thanks!\""


#sending mail is below:

os.system("mail -s "+subject+" "+sellerEmail+" "+messageToSeller)
os.system("mail -s "+subject+" "+buyerEmail+" "+messageToBuyer)
