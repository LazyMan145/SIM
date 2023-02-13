import lxml.etree
import os
from datetime import datetime
import random
import arrow  #pip install arrow



# сбор данных
def creating_file(description, CheckBox5, CheckBox1, CheckBox3, status, priority, service, influence, 
                  type_of_work, start_time_label_1, start_plan_label_1, end_plan_label_1, end_time_label_1):

    date_now = False

    MSKutc = "+03:00"

    plus1 = start_time_label_1 + MSKutc

    plus2 = start_plan_label_1 + MSKutc

    plus3 = end_plan_label_1 + MSKutc

    plus4 = end_time_label_1 + MSKutc

    MSKdateformat1 = None
    MSKdateformat2 = None
    MSKdateformat3 = None
    MSKdateformat4 = None

    rf = [plus1, plus2, plus3, plus4]
    rf2 = [MSKdateformat1, MSKdateformat2, MSKdateformat3, MSKdateformat4]

    rfs = len(rf)
    rfs2 = len(rf2)


    for Y in range(rfs):
        if date_now == False:
            if rf[Y] != '':

                qustion = arrow.get(rf[Y])
                rf2[Y] = qustion.format('YYYY-MM-DDTHH:mm:ssZZ')

            else:

                utc = arrow.utcnow()

                MSKtimezone = utc.to('Europe/Moscow')
                rf2[Y] = MSKtimezone.format('YYYY-MM-DDTHH:mm:ssZZ')
        else: 
            rf2[Y] = ''

        Y += 1


    k = random.randint(10, 100)
    k = int(k) + 1 # переделать нахер

    if CheckBox5 == 0:
        in_report = False
    else:
        in_report = True

    if CheckBox1 == 0:
        checkbox_2 = False
    else:
        checkbox_2 = True

    if CheckBox3 == 0:
        checkbox_3 = False
    else:
        checkbox_3 = True


    NSMAP = {'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                'ext': 'http://schemas.mts.ru/extsys_saes/'}
    root = lxml.etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope', nsmap=NSMAP)

    Header = lxml.etree.SubElement(root, '{http://schemas.xmlsoap.org/soap/envelope/}Header')

    Body = lxml.etree.SubElement(root, '{http://schemas.xmlsoap.org/soap/envelope/}Body')

    Create_Work = lxml.etree.SubElement(Body, '{http://schemas.mts.ru/extsys_saes/}Create_Work')

    WorkType = lxml.etree.SubElement(Create_Work, 'WorkType')
    WorkType.text = 'Create_Work'

    ClassificatorCause = lxml.etree.SubElement(Create_Work, 'ClassificatorCause')
    ClassificatorCause.text = type_of_work

    Status = lxml.etree.SubElement(Create_Work, 'Status')
    Status.text = status

    Priority = lxml.etree.SubElement(Create_Work, 'Priority')
    Priority.text = priority

    ShortDescription = lxml.etree.SubElement(Create_Work, 'ShortDescription')
    ShortDescription.text = description

    NE = lxml.etree.SubElement(Create_Work, 'NE')
    NE.text = 'Согласно приложенному файлу'

    ServiceType = lxml.etree.SubElement(Create_Work, 'ServiceType')
    ServiceType.text = service

    ServiceImpactCls = lxml.etree.SubElement(Create_Work, 'ServiceImpactCls')
    ServiceImpactCls.text = influence

    PlanStart = lxml.etree.SubElement(Create_Work, 'PlanStart')
    PlanStart.text = rf2[0]

    PlanBegRestrictService = lxml.etree.SubElement(Create_Work, 'PlanBegRestrictService')
    PlanBegRestrictService.text = rf2[1]

    PlanEndRestrictService = lxml.etree.SubElement(Create_Work, 'PlanEndRestrictService')
    PlanEndRestrictService.text = rf2[2]

    DeadLine = lxml.etree.SubElement(Create_Work, 'DeadLine')
    DeadLine.text = rf2[3]

    ExecutorGroupID = lxml.etree.SubElement(Create_Work, 'ExecutorGroupID')
    ExecutorGroupID.text = 'MSK000000012749'

    ExecutorLogin = lxml.etree.SubElement(Create_Work, 'ExecutorLogin')
    ExecutorLogin.text = 'drmazurin'

    InitiatorLogin = lxml.etree.SubElement(Create_Work, 'InitiatorLogin')
    InitiatorLogin.text = 'drmazurin'

    SupervisorLogin = lxml.etree.SubElement(Create_Work, 'SupervisorLogin')
    SupervisorLogin.text = 'drmazurin'

    SupervisorGroupID = lxml.etree.SubElement(Create_Work, 'SupervisorGroupID')
    SupervisorGroupID.text = 'MSK000000012749'

    HwSubSystem = lxml.etree.SubElement(Create_Work, 'HwSubSystem')
    HwSubSystem.text = 'Радиоподсистема'

    Description = lxml.etree.SubElement(Create_Work, 'Description')
    Description.text = description

    ExtID = lxml.etree.SubElement(Create_Work, 'ExtID')
    ExtID.text = 'extID' + str(k)

    InReport = lxml.etree.SubElement(Create_Work, 'InReport')
    InReport.text = str(in_report)

    GetSupplier = lxml.etree.SubElement(Create_Work, 'GetSupplier')
    GetSupplier.text = str(checkbox_2)

    NotifyService = lxml.etree.SubElement(Create_Work, 'NotifyService')
    NotifyService.text = str(checkbox_3)

    OperationID = lxml.etree.SubElement(Create_Work, 'OperationID')
    OperationID.text = '4578eb18-5a3b-4224-8960-47775'

    HwRegion = lxml.etree.SubElement(Create_Work, 'HwRegion')
    HwRegion.text = 'М\Москва'

    Main_NIOSS_ID = lxml.etree.SubElement(Create_Work, 'Main_NIOSS_ID')
    Main_NIOSS_ID.text = '9127631760513307442'

    Module = lxml.etree.SubElement(Create_Work, 'Module')
    Module.text = 'Parameters Consistency'

    StartedBands = lxml.etree.SubElement(Create_Work, 'StartedBands')
    StartedBands.text = 'UMTS-2100'

    file_name = str(k) + "text.xml"

    handle = lxml.etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)
    with open(os.path.join(os.getcwd(), file_name), "wb") as f:
        f.write(handle)

    cmd = 'java jms_sender {file_name}'
    os.system(cmd)