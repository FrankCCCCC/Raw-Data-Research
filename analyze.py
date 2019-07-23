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
    
    fp.close()

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

    fp.close()
    
    return listVoucherRawData

def getRawCategoryAll(): # raw_category_all.json
    fileName = "raw_category_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listRawCategory = json.load(fp)
    
    fp.close()

    return listRawCategory

def getVoucherCategoryAll(): # rvoucher_type_all.json
    fileName = "rvoucher_type_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listVoucherCategory = json.load(fp)

    fp.close()
    
    return listVoucherCategory

def getMemberTypeAll(): # member_type_all.json
    fileName = "member_type_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listMemberType= json.load(fp)
    
    fp.close()

    return listMemberType

def getVoucherAll(): # voucher_all_and_vouchercode.json
    fileName = "voucher_all_and_vouchercode.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listVoucherAll= json.load(fp)
    
    fp.close()
    
    return listVoucherAll

def getVPLogGain(): # voucher_all_and_vouchercode.json
    fileName1 = "vp_log_gain_1.json"
    fileName2 = "vp_log_gain_2.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath1 = folder + "\\" + fileName1
    filePath2 = folder + "\\" + fileName2

    with open(filePath1,encoding='utf-8',errors='ignore') as fp1:
        listVPLogGain= json.load(fp1)
    with open(filePath2,encoding='utf-8',errors='ignore') as fp2:
        listVPLogGain.append(json.load(fp2))

    fp1.close()
    fp2.close()

    return listVPLogGain

# def analyzeUserBuyVoucher():


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
        # paymentType = ele['payment_type_id']
        # voucherType = ele['voucher_type_id']
        # memberType = ele['member_type_id']
        # redeemType = ele['redeem_type_id']
        # name = ele['name']

        if quantityTotal == 0:
            quantityTotal = -1

        # if quantityTotal < 10:
        #     price = 0
        #     quantityRemain = 0
        #     quantityTotal = 1

        listPrice.append(price) # Price
        listDate.append((validUntil - validFrom) / 86400) # Sec -> Days Valid Period
        listSalesRate.append((quantityTotal - quantityRemain) / quantityTotal *100) # Sales Rate

    # Price V.S Sales Rate
    correlationPriceSalesRate = round(np.corrcoef(listPrice, listSalesRate)[1,0], 5)
    plt.plot(listPrice, listSalesRate, "ro")
    # plt.xscale('log')
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
    listMemberType = getMemberTypeAll()
    lenListRawCategory = len(listRawCategory)
    lenListMemberType = len(listMemberType)
    
    nameList = []
    targetsMtx = np.zeros((lenListMemberType, lenListRawCategory))
    baseMtx = np.zeros((lenListMemberType, lenListRawCategory))
    salesRateMtx = np.zeros((lenListMemberType, lenListRawCategory))
    
    for type in listRawCategory:
        nameList.append(type['name'])

    for ele in listVoucherRawData:
        c = ele['category_id'] - 1
        r = ele['member_type_id'] - 1

        baseMtx[r][c] = baseMtx[r][c] + ele['quantity_left']
        targetsMtx[r][c] = targetsMtx[r][c] + ele['quantity_available']

        if ele['member_type_id'] == 1:
            baseMtx[lenListMemberType][c] = baseMtx[lenListMemberType][c] + ele['quantity_left']
            targetsMtx[lenListMemberType][c] = targetsMtx[lenListMemberType][c] + ele['quantity_available']
        elif ele['member_type_id'] == 2:
            baseMtx[lenListMemberType + 1][c] = baseMtx[lenListMemberType + 1][c] + ele['quantity_left']
            targetsMtx[lenListMemberType + 1][c] = targetsMtx[lenListMemberType + 1][c] + ele['quantity_available']
        
    
    cols = len(baseMtx[1,:])
    rows = len(baseMtx[:,1])
    print(rows, " : ", cols)
    for r in range(rows):
        for c in range(cols):
            if baseMtx[r-1][c-1] == 0:
                baseMtx[r-1][c-1] = 1
            salesRateMtx[r-1][c-1] = targetsMtx[r-1][c-1] / baseMtx[r-1][c-1] * 100

    baseArray = range(len(listRawCategory))
    baseArray = [x+1 for x in baseArray]
    plt.title("Sales Rate V.S Voucher Catergory and member type")
    plt.ylabel("Voucher Catergory")
    plt.xlabel("Sales Rate (%)")
    # Add Major grid
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Add Minor grid
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.grid(True)
    barHeight = 0.4
    plt.barh(baseArray, salesRateMtx[0,:], height=barHeight, tick_label = nameList, color = "blue", label="All", alpha=0.8)
    plt.barh([x+barHeight for x in baseArray], salesRateMtx[1,:], height=barHeight, color = "red", label="Premium", alpha=0.8)
    plt.legend()
    plt.savefig("Sales Rate V.S Voucher Catergory and member type.png")
    plt.show()


    # Voucher type v.s Sales Rate

    # Payment Type v.s Sales Rate

    # Redeem Type v.s Sales Rate

# plotVPandUserAmount()
# analyzeVoucherPriceDateLeft()
