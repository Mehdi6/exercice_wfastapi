# Querying broadcasting channels data through REST Api using FastAPI
This Rest API is supposed to solve a technical test. It uses FastAPI as a python framework for the implementation. 

## The Rest API 

Tools:
- fastapi==0.95.1
- slowapi==0.1.8
- fastapi-pagination==0.12.2
- uvicorn==0.22.0
- pydantic==1.10.7
- pandas==1.5.2
- fastapi-cache==0.21.0
- python 3.10.11
    
How it works:

- pull the git the repository to your local machine.
- Install pipenv and run `pipenv install` on the dev folder.
- Run `pipenv shell` and go to the folder "code" (if on windows, "cd code").
- Run the command line `uvicorn main:app --reload`
- Now your server is running, you can start requesting data through your browser or postman.

How to test if it works:

- if everything is setup well and you have run the server successfully you can test the Rest API by simply running one of the following endpoints:
	-- http://127.0.0.1:8000/top10/Atn
	-- http://127.0.0.1:8000/tvshows?page=12

- testing pagination:
	-- you can additionally to the page number, add the page size which might be usefull to control the number of items on a batch of data (http://127.0.0.1:8000/tvshows?page=12&size=100). The default batch size is 50.
	
Enhanced features for better performance and security:

- For controlling the number of requests performed by a specific user, we've added trottling, which can be usefull to reduce the overheight on the server when there is a big number of requests sent by a user or a group of users. This feature takes as input the number of requests authorized by a user per minute for example.

- For better performances, we have used caching, since the data is being updated one time during the day exactly when the generated file is dropped in the server, we don't need to process the data every time we request it. 


## Issue Reporting

If you have found a bug or feature request, please report them at the repository issues section.

## License 

MIT

## Acknowledgements

In this exercices, we have used different libraries that have been very usefull to make the implementation quick and efficient. Thanks to the community for working on developping these libraries and tools and making them free for use.
