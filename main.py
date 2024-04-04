import time
import sys
import random
import tqdm
from math import ceil
from decimal import Decimal
from decimal import getcontext
Pt={"win32":"\\","linux":"/"}
X=Pt.get(sys.platform,"linux")
self_defaultHeader="[{time} {session}] {things}{endv}"
RandomList="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.@~-,:*?!_#/=+&^;%$()<>[]{}'`´\""
class printlog():
    def __init__(self):
        global self_defaultHeader
        self.path=sys.path[0] + X + ".cache" + X + "cache.log"
        self.logFile=open(self.path,"a+")
        self.SessionId=''.join(random.choices(RandomList, k=16))
    def log(self,word,header=self_defaultHeader,endv="\n"):
        self.logFile.write(header.format(time=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),session=self.SessionId,things=word,endv=endv))
    def delog(self,ycontinue):
        if ycontinue!="y":
            print("class:printlog.delog异常，请发送日志到lotustwos@gmail.com，此提示不影响程序运行，仅为删除日志失败的提示。")
            return
        os.remove(self.path)
FLog=printlog()
def floatPatch(num):
    return Decimal(str(num))
def creatfilesize(n, data_type,SegmentedTrillion,SizeOfEachFile):
    '''
    主函数
    :param n: 需要生成的文件大小(单位:GB)
    :param data_type: 需要生成的文件格式(例:.mp4)
    :return:
    '''
    FLog.log("input:{0},{1},{2},{3}".format(n, data_type,SegmentedTrillion,SizeOfEachFile))
    print()
    global RandomList
    RandomList = "".join(random.sample(RandomList, len(RandomList)))
    print("randomList: ",RandomList)
    FLog.log("random List:{0}".format(RandomList))
    FileExtraSize=0.0
    fileSuffix=""
    SizeOfEachFile=float(SizeOfEachFile)
    FLog.log("SizeOfEachFile:{0}".format(SizeOfEachFile))
    if float(str(float(SizeOfEachFile)).split(".")[1])!=0.0:
        print("文件大小仅能为整数")
        sys.exit(0)
    rangeNum=float(float(n)/SizeOfEachFile)#被分成的文件数
    FLog.log("rangeNum:".format(rangeNum))
    if rangeNum<=1.0:
        FLog.log("#001if:0")
        fileSize=float(n)
        rangeNum=range(1)
        rangeNumN=float(1)
        FLog.log("fileSize,rangeNum,rangeNumN:{0},{1},{2}".format(fileSize,rangeNum,rangeNumN))
    elif rangeNum<=30.0:
        FLog.log("#001if:1")
        rangeNum=range(ceil(rangeNum))
        fileSize=SizeOfEachFile
        rangeNumN=float(float(n)/SizeOfEachFile)
        FLog.log("fileSize,rangeNum,rangeNumN:{0},{1},{2}".format(fileSize,rangeNum,rangeNumN))
        FileExtraSize=float(floatPatch(n)-floatPatch(int(SizeOfEachFile)*(ceil(rangeNumN)-1)))
        FLog.log("FileExtraSize:{0}".format(FileExtraSize))
    else:
        print("The file is too big, please generate the file several times.")
        sys.exit(0)
    local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print("\r\033[s\033[1A")
    SegmentedTrillion=SegmentedTrillion
    for fileNum in rangeNum: #每个文件
        FLog.log("#002for: fileNum:{0} ,rangeNum:{1}".format(fileNum,rangeNum))
        print("\r\033[uNew File:{0}/{1}".format(fileNum+1,ceil(rangeNumN)))
        FLog.log("\033[31m\033[1mNew File:{0}/{1}\033[0m".format(fileNum+1,ceil(rangeNumN)))
        if rangeNumN!=1:
            fileSuffix="_{0}".format(fileNum+1)
        if ceil(rangeNumN)-fileNum==1 and FileExtraSize!=0.0:
            fileSize=FileExtraSize
        FLog.log("fileSize:{0}".format(fileSize))
        # 默认在.cache根目录下生成以当前时间命名的文件
        file_name = sys.path[0] + X + ".cache" + X + str(local_time) + fileSuffix + data_type
        segmentationExtraSize=0.0
        segmentationSize=SegmentedTrillion/1024
        FLog.log("segmentationSize:{0}".format(segmentationSize))
        if fileSize<=SegmentedTrillion:
            segmentationNum=1
            segmentationSize=fileSize
            FLog.log("#003if:0")
            FLog.log("segmentationNum:{0}".format(segmentationNum))
        else:
            FLog.log("#003if:1")
            segmentationNum=ceil(fileSize/SegmentedTrillion)
            FLog.log("segmentationNum:{0} ,d:{1} ,ceil:{2}0,fileSize:{3} ,SegmentedTrillion:{4}".format(segmentationNum,fileSize/SegmentedTrillion,ceil(fileSize/(SegmentedTrillion)),fileSize,SegmentedTrillion))
            segmentationExtraSize=float(fileSize)-float(int(SegmentedTrillion)*(segmentationNum-1))
            FLog.log("segmentationExtraSize:{0}".format(segmentationExtraSize))
            if segmentationExtraSize==float(fileSize):
                FLog.log("#004if:Ture")
                segmentationExtraSize=0.0
                FLog.log("segmentationExtraSize:{0}".format(segmentationExtraSize))
        #dataList=[]
        bigFile = open(file_name, 'w')
        #FLog.log("dataList:{0}".format(dataList))  
        FLog.log("file opened,file name:{0}".format(file_name))
        for segmentationNumIn in range(segmentationNum):
            FLog.log("#005for s egmentationNumIn:{0} segmentationNum:{1}".format(segmentationNumIn,segmentationNum))
            #print("\033[4A")
            print("\r\033[u\n\n                   \rNew segmentation:{0}/{1}".format(str(segmentationNumIn+1),str(segmentationNum)))
            FLog.log("New segmentation:{0}/{1}".format(str(segmentationNumIn+1),str(segmentationNum)))
            if segmentationNum-segmentationNumIn==1 and segmentationExtraSize != 0.0:
                FLog.log("#006if Ture")
                segmentationSize=segmentationExtraSize/1024.0
                FLog.log("segmentationSize:{0}".format(segmentationSize))
            data1_4=sc(segmentationSize, RandomList)
            FLog.log("dataGet,sc(segmentationSize:{0}, RandomList)".format(segmentationSize))
            #data=sc(fileSize, data_type,SegmentedTrillion)
            bigFile.write(data1_4)
            FLog.log("write the data1_4")
        bigFile.close()
        FLog.log("file closed")
    print("ALL down !\nSave at ./.cache/")
    FLog.log("ALL down ! Save at ./.cache/\n\n\n")
    if input("你想要删除日志吗?(y/其他) ") == "y":
        FLog.delog("y")
        print("删除成功")

def sc(n, RandomList):
    FLog.log("join f:sc(n:{0})".format(n))
    if len(str(float(n)).split(".")[1])>5:
        FLog.log("#007if Ture")
        n=float("".join((str(float(n)).split(".")[0],".",str(float(n)).split(".")[1][0:5])))
        FLog.log("n:{0}".format(n))
    byteNum=int(1024 * 1024 * 1024 * n)
    FLog.log("byteNum:{0}".format(byteNum))
    RandomNum1_=128
    RandomByteNum=int(byteNum/RandomNum1_) #单位byte
    FLog.log("RandomByteNum:{0}".format(RandomByteNum))
    ByteArr=[]
    FLog.log("new ByteArr")
    rangeClassByte1_=tqdm.tqdm(range(RandomNum1_),bar_format="{desc}{percentage:3.0f}%|{bar}|",position=0)
    FLog.log("rangeClassByte1_:range{0},d:{1}".format(RandomNum1_,rangeClassByte1_))
    for byteNumIn in rangeClassByte1_:
        # print("Generating random characters...")
        # for cache in tqdm.tqdm(range(int((int(n)*1024)/SegmentedTrillion))):
        #print("\r\033[u\033[4BNew Byte:{0}/{1}".format(str(byteNumIn),str(128)))
        if byteNumIn==0:
            FLog.log("#008for byteNumIn:{0} rangeClassByte1_128:{1}".format(byteNumIn,rangeClassByte1_))
            FLog.log("ByteArr1_4 generated")
            FLog.log("ByteArr.appended(ByteArr1_4)")
            FLog.log("New Byte:(共{All}),当前{Now},".format(Now=str(byteNumIn),All=str(128)),endv="")
        if (byteNumIn+1)%(int(RandomNum1_/8))==0:
            FLog.log("".join((str(byteNumIn),",")),"","")
        #else:
            #FLog.log("#009if False ,d:{0}".format((byteNumIn+1)%(int(RandomNum1_/8))))
        rangeClassByte1_.set_description("\033[u\033[4BNew Byte:{0}/{1}".format(str(byteNumIn),str(128)))
        ByteArr1_4=""
        ByteArr1_4 = ''.join(random.choices(RandomList, k=RandomByteNum))
        ByteArr.append(ByteArr1_4)
    ByteData="".join(ByteArr)
    FLog.log("","")
    rangeClassByte1_.close()
    FLog.log("ByteData=''.join(ByteArr)")
    FLog.log("f:sc exit")
    return ByteData
#bigFile.write
if __name__ == '__main__':
    n = input("请输入需要生成的文件大小(单位:GB):")
    data_type = input("请输入需要生成的文件格式(例:.mp4):")
    SizeOfEachFile=input("每个文件大小(建议2,只支持整数)，单位GB: ")
    SegmentedTrillion=input("几兆分段(建议128,不能超过1024,大了卡死), 单位MB:")
    creatfilesize(float(n), data_type,int(SegmentedTrillion),SizeOfEachFile)