#!/usr/bin/env python
# coding=utf-8

import time
import os
import sys
import smtplib
from email.mime.text import MIMEText
#配置文件
    #邮件配置
mailto_list="28297654@qq.com"      #接收邮箱
mail_host='smtp.126.com'  #设置服务器
mail_user='pm2point5work'##    #用户名
mail_pass='pm2.5work'   #口令 
mail_postfix='126.com'  #发件箱的后缀
mail_title="CUACE data is normal"           #发送邮件标题
mail_text="CUACE data is normal"   #发送邮件内容

    #log配置 
logPath='D:/Run/tianhe/script/log/'  #log路径

logName='log.txt'  #log名字

    #第一项配置
# T639文件的存放目录
filePath1='/home/cloud01/T639_36/'		#文件路径
date=[]         #设置时间变量
date.append(time.strftime('%Y-%m-%d',time.localtime(time.time()-24*60*60)))
date.append(time.strftime('%Y-%m-%d',time.localtime(time.time())))
date.append(time.strftime('%Y-%m-%d',time.localtime(time.time()+24*60*60)))
date.append(time.strftime('%Y-%m-%d',time.localtime(time.time()+2*24*60*60)))
date.append(time.strftime('%Y-%m-%d',time.localtime(time.time()+3*24*60*60)))
date.append(time.strftime('%Y-%m-%d',time.localtime(time.time()+4*24*60*60)))
hours='12','18','00','06'       #设置小时变量
fileName1=[]                  #设置文件名数组
fileName1List=[]                  #设置文件名数组

for i in range(0,21):   #生成文件名
  #i=i-1
    if i<2:
      fileName1.append('T639:'+date[0]+'_'+hours[i])
    if i>=2 and i<6:
      j=i%4
      fileName1.append('T639:'+date[1]+'_'+hours[j])
    if i>=6 and i<10:
      j=i%4
      fileName1.append('T639:'+date[2]+'_'+hours[j])
    if i>=10 and i<14:
      j=i%4
      fileName1.append('T639:'+date[3]+'_'+hours[j])
    if i>=14 and i<18:
      j=i%4
      fileName1.append('T639:'+date[4]+'_'+hours[j])
    if i>=18 and i<21:
      j=i%4
      fileName1.append('T639:'+date[5]+'_'+hours[j])

for i in range(0,21):   #生成文件
  fileName1List.append([fileName1[i],110311480])
print len(fileName1List)


#    #第二项配置
#filePath2='/vol6/home/cloud03/CUACE_HB/RUN_CUACE/'      #文件路径
#programName='/vol6/home/cloud03/CUACE_HB/RUN_CUACE/prerun.csh'               #调用其他程序的程序名
#
#
#fileName2=[['BDYOUT_DOMAIN1',91919460],['LOWBDY_DOMAIN1',10750256 ],['MMINPUT_DOMAIN1',772246628 ]]	#文件名和大小[filename,size]
#fileHeight2=3			#文件二维数组行数
#sleepTime=100    #文件检测超时
#
#    #第三项配置
#filePath3='/vol6/home/cloud03/CUACE_HB/RUN_CUACE/'	#文件路径
#programName3='/vol6/home/cloud03/CUACE_HB/RUN_CUACE/sub.sh'	#调用其他程序的程序名
#fileName3=[['MMOUT_DOMAIN1',6773952688 ],['CUACEOUT1',73195540704 ]]	#文件名和大小[filename,size]
#fileHeight3=2	#文件二维数组行数

    #第四项配置
filePath4='D:/Run/tianhe/data/' 	#数据文件路径
dailyFile = 'CUACE_09km_daily_' + date[1] + '.nc'
hourlyFile = 'CUACE_09km_hourly_' + date[1] + '.nc'
fileName4=[[dailyFile,1154640],[hourlyFile,32527872]]	#数据文件文件名和大小[filename,size]
fileHeight4=2	#数据文件二维数组行数
programName4='/vol6/home/cloud03/CUACE_HB/POST_CUACE_9km/postrun_n.csh'	#调用其他程序的程序名
datenodash = date[1][0:4]+date[1][5:7]+date[1][8:10]
filePicturePath4='D:/Run/tianhe/figure/'+datenodash +'/'  #图片文件路径
#filePictureType='8'	#图片类别数量
filePicture='CUACE_09km_AQI_','CUACE_09km_CO_','CUACE_09km_NO2_','CUACE_09km_O3_','CUACE_09km_PM10_','CUACE_09km_PM2.5_','CUACE_09km_SO2_','CUACE_09km_VIS_'#图片类别
filePictureNumber='120' #每个类别图片数量
filePictureSizeLimit=100*1024	#图片最低大小
#测试图片文件
filePictureName4=[]
for i in filePicture:
  for j in range(21,24):
    sj=str(j)
    filePictureName4.append(i+date[0]+'_'+sj+'.png')
  for j in range(0,24):
    if j<10:
      sj=str(j)
      filePictureName4.append(i+date[1]+'_0'+sj+'.png')
      filePictureName4.append(i+date[2]+'_0'+sj+'.png')
      filePictureName4.append(i+date[3]+'_0'+sj+'.png')
      filePictureName4.append(i+date[4]+'_0'+sj+'.png')
    if j >= 10:
      sj=str(j)
      filePictureName4.append(i+date[1]+'_'+sj+'.png')
      filePictureName4.append(i+date[2]+'_'+sj+'.png')
      filePictureName4.append(i+date[3]+'_'+sj+'.png')
      filePictureName4.append(i+date[4]+'_'+sj+'.png')
  for j in range(0,21):
    if j<10:
      sj=str(j)
      filePictureName4.append(i+date[5]+'_0'+sj+'.png')
    if j >= 10:
      sj=str(j)
      filePictureName4.append(i+date[5]+'_'+sj+'.png')
#print len(filePictureName4)
#print filePictureName4

#send_mail(mailto_list,mail_title,mail_text)
#程序失败发送提醒邮件
def send_mail(to_list,sub,content):  
  #me=mail_title+"<"+mail_user+"@"+mail_postfix+">"  
  me=mail_user+"@"+mail_postfix  
  msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
  msg['Subject'] = sub  
  msg['From'] = me  
  #msg['To'] = ";".join(to_list)  
  msg['To'] = to_list
  try:  
    server = smtplib.SMTP()  
    server.connect(mail_host)  
    server.login(mail_user,mail_pass)  
    server.sendmail(me, to_list, msg.as_string())  
    server.close()  
    print 'Email send successful.'
    return True  
  except Exception, e:  
    print str(e)  
    print 'Email send failed.'
    return False

# send_mail(mailto_list,mail_title,mail_text)
# sys.exit(0)	
	
#写入log文件
def logWrite(Path,Name,Str):
  current_date = time.strftime('%Y%m%d',time.localtime(time.time()))
  f=open(Path+current_date+'_up_'+Name,'a')
  current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
  f.write(current_time + ':  ' + Str)
  f.close()

#第一项
def monitorT639() :
  isExist = check_file(filePath1, fileName1List )

  if isExist:
    logStr = ' T639 files all have existed!\n\n'
    logWrite(logPath,logName,logStr)            
    print logStr
    return True
  else:
    return False

#第二项

def monitor_prerun() :
  isExist = check_file(filePath2, fileName2 )
  if isExist:
    logStr= ' prerun 预处理成功!\n\n'
    logWrite(logPath,logName,logStr)
    return True
  else:
    return False

##第三项
def monitor_run_cuace() :
  isExist = check_file(filePath3, fileName3 )
  if isExist:
    logStr= ' CUACE 处理成功!\n\n'
    logWrite(logPath,logName,logStr)
    return True
  else:
    return False

def check_file(filepath, filename ):
  for i in range(0,len(filename)):   #文件检测
    if os.path.isfile(filepath+filename[i][0]): # and 
      if os.path.getsize(os.path.join(filepath,filename[i][0]))==filename[i][1]:
        logStr=filepath+filename[i][0]+' 存在且大小正常\n'
        logWrite(logPath,logName,logStr)
      else: 
        logStr=filepath+filename[i][0]+' 存在但大小不正常\n'
        logWrite(logPath,logName,logStr)
        return False
    else:
      logStr=filepath+filename[i][0]+' 不存在\n'
      logWrite(logPath,logName,logStr)
      return False
    
  return True

#第四项
def monitor_postrun():
  # 检测数据
  isExist = check_file(filePath4, fileName4)
  if isExist:
    logStr= ' POST CUACE netcdf 数据处理成功!\n'
    logWrite(logPath,logName,logStr)
  else:
    return False

  for n in range(0,960):
    if os.path.isfile(filePicturePath4+filePictureName4[n]): 
      logStr=filePicturePath4+filePictureName4[n]+' 存在\n'
      logWrite(logPath,logName,logStr)
    else:
      logStr=filePicturePath4+filePictureName4[n]+' 不存在\n'
      logWrite(logPath,logName,logStr)
      return False

  logStr= ' POST CUACE figure 处理成功!\n'
  logWrite(logPath,logName,logStr)
  logStr= ' POST CUACE all files 处理成功!\n'
  logWrite(logPath,logName,logStr)
  return True

if __name__=='__main__':
  logStr = '\n\n=============='+ date[1] + ' new begin ==================\n'
  logWrite(logPath,logName,logStr)
  
  # 1. 检测T639数据
  # sleepStep = 0
  # while not monitorT639() :
    # sleepStep += 1
    # if sleepStep > 20: # 超过1 小时，还没数据，则当天任务失败。
        # logStr= date[1] + ' T639数据没有到,任务退出！\n'
        # print logStr
        # logWrite(logPath,logName,logStr)
    	# sys.exit(0)
    # print ' monitoring T639, sleep 180 seconds'
    # time.sleep(180)
  # #启动上传程序
  # uploadcmd = '/home/cloud01/run/script/pre_upload.sh'
  # logStr=uploadcmd +' 开始上传T639数据！\n'
  # print logStr
  # logWrite(logPath,logName,logStr)
  # os.system(uploadcmd)
# #  print '/home/cloud01/run/script/pre_upload.sh > pre_upload.log'
  # logStr=uploadcmd +' 上传T639数据完毕！\n'
  # print logStr
  # logWrite(logPath,logName,logStr)
  # mail_text = ' T639 data is upload over!'

  #send_mail(mailto_list,mail_title,mail_text)


#  # 2. 启动预处理，检测预处理结果
#  #isOver=os.popen(programName)  #调用其他程序
#  #print isOver.read()
##  os.system(programName)
#  print programName
#  logStr=programName+'调用成功！\n'
#  print logStr
#  logWrite(logPath,logName,logStr)
#
#  while not monitor_prerun():
#    print 'monitoring prerun, sleep 3 seconds'
#    time.sleep(3)
#
#  # 3. 启动CUACE,检测CUACE的输出
#  #isOver=os.popen(programName3)  #调用其他程序
#  #print isOver.read()
##  os.system(programName3)
#  print programName3
#  logStr=programName3+'调用成功！\n'
#  print logStr
#  logWrite(logPath,logName,logStr)
#
#  while not monitor_run_cuace():
#    print 'monitoring RUN CUACE, sleep 3 seconds'
#    time.sleep(60)

  # 4. 启动后处理，检测数据和图片产品
  #isOver=os.popen(filePath4+programName4)  #调用其他程序
  #print isOver.read()
  #os.system(programName4)
  #print programName4
  #logStr=programName4+'调用成功！\n'
  #print logStr
  #logWrite(logPath,logName,logStr)

  #while not monitor_postrun():
  #  print 'monitoring POST CUACE, sleep 3 seconds'
  #  time.sleep(3)

  #logStr=date[1] +' CUACE 数据处理全部成功！\n'
  #print logStr
  #logWrite(logPath,logName,logStr)

  sleepStep = 0
  postdowncmd =  'D:/Run/tianhe/script/post_upload_langfang_1.bat'
  os.system(postdowncmd)
  while not monitor_postrun():
    sleepStep += 1
    if sleepStep > 720: # 超过3 小时，还没数据，则当天任务失败。
        logStr= ' CUACE data and figure 数据没有到,上传失败！\n'
        print logStr
        logWrite(logPath,logName,logStr)
    	sys.exit(0)
	os.system(postdowncmd)
    logStr = ' CUACE 数据 not complete, sleep(10)！\n'
    print logStr
    logWrite(logPath,logName,logStr)
    time.sleep(15)



  os.system(postdowncmd)
  logStr=postdowncmd+' CUACE data and figures  upload to langfang successful！\n'
  print logStr
  logWrite(logPath,logName,logStr)
    


  mail_text="CUACE data and figures have uploaded to langfang!"   #发送邮件内容
  send_mail(mailto_list,mail_title,mail_text)
  

