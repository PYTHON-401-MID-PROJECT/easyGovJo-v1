from flask import request
from bot import app
from web_scraping.vehicle_validation import vehicle_validation
from web_scraping.financial_status import financial_status
from web_scraping.violations_lookup import violations_lookup
from web_scraping.roof_tax import roof_tax
from web_scraping.land_location import land_location

processes = {"11":["الإستعلام عن المخالفات", 3, [" أمانة عمان الكبرى - الإستعلام عن المخالفات\n\n أدخل رقم المركبة لطفاً", "أدخل الترميز", "أدخل رقم التسجيل"], vehicle_validation], "12":["المالية لوزارة المالية", 1, ["الذمم المالية المتحققة بذمتكم لوزارة المالية / مديرية الأموال العامة\n\nأدخل الرقم الوطني لطفاً"], financial_status], "13":["قيم مخالفات السير", 1, ["الاستعلام عن قيم مخالفات السير حسب قانون السير رقم 48 \n\n أدخل جزء من وصف المخالفة لطفاً"], violations_lookup], "14":["ضريبة الأبنية والمسقفات", 2, ["ضريبة الأبنية والمسقفات \n\n أدخل الرقم الوطني لطفاً", "أدخل رقم الهوية"], roof_tax], "15":["الاستعلام عن قطعة أرض", 1, ["دائرة الأراضي والمساحة - الاستعلام عن قطعة أرض\n\n أدخل مفتاح القطعة لطفاً"], land_location]}
responses = {}  
current_process = "" 

def service(incoming_msg, phone_number):
    global current_process
    global process_values
    global question
    # incoming_msg = request.values['Body']
    # phone_number = request.values['WaId']
    
    if incoming_msg in processes:
        current_process = incoming_msg
        process_values = processes[incoming_msg][0]
        responses[process_values] = []  
        question = 0
        app.send_message(f"{processes[current_process][2][question]} \n\nللخروج في أي وقت، فقط اضغط 0", phone_number)
    
    elif incoming_msg == "0":
        del responses[process_values]
        current_process = ""
        app.send_message("تم إلغاء العملية", phone_number)

    elif processes[current_process][0] in responses:
        if len(responses[process_values]) < processes[current_process][1]:  
            responses[process_values].append(incoming_msg)  
            remaining_responses = processes[current_process][1] - len(responses[process_values]) 
            if remaining_responses > 0:
                question += 1
                app.send_message(processes[current_process][2][question], phone_number)
            else:
                collected_responses = responses[process_values]
                do_service = processes[current_process][3]
                del responses[process_values]
                app.send_message("شكراً لك، انتظر النتيجة", phone_number)
                service_result = do_service(*collected_responses)
                
                if current_process == "15":
                    app.send_media_message(service_result, phone_number)

                elif isinstance(service_result, tuple):       # to handle long twilio's message
                    for ele in service_result:
                        app.send_message(ele, phone_number)
                else:
                    app.send_message(service_result, phone_number)
                current_process = ""
