import matplotlib.pyplot as plt
import numpy as np
import pylab
import json
import os

def getUserCurrentVP(): # user_vp_from_highest.json
    fileName = "user_vp_from_highest.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listUserVP = json.load(fp)
    
    return listUserVP

def plotVPandUserAmount():
    listUserVP = getUserCurrentVP()

    listVP = []
    for ele in listUserVP:
        listVP.append(ele['vex_point'])

    plt.hist(listVP, bins=100)
    plt.title("Users' VP amount V.S User amount")
    plt.xlabel("VP amount")
    plt.ylabel("User amount")
    plt.yscale('log')
    # Add Major grid
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Add Minor grid
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.grid(True)
    plt.savefig("Users' VP amount V.S User amount.png")
    plt.show()


    values, base = np.histogram(listVP, bins=100)
    cumulative = np.cumsum(values)
    plt.plot(base[:-1], cumulative)
    plt.title("Users' VP amount V.S Cumulative User amount")
    plt.xlabel("VP amount")
    plt.ylabel("Cumulative User amount")
    # Add Major grid
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Add Minor grid
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.grid(True)
    plt.savefig("Users' VP amount V.S Cumulative User amount.png")
    plt.show()

def getVoucherRawData(): # raw_voucher_all.json
    fileName = "raw_voucher_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listVoucherRawData = json.load(fp)
    
    return listVoucherRawData

def getRawCategoryAll(): # raw_category_all.json
    fileName = "raw_category_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listRawCategory = json.load(fp)
    
    return listRawCategory

def getVoucherCategoryAll(): # rvoucher_type_all.json
    fileName = "rvoucher_type_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listVoucherCategory = json.load(fp)
    
    return listVoucherCategory

def analyzeVoucherPriceDateLeft():
    listVoucherRawData = getVoucherRawData()
    # print(listVoucherRawData)

    listPrice = []
    listDate = []
    listSalesRate = []
    for ele in listVoucherRawData:
        price = ele['price']
        validUntil = ele['valid_until']
        validFrom = ele['valid_from']
        quantityTotal = ele['quantity_left']
        quantityRemain = ele['quantity_available']
        paymentType = ele['payment_type_id']
        voucherType = ele['voucher_type_id']
        memberType = ele['member_type_id']
        redeemType = ele['redeem_type_id']

        if quantityTotal == 0:
            quantityTotal = -1

        listPrice.append(price) # Price
        listDate.append((validUntil - validFrom) / 86400) # Sec -> Days Valid Period
        listSalesRate.append((quantityTotal - quantityRemain) / quantityTotal *100) # Sales Rate

    # Price V.S Sales Rate
    correlationPriceSalesRate = round(np.corrcoef(listPrice, listSalesRate)[1,0], 5)
    plt.plot(listPrice, listSalesRate, "ro")
    title = "Voucher Price V.S Sales Rate Correlation: " + str(correlationPriceSalesRate)
    plt.title(title)
    plt.xlabel("Voucher Price (VP)")
    plt.ylabel("Sales Rate (%)")
    # Add Major grid
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Add Minor grid
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.grid(True)
    # plt.xscale('log')
    plt.savefig("Voucher Price V.S Sales Rate.png")
    plt.show()
    
    print(correlationPriceSalesRate)

    # Valid Period V.S Sales Rate
    correlationValidPeriodSalesRate = round(np.corrcoef(listDate, listSalesRate)[1,0], 5)
    plt.plot(listDate, listSalesRate, "ro")
    title = "Voucher Valid Period V.S Sales Rate Correlation: " + str(correlationValidPeriodSalesRate)
    plt.title(title)
    plt.xlabel("Voucher Valid Period (Day)")
    plt.ylabel("Sales Rate (%)")
    # Add Major grid
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Add Minor grid
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.grid(True)
    # plt.xscale('log')
    plt.savefig("Voucher Valid Period V.S Sales Rate.png")
    plt.show()
    
    print(correlationValidPeriodSalesRate)

    # Voucher Category v.s Sales Rate
    listRawCategory = getRawCategoryAll()
    types = len(listRawCategory)
    listCategoriesSalesRate = []
    for type in listRawCategory:
        targets = 0
        base = 0
        for ele in listVoucherRawData:
            if ele['category_id'] == type['id']:
                targets = targets + ele['quantity_available']
                base = base + ele['quantity_left']
        if base == 0:
            salesRate = 0
        else:
            salesRate = targets / base
        listCategoriesSalesRate.append(salesRate)
    plt.hist(listCategoriesSalesRate)
    plt.show()


    # Voucher type v.s Sales Rate

    # Member Type v.s Sales Rate

    # Payment Type v.s Sales Rate

    # Redeem Type v.s Sales Rate

# plotVPandUserAmount()
analyzeVoucherPriceDateLeft()