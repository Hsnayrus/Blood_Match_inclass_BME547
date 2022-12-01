import requests

url = "http://vcm-7631.vm.duke.edu:5002"
get_sj346 = requests.get(url + "/get_patients/sj346")
response_dict = get_sj346.json()
patient_1 = response_dict["Donor"]
patient_2 = response_dict["Recipient"]
blood_type_p1_resp = requests.get(url + "/get_blood_type/" + patient_1)
blood_type_p2_resp = requests.get(url + "/get_blood_type/" + patient_2)
blood_type_p1 = blood_type_p1_resp.text
blood_type_p2 = blood_type_p2_resp.text
answer = blood_type_p1 == blood_type_p2
if answer: 
    answer = "Yes"
else:
    answer = "No"
json_to_send = {"Name": "sj346", "Match": answer}
request_final = requests.post(url + "/match_check", json=json_to_send)
print(blood_type_p1, blood_type_p2, request_final.text)
