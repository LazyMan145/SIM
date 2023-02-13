import arrow  #pip install arrow

date_now = True

MSKutc = "+03:00"
start_time_label_1 = '2023.02.11 13:00:00'
start_plan_label_1 = '2023.02.11 13:00:01'
end_plan_label_1 = '2023.02.11 13:00:02'
end_time_label_1 = '2023.02.11 13:00:03'

plus1 = start_time_label_1 + MSKutc

plus2 = start_plan_label_1 + MSKutc

plus3 = end_plan_label_1 + MSKutc

plus4 = end_time_label_1 + MSKutc

MSKdateformat1 = 0
MSKdateformat2 = 0
MSKdateformat3 = 0
MSKdateformat4 = 0

rf = [plus1, plus2, plus3, plus4]
rf2 = [MSKdateformat1, MSKdateformat2, MSKdateformat3, MSKdateformat4]

rfs = len(rf)
rfs2 = len(rf2)



for Y in range(rfs):
    if date_now == False:
        if rf[Y] != '':

            qustion = arrow.get(rf[Y])
            local = qustion.to("Europe/Moscow")
            rf2[Y] = local.format('YYYY-MM-DDTHH:mm:ssZZ')

        else:

            utc = arrow.utcnow()

            MSKtimezone = utc.to('Europe/Moscow')
            rf2[Y] = MSKtimezone.format('YYYY-MM-DDTHH:mm:ssZZ')
    else: 
        utc = arrow.utcnow()
        local = utc.to("Europe/Moscow")
        rf2[Y] = local.format('YYYY-MM-DDTHH:mm:ssZZ')

    Y += 1

print (rf2)


