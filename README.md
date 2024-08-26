# fast-session
Web app that uses a Amazon Bedrock LLM API to help student get career advice

# How to Run
Install node on your machine and then run the block of code below to open the app on your browser:
```
npm i
cd client
cd src
npm run dev
```

Next, to run the server, open another terminal and go to the server folder.
This process is more complicated because you need to configure Amazon Bedrock on your machine with your account.
Here is a link to help you set it up: [Bedrock Site](https://aws.amazon.com/bedrock/?gclid=Cj0KCQjwz7C2BhDkARIsAA_SZKaJPdxvpTT6bypCoQEwqd935VwfGTY5jhEC78mW_Ek18eMxLAIQ-rEaAgJrEALw_wcB&trk=e2792953-875b-4140-9d37-0f1aa692ec25&sc_channel=ps&ef_id=Cj0KCQjwz7C2BhDkARIsAA_SZKaJPdxvpTT6bypCoQEwqd935VwfGTY5jhEC78mW_Ek18eMxLAIQ-rEaAgJrEALw_wcB:G:s&s_kwcid=AL!4422!3!692005991752!p!!g!!aws%20bedrock!21048268446!157173584137)

After you have bedrock set up with your AWS account, run from root folder:
```
cd server
pip install -r requirements.txt
python app.py
```
NOTE: The bedrock process is very teadious and long if you have never worked with AWS
