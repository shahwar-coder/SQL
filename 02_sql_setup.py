'''
1. Download & Install Docker : Go to docker.com 
 -> Download Docker Desktop 
 -> Download for Mac (Apple Chip)
 -> Docker.dmg file is downloaded (~500 MB)
 -> Click downloaded file
 -> Option to Drag the Docker App to Application folder appears, we drag it
 
2. Setup:
 -> Accept T&C and Finish
 -> Password  Filling Dialogue Box appears, fill your mac password.
 -> Click Create Docker Account, you will be directed to a browser
 -> Sign Up 
 
3. Install Azure Studio:
 -> Search and Click Azure Data Studio
 -> Navigate macOS -> Click Apple Silicon
 -> File - azuredatastudiomacosarm64.zip gets downloaded
 -> Click on the file to unzip it
 -> You will have Azure Studio Application, drag it to Applications folder
 -> Now you can open it
 
4. Install MSSQL:
 -> Search azure-sql-edge docker
 -> Copy the command: "docker pull mcr.microsoft.com/azure-sql-edge:latest"
 -> Open Termainal, paste and run this command
 -> Now the image is pulled
 -> You can now go to Docker Desktop and check the image there in image section
 -> Run this command to run docker container :"docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=MyStrongPass123" -e "MSSQL_PID=Developer" -e "MSSQL_USER=SA" -p 1433:1433 -d --name=sql mcr.microsoft.com/azure-sql-edge"
 -> You can go back to Docker Desktop and check the running container in container section
 
5. Final Step:
 -> Go to Azure Data Studio
 -> Select New Connection
 -> Connection Type : Microsoft SQL Server
 -> Input Type : Parameters
 -> Server : localhost
 -> Authentication : SQL Login
 -> User name : SA
 -> Password : **********
 -> Click on Remember Password
 -> Click Connect
 -> Click Enable Trust Server Certificate
 -> Now you are conncted to MSSQL Server
'''
