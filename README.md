# filed-audio-assignement


## StartUp
*Pre-requisites*
~ Highly recommend to have a linux machine
1. Install docker
2. clone the repository - 
3. change directory to assignment root file - `cd filed-audio-assignement`
4. run `docker-compose up --build`

* Falsk application api endpoints
  > * create new audio file - `http://0.0.0.0:5000/audio/create` [POST method]
  >   ```
  >   // test case 1 - song JSON
  >     {
  >       "audioFileType": "song",
  >       "audioFileMetadata": {
  >         "name": "perly",
  >         "duration": 2
  >       }
  >     }
  >     
  >   // test case 2 - podcast JSON
  >     {
  >       "audioFileType": "podcast",
  >       "audioFileMetadata": {
  >         "name": "perly",
  >         "duration": 2,
  >         "host": "robin",
  >         "participants":["John Doe", "Mark", "Ross", "Rachel"]
  >       }
  >     }
  >     
  >     // test case 3 - audiobook JSON
  >     {
  >       "audioFileType": "audiobook",
  >       "audioFileMetadata": {
  >         "title": "perly",
  >         "duration": 2,
  >         "author": "Robin",
  >         "narrator": "Rajamouli"
  >       }
  >     }
  >   ```
  > * delete existing file - `http://0.0.0.0:5000/audio/<audioFileType>/<audioFileId>` [DELETE method]
  > * update existing file - `http://0.0.0.0:5000/audio/<audioFileType>/<audioFileId>` [PUT method]
  >   ```
  >   // test case 1 - song JSON
  >     {
  >       "audioFileMetadata": {
  >         "name": "John",
  >         "duration": 200
  >       }
  >     }
  >     
  >   // test case 2 - podcast JSON
  >     {
  >       "audioFileMetadata": {
  >         "name": "John",
  >         "duration": 200,
  >         "host": "robin",
  >         "participants":["John Doe", "Mark", "Ross", "Rachel"]
  >       }
  >     }
  >     
  >     // test case 3 - audiobook JSON
  >     {
  >       "audioFileMetadata": {
  >         "title": "John",
  >         "duration": 200,
  >         "author": "Robin",
  >         "narrator": "Sam"
  >       }
  >     }
  >   ```
  > * get existing file - `http://0.0.0.0:5000/audio/<audioFileType>/<audioFileId>` [GET method]
