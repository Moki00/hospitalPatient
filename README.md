# Team 3 for McKenney’s

This is a WebApp to be used on a tablet for a patient in a hospital.

## Usage

 [WebApp link](https://moki929.github.io/) <---- here

 [McKenney's Info](https://docs.google.com/document/d/1UEjvY1xMrd0HxizS0Tk2cYwiuSoOBhEF/edit) for this project

 [blue logos](https://doctormultimedia.com/medical-logos-blue/) for hospitals

 [Walkthrough](https://www.khanacademy.org/computing/computer-programming/html-css/web-development-tools/a/hosting-your-website-on-github) on how to host on Github

## Example

```javascript
fetch(‘https://{deviceIP}/api/rest/v1/protocols/bacnet/local/objects/{objectType}/{objectInstance}/properties/presentValue’,{
 	method: ‘POST’,
	headers: {
		Set-Cookie: ` ECLYPSERESTSESSIONID=1ihtgt27axib71plskbk2nhp4i`,
		Content-Type: ‘application/json’
		
},
body: JSON.stringify({ value: 70 }),

         })
         .then(response => {
	return response.json();
         });

```

## Group Members

Morgan King, Keshav Raviprakash, Eric Chow, and Ahmed Legesse

## TimeStamp

We started coding Oct 1st and are submitting code Oct 2nd by 6pm of 2022