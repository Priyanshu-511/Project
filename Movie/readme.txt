Pre-SetUP of movieMAnia website.
Priyanshu Kumar
April 2024
1 Set-up to use website
IT IS FOR WINDOWS
Step-1: Install VS Code.
Step-2: Download and install the LTS version of Node.js from the Node.js website. You can find it here.
Step-3: part-1 Download and install mongodb community server from link.
part-2 choose complete set-up type and click on next continously then give permission oon clicking allow to this maake app changes to your devices.
Step-4: Download mongodb shell from link.
Step-5: Extract mongodb in C :> P rogramF iles > MongoDB
Step-6: Copy C :> P rogramF iles > MongoDB > mongosh − 2.2.3 − win32 −
x64 > bin to path (in system variable of enviromental variable)
Step-7: Open your PowerShell Terminal to check it completely work or not.
Type mongosh
Step-8: Close your terminal.
Step-9: Open VS-code then open vs code terminal by pressing ctrl+shift+‘ .
Step-10: type:-
npm init
npm i express
npm i hbs
npm i mongoose
npm i nodemon
npm i path
Step-11: Run your PowerShell terminal as administrator through Run as administrator. Then type Set-ExecutionPolicy Unrestricted and pressed enter key. Then type A pressed enter key.
Step-12: Run Mongodb compass.
URL must be mongodb://localhost:27017/ then click on save and connect option enter the name movieMAnia. Click on save and connect.
Step-13: Open my every file in VS code.
Step-14: Open VS code terminal by pressing ctrl+shift+‘ .
Step-15: Type: nodemon src/index.js and pressed enter key.
Step-16: Open web browser type localhost:5000.
1
IF IT SHOW ERROR. THEN DISCONNECT YOUR MongoDbCompass AND AGAIN CONNECT
IT.
2 terminal use
type into terminal
python -m pip install flask
python -m pip install bs4
python -m pip install requests
python -m pip install numpy
in movies.json there is an error . you have to replace (\) with ("
").
3 VS Code
type nodemon src/server.js
4 web browser
type localhost:5000
5 BUG
firstly it was successfully link with mongodb. but now it won’t. especially for
registration data.
another bug is recommender only work if i put whole name of movie (it is spacesensitive).
to fixing so many thing it will make some of bug and i identify some
of them.
