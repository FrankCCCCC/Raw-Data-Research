import matplotlib.pyplot as plt
import numpy as np
import pylab
import json
import os

list = ['Indomaret', 'Tokens!', 'Tokens', 'Alfamart', 'ESE', 'KFC', 'Besar', 'LYFE', 'LBXC', 'Airdrop', 'Go-pay', 'Heluss', 'Draw', 'GoFind', 'JBL', 'GO', 'Speaker', 'T-Shirt', 'Redmi', 'Xiaomi', 'VEX', 'Floweradvisor', 'Pegipegi.com', 'Bottle', 'Adidas', 'Fossil', 'T-Shirts', 'LED', 'Vex', 'Tokenomy', 'Powerbank', 'Mech', 'Backpack', 'Delonghi', 'ECP', 'Coffee', 'Samsung', 'Maker', 'TV', 'Lock&Lock', 'Eco', 'ROBOT', 'RT150', 'Ralali', 'Airy', 'Headphone', 'Flight', 'GO-PAY', 'Philips', 'sony', 'MDR-zx110AP', 'YI', 'Camera', 'Straightener', 'HP8302', 'Inul', 'Vizta', 'Excelso', 'Gramedia', 'GOJEK', 'Roadbike', 'Mouse', 'Steelseries', ] 

def getUserCurrentVP(): # user_vp_from_highest.json
    fileName = "user_vp_from_highest.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listUserVP = json.load(fp)
    
    fp.close()

    return listUserVP

def getUserPremium(): # user_premium_vex_v2.json
    fileName = "user_premium_vex_v2.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listUserPre = json.load(fp)
    
    fp.close()

    return listUserPre

def getUserPremiumKYC(): # user_vp_premium_kyc_all.json
    fileName = "user_vp_premium_kyc_all.json"

    absPath = os.path.abspath(__file__)
    folder = os.path.dirname(absPath)
    filePath = folder + "\\" + fileName

    with open(filePath,encoding='utf-8',errors='ignore') as fp:
        listUserPreKYC = json.load(fp)
    
    fp.close()

    return listUserPreKYC

def getUser():
    listPre = getUserPremium()
    listKYC = getUserPremiumKYC()
    dict = {}
    for e in listPre:
        dict[e['id']] = {
            "name": e['name'],
            "vex_point": e['vex_point'],
            "premium_until": e['premium_until'],
            "premium_duration": e['premium_duration'],
            "vex_token": e['vex_token']
        }

    for k in listKYC:
        dict[k['id']]['created_at'] = k['created_at']
        dict[k['id']]['status'] = k['status']

    listKYC.clear()
    listPre.clear()

    print(dict)

    return dict

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

def analyzeUserBuyVoucher(dictUser, listVoucherRawData, listVoucherAll, showPlot, savePlot):
    return 

def priceVSSalsRate(listPrice, listSalesRate, showPlot, savePlot):
    correlationPriceSalesRate = round(np.corrcoef(listPrice, listSalesRate)[1,0], 5)

    if showPlot or savePlot:
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
        if savePlot:
            plt.savefig("Voucher Price V.S Sales Rate.png")
        if showPlot:
            plt.show()

    plt.clf()

    return correlationPriceSalesRate

def validPeriodVSSalesRate(listValidFrom, listvalidUntil, listSalesRate, showPlot, savePlot):
    l = len(listValidFrom)
    listDate = []
    for i in range(0, l):
        listDate.append((listvalidUntil[i] - listValidFrom[i]) / 86400)

    correlationValidPeriodSalesRate = round(np.corrcoef(listDate, listSalesRate)[1,0], 5)

    if savePlot or showPlot:
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

        if savePlot:
            plt.savefig("Voucher Valid Period V.S Sales Rate.png")
        if showPlot:
            plt.show()

    plt.clf()
    
    return correlationValidPeriodSalesRate

def categoryMemberVSSalesRate(listVoucherRawData, showPlot, savePlot):
    listRawCategory = getRawCategoryAll()
    listMemberType = getMemberTypeAll()
    lenListRawCategory = len(listRawCategory)
    lenListMemberType = len(listMemberType)
    
    nameList = []
    # Sales Volume
    targetsMtx = np.zeros((lenListMemberType + 1, lenListRawCategory))
    baseMtx = np.zeros((lenListMemberType + 1, lenListRawCategory))
    salesRateMtx = np.zeros((lenListMemberType + 1, lenListRawCategory))

    # Sales Amount
    targetsMtx_A = np.zeros((lenListMemberType + 1, lenListRawCategory))
    baseMtx_A = np.zeros((lenListMemberType + 1, lenListRawCategory))
    salesRateMtx_A = np.zeros((lenListMemberType + 1, lenListRawCategory))
    
    for type in listRawCategory:
        nameList.append(type['name'])

    # row 0: All-id: 1
    # row 1: Premium-id: 2
    # row 2: Non Premium-id: 3
    # row 3: Combine All
    for ele in listVoucherRawData:
        c = ele['category_id'] - 1
        r = ele['member_type_id'] - 1

        qLeft = ele['quantity_left']
        qAvailable = ele['quantity_available']
        price = ele['price']

        # Sales Volume
        baseMtx[r][c] = baseMtx[r][c] + qLeft
        targetsMtx[r][c] = targetsMtx[r][c] + qAvailable

        baseMtx[3][c] = baseMtx[3][c] + qLeft
        targetsMtx[3][c] = targetsMtx[3][c] + qAvailable

        # Sales Amount
        baseMtx_A[r][c] = baseMtx_A[r][c] + qLeft * price
        targetsMtx_A[r][c] = targetsMtx_A[r][c] + qAvailable * price

        baseMtx_A[3][c] = baseMtx_A[3][c] + qLeft * price
        targetsMtx_A[3][c] = targetsMtx_A[3][c] + qAvailable * price
        
    
    cols = len(baseMtx[1,:])
    rows = len(baseMtx[:,1])
    print(rows, " : ", cols)
    for r in range(rows):
        for c in range(cols):
            if baseMtx[r-1][c-1] == 0:
                baseMtx[r-1][c-1] = 1
            if baseMtx_A[r-1][c-1] == 0:
                baseMtx_A[r-1][c-1] = 1

            salesRateMtx[r-1][c-1] = (baseMtx[r-1][c-1] - targetsMtx[r-1][c-1]) / baseMtx[r-1][c-1] * 100
            salesRateMtx_A[r-1][c-1] = (baseMtx_A[r-1][c-1] - targetsMtx_A[r-1][c-1]) / baseMtx_A[r-1][c-1] * 100

    if showPlot or savePlot:
        baseArray = range(len(listRawCategory))
        baseArray = [x+1 for x in baseArray]
        plt.title("Sales Volume Rate V.S Voucher Catergory and member type")
        plt.ylabel("Voucher Catergory")
        plt.xlabel("Sales Rate (%)")
        # Add Major grid
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        # Add Minor grid
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        plt.grid(True)
        barHeight = 0.3
        plt.barh(baseArray, salesRateMtx[0,:], height=barHeight, tick_label = nameList, color = "blue", label="All", alpha=0.8)
        plt.barh([x+barHeight for x in baseArray], salesRateMtx[1,:], height=barHeight, color = "red", label="Premium", alpha=0.8)
        # plt.barh([x+barHeight*2 for x in baseArray], salesRateMtx[2,:], height=barHeight, color = "yellow", label="Non Premium", alpha=0.8)
        plt.barh([x+barHeight*2 for x in baseArray], salesRateMtx[3,:], height=barHeight, color = "green", label="Combine", alpha=0.8)
        plt.legend()
        if savePlot:
            plt.savefig("Sales Volume Rate V.S Voucher Catergory and member type.png")
        if showPlot:
            plt.show()

        plt.clf()

        plt.title("Sales Amount V.S Voucher Catergory and member type")
        plt.ylabel("Voucher Catergory")
        plt.xlabel("Sales Amount (IDR)")
        # Add Major grid
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        # Add Minor grid
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        plt.grid(True)
        barHeight = 0.3
        plt.barh(baseArray, targetsMtx_A[0,:], height=barHeight, tick_label = nameList, color = "blue", label="All", alpha=0.8)
        plt.barh([x+barHeight for x in baseArray], targetsMtx_A[1,:], height=barHeight, color = "red", label="Premium", alpha=0.8)
        # plt.barh([x+barHeight*2 for x in baseArray], salesRateMtx[2,:], height=barHeight, color = "yellow", label="Non Premium", alpha=0.8)
        plt.barh([x+barHeight*2 for x in baseArray], targetsMtx_A[3,:], height=barHeight, color = "green", label="Combine", alpha=0.8)
        plt.legend()
        if savePlot:
            plt.savefig("Sales Amount V.S Voucher Catergory and member type.png")
        if showPlot:
            plt.show()

        plt.title("Sales Amount Rate V.S Voucher Catergory and member type")
        plt.ylabel("Voucher Catergory")
        plt.xlabel("Sales Amount Rate (%)")
        # Add Major grid
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        # Add Minor grid
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        plt.grid(True)
        barHeight = 0.3
        plt.barh(baseArray, salesRateMtx_A[0,:], height=barHeight, tick_label = nameList, color = "blue", label="All", alpha=0.8)
        plt.barh([x+barHeight for x in baseArray], salesRateMtx_A[1,:], height=barHeight, color = "red", label="Premium", alpha=0.8)
        # plt.barh([x+barHeight*2 for x in baseArray], salesRateMtx[2,:], height=barHeight, color = "yellow", label="Non Premium", alpha=0.8)
        plt.barh([x+barHeight*2 for x in baseArray], salesRateMtx_A[3,:], height=barHeight, color = "green", label="Combine", alpha=0.8)
        plt.legend()
        if savePlot:
            plt.savefig("Sales Amount Rate V.S Voucher Catergory and member type.png")
        if showPlot:
            plt.show()
    
    plt.clf()

    # return np.concatenate(salesRateMtx, salesRateMtx_A)

def voucherNameVSSalesRate(listVoucherRawData, showPlot, savePlot):
    
    dict = {}
    for e in listVoucherRawData:
        arr = str(e['name']).split()
        quantityTotal = e['quantity_left']
        quantityRemain = e['quantity_available']
        price = e['price']
        for s in arr:
            value = dict.get(s)
            if value == None:
                dict[s] = [quantityTotal * price, quantityRemain * price]
            else:
                dict[s][0] = dict[s][0] + quantityTotal * price
                dict[s][1] = dict[s][1] + quantityRemain * price

    
    listNameSalesAmountRate = []
    listNameSalesAmount = []
    for key in dict:
        if dict[key][0] == 0:
            dict[key][0] = 1
        listNameSalesAmountRate.append((key, dict[key][0] - dict[key][1], (dict[key][0] - dict[key][1]) / dict[key][0] * 100))
        listNameSalesAmount.append((key, dict[key][0] - dict[key][1]))

    print("------------------------------------------------------------------------")
    # print(listNameVolumeSalesRate)
    print("------------------------------------------------------------------------")
    # print(listNameSalesVolume)
    print("------------------------------------------------------------------------")
    # print(dict.keys())

    
    fGetVolume = lambda x: x[1]
    fGetSalesRate = lambda x: x[2]
    listNameSalesAmount.sort(key=fGetVolume, reverse=True)
    listNameSalesAmountRate.sort(key=fGetSalesRate, reverse=True)
    print(listNameSalesAmount)
    print("------------------------------------------------------------------------")
    print(listNameSalesAmountRate)

def analyzeVoucherPriceDateLeft():
    listVoucherRawData = getVoucherRawData()
    # print(listVoucherRawData)

    listPrice = []
    listDate = []
    listSalesRate = []
    listValidFrom = []
    listValidUntil = []
    listName = []
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
        name = ele['name']

        if quantityTotal == 0:
            quantityTotal = -1

        # if quantityTotal < 10:
        #     price = 0
        #     quantityRemain = 0
        #     quantityTotal = 1

        listName.append(name)
        listPrice.append(price) # Price
        listValidFrom.append(validFrom)
        listValidUntil.append(validUntil)
        listDate.append((validUntil - validFrom) / 86400) # Sec -> Days Valid Period
        listSalesRate.append((quantityTotal - quantityRemain) / quantityTotal *100) # Sales Rate

    # Price V.S Sales Rate
    # correlationPriceSalesRate = priceVSSalsRate(listPrice, listSalesRate, False, False)

    # Valid Period V.S Sales Rate
    # correlationValidPeriodSalesRate = validPeriodVSSalesRate(listValidFrom, listValidUntil, listSalesRate, False, False)

    # Voucher Category v.s Sales Rate
    # categoryMemberVSSalesRate(listVoucherRawData, True, True)

    # Voucher Name v.s Sales Rate
    # voucherNameVSSalesRate(listVoucherRawData, False, False)

    # Voucher type v.s Sales Rate

    # Payment Type v.s Sales Rate

    # Redeem Type v.s Sales Rate

    # 
    dictUser = getUser()
    listVoucherAll = getVoucherAll()
    analyzeUserBuyVoucher(dictUser, listVoucherRawData, listVoucherAll, True, True)

# plotVPandUserAmount()
analyzeVoucherPriceDateLeft()
